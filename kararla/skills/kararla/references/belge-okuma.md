# Belge Okuma (UYAP .udf → HTML)

UYAP `.udf` ikili (zip tabanlı) bir formattır; düz metin olarak okunamaz, önce HTML'e
dönüştürülür. Dönüşüm Kararla sunucusunda yapılır; dosya sandbox'tan doğrudan API'ye gider.

## Akış

### Adım 1 — Erişim al
Önce **operasyonu seç**: belgeyi okuyup analiz edecek / canvas'ta göstereceksen `udf-to-html`;
kullanıcı düzenlenebilir Word (.docx) istiyorsa `udf-to-docx`. `request_api_usage` MCP tool'unu
seçtiğin `operation` ile çağır → `{ token, url }`. (İkisi de gerekiyorsa iki ayrı çağrı.)

### Adım 2 — Dönüştür
Yüklenen `.udf`'i bul, script ile dönüştür:
```bash
ls -la; find . -maxdepth 3 -iname "*.udf" 2>/dev/null   # dosya adı belli değilse
python scripts/convert_udf.py <udf_dosyasi> "<url>" "<token>"
```
- Script operasyon-agnostiktir: **yanıt şekline göre** ya HTML (`.html`, metin) ya da DOCX
  (`.docx`, ikili) yazar — `url` hangi endpoint'i çağırdığını belirler.
- Çıktıyı **yazılabilir bir dizine** otomatik yazar (claude.ai'da `/mnt/user-data/outputs`) ve
  yolu basar. **Çıktı yolunu elle verirken yüklenen dosyanın dizinini (örn. `/mnt/user-data/uploads/`)
  KULLANMA** — orası salt-okunurdur, `OSError [Errno 5]` alırsın. 4. argümanı boş bırak, script doğru yeri seçer.
- Hata kodlarını Türkçe mesaja çevirir (401/403/413/422/429).

### Adım 3 — Çıktıyı kullan

**HTML (`udf-to-html`) → canvas:** Üretilen HTML dosyasını oku ve içeriğini AYNEN bir HTML
artifact'a (canvas) koy.
- HTML'i **yeniden yazma, özetleme veya yeniden üretme** — dosyadaki içeriği **birebir** kullan.
  (Uzun belgelerde elle yeniden yazmak veri kaybına/kırpılmaya yol açar; dönüşmüş HTML zaten tam ve hazır.)
- Dosyayı oku → içeriğini olduğu gibi artifact'ın gövdesine ver. Kullanıcı belgeyi okunabilir görür,
  `/mnt/user-data/outputs`'taki dosyayı da indirebilir.

**DOCX (`udf-to-docx`) → indirme:** Üretilen `.docx` ikili bir dosyadır → **canvas'a KOYMA**
(içeriğini okuyup yazmaya çalışma; bozulur). Kullanıcıya `/mnt/user-data/outputs/...` yolunu
indirilebilir dosya olarak bildir. Belgeyi ayrıca analiz etmen de gerekiyorsa onu `udf-to-html`
ile (ikinci çağrı) oku.

Sonra belgeyi incele:
1. Türünü ve künyesini çıkar → [belge-turleri.md](belge-turleri.md).
2. Atıf yapılan madde/kararları doğrula → [arastirma.md](arastirma.md).
3. İlgili süre/faiz hesaplarını yap → [hesaplama.md](hesaplama.md).

## Token yaşam döngüsü
- **60 saniye** geçerli — `request_api_usage`'ı çağırır çağırmaz dönüştür, arada uzun işlem yapma.
- **Tek kullanımlık** — bir başarılı dönüşüm token'ı tüketir; ikinci deneme `401` döner → yeni token al.

## Manuel curl (script yoksa fallback)
```bash
curl -sS -X POST "$URL" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/octet-stream" \
  -H "User-Agent: kararla-skill/1.0" \
  --data-binary @"$UDF_PATH"
```
> **`User-Agent` ŞART:** Cloudflare bot-koruması bazı varsayılan UA'ları (özellikle `Python-urllib`,
> bazı durumlarda `curl/*`) **1010** ile bloklar → 403/HTML hata sayfası, JSON gelmez. Script bu yüzden
> `kararla-skill/1.0` gönderiyor; manuel çağrıda da **aynı header'ı ekle**. Python ile yapıyorsan
> `urllib.request.Request(..., headers={"User-Agent": "kararla-skill/1.0", ...})` — UA'sız `urllib` kesin bloklanır.
`--data-binary` şarttır (`-d` ikili dosyayı bozar). Yanıt JSON:
- `udf-to-html` → `{ html, quality, warnings, meta }`.
- `udf-to-docx` → `{ format, mime, content_base64, quality, warnings, meta }`; `.docx`'i almak için
  `content_base64`'ü base64-decode et (`... | base64 -d > belge.docx`).

## Hata tablosu
| Kod | Anlam | Ne yap |
|---|---|---|
| 401 | Token geçersiz/dolmuş/kullanılmış | `request_api_usage` ile yeni token al |
| 403 | İşlem kullanıcının planına dahil değil | Plan yükseltmesi gerektiğini bildir |
| 413 | Dosya 10MB'ı aşıyor | Küçült/böl |
| 422 | Bozuk/desteklenmeyen `.udf` | Geçerli UYAP dosyası mı doğrula |
| 429 | Hız limiti | Kısa süre bekleyip tekrar dene |

## Dönüşümde korunan / atılan biçim
- **Korunur:** metnin tamamı, paragraflar, başlıklar, **tablolar**, **kalın/italik**, listeler.
- **Atılır:** görseller, renkler, özel fontlar, antetli kağıt/logo. Biçim sadeleşir, **içerik kaybı olmaz**.

## Sınırlar
- Maksimum **10MB** (`413`). Operasyonlar: `udf-to-html` (oku/analiz), `udf-to-docx` (Word indir).
  DOCX, HTML ile **aynı içerikten** üretilir — korunan/atılan biçim kuralları (yukarıda) ikisi için de geçerli.
