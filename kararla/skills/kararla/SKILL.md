---
name: kararla
description: >-
  Türk hukukunda araştırma, hesaplama ve belge analizi için kapsamlı asistan; Kararla'nın
  içtihat, mevzuat, finansal/tarih ve UYAP belge dönüştürme araçlarını birlikte kullanır.
  Şu durumlarda devreye girer: emsal Yargıtay/Danıştay/BAM kararı veya kanun maddesi
  araştırmak; bir hukuki soruyu ya da olayı içtihat ve mevzuatla yanıtlamak; yasal süre
  (istinaf/temyiz/itiraz), temerrüt/yasal faiz, TÜFE güncellemesi, döviz/altın alacağı
  hesaplamak; UYAP/e-Devlet'ten alınan .udf dosyalarını ve dava belgelerini (dilekçe,
  mahkeme kararı, bilirkişi raporu, tebligat, icra evrakı) okuyup analiz etmek ve içindeki
  atıfları doğrulamak. "içtihat", "emsal karar", "Yargıtay", "mevzuat", "kanun maddesi",
  "TCK", "HMK", "faiz", "süre hesabı", ".udf", "UYAP", "dava dosyası" veya genel bir Türk
  hukuku işi geçtiğinde kullanılır.
license: Proprietary
metadata:
  author: Kararla
  version: "1.0"
  domain: Turkish law
---

# Kararla Hukuk Asistanı

Türk hukuku işlerinde Kararla'nın araç ailesini orkestra eden asistan. Dört yetenek alanı:

1. **İçtihat araştırması** — emsal Yargıtay/Danıştay/BAM/yerel mahkeme kararları.
2. **Mevzuat araştırması** — kanun ve yönetmelik maddeleri (güncel/mülga).
3. **Hesaplama** — yasal süre, temerrüt/yasal faiz, TÜFE güncellemesi, döviz/altın alacağı.
4. **Belge okuma & analiz** — UYAP `.udf` ve dava belgelerini HTML'e çevirip inceleme.

Asıl değer bunları **birleştirmektir**: bir soruyu emsalle yanıtla → dayanağı mevzuattan
doğrula → süre/faiz hesapla → yüklenen belgedeki atıfları teyit et.

---

## Araç haritası

**İçtihat (mahkeme kararları)**
| Araç | İş | Anahtar argüman |
|---|---|---|
| `ictihat_semantik_arama` | Olay/hukuki soruyla anlamsal emsal | `question` (+ tarih, `court_types`) |
| `ictihat_metin_arama` | Belirli ibare/terim geçen kararlar (Bleve, sayfalı) | `query` |
| `ictihat_kunye` | Esas/karar no ile karar → `uid` | `case_number` / `decision_number` |
| `ictihat_detay` | Kararın tam metni | `uid` |

**Mevzuat (kanun maddeleri)**
| Araç | İş | Anahtar argüman |
|---|---|---|
| `mevzuat_semantik_arama` | Konuyla ilgili maddeler | `question` |
| `mevzuat_kunye` | Kanunu bul (TCK/5237) → `mevzuat_id` | `mevzuat_no` \| `short_name` \| `mevzuat_adi` |
| `mevzuat_madde` | Belirli maddeyi tam metniyle | `mevzuat_id` + `article_number` |

**Hesaplama (finansal & tarih)**
| Araç | İş | Anahtar argüman |
|---|---|---|
| `faiz_orani` | Temerrüt/yasal/reeskont/politika faizi | `rate_type` + tarih aralığı |
| `tufe` | Enflasyon güncellemesi | tarih aralığı |
| `doviz_kuru` / `doviz_kuru_gunluk` | Döviz alacağı | tarih(ler) |
| `altin_fiyati` / `altin_fiyati_gunluk` | Altın alacağı | tarih(ler) |
| `bugun` | Bugün + iş günü/tatil bilgisi | — |
| `is_gunu_mu` | Tarih iş günü mü (+ sonraki/önceki iş günü) | `date` |
| `is_gunu_ekle` | Tarihe N iş günü ekle/çıkar | `date` + `days` |
| `is_gunu_say` | İki tarih arası iş günü sayısı | `start_date` + `end_date` |

**Belge**
| Araç | İş | Anahtar argüman |
|---|---|---|
| `request_api_usage` | UYAP `.udf` dönüşümü için erişim al | `operation: "udf-to-html"` (oku/analiz) \| `"udf-to-docx"` (indirilebilir Word) |

---

## Yetenek alanları (derinlik referanslarda)

### 1. İçtihat & mevzuat araştırması
Hangi araç ne zaman (anlamsal vs künye vs metin), arama→detay zincirleri ve atıf doğrulama:
→ [references/arastirma.md](references/arastirma.md)

### 2. Hesaplama
Yasal süre (mevzuattan teyit + tarih araçları), faiz, alacak güncelleme yöntemleri:
→ [references/hesaplama.md](references/hesaplama.md)

### 3. Belge okuma & analiz
`.udf` → HTML/DOCX dönüşüm akışı, token ve biçim sınırları → [references/belge-okuma.md](references/belge-okuma.md).
Belge türlerini tanıma ve künye çıkarımı → [references/belge-turleri.md](references/belge-turleri.md).
Yapılandırılmış inceleme (term-by-term + risk özeti, birebir alıntı) → [references/belge-inceleme.md](references/belge-inceleme.md).
> **Hangi format?** Belgeyi **okuyup analiz** edecek / canvas'ta göstereceksen `udf-to-html`.
> Kullanıcı **düzenlenebilir Word (.docx)** istiyorsa (`"word olarak ver"`, `"docx indir"`)
> `udf-to-docx`. İkisi de gerekiyorsa iki ayrı çağrı (iki token, iki dönüşüm sayılır).
> - **HTML** çıktısını **dosyadan AYNEN canvas'a (artifact) koy** — yeniden yazma/özetleme YAPMA
>   (uzun belgede veri kaybı/kırpılma riski; HTML zaten tam ve hazır).
> - **DOCX** ikilidir → canvas'a KOYMA; kullanıcıya indirilebilir dosya yolunu bildir.
> - Çıktı **yazılabilir dizine** yazılır; yüklenen dosyanın dizini (`/mnt/user-data/uploads/`)
>   salt-okunurdur, oraya yazma.

---

## Tipik iş akışları

**Bir hukuki soruyu yanıtlama**
1. `mevzuat_semantik_arama` ile ilgili maddeleri, `ictihat_semantik_arama` ile emsalleri tara.
2. Kilit madde/kararları `mevzuat_madde` / `ictihat_detay` ile tam metinden teyit et.
3. Cevabı resmi numara ve birebir alıntılarla, mülga/değişiklik notlarıyla ver. Karmaşık/çok-dayanaklı
   analizde [memo formatında](references/arastirma.md) ver (Olay→Sorun→Mevzuat/Emsal→Değerlendirme→Sonuç).

**Yüklenen dava belgesini inceleme**
1. `.udf` ise [references/belge-okuma.md](references/belge-okuma.md) akışıyla HTML'e çevir; dönüşmüş HTML'i dosyadan AYNEN canvas'a koy (yeniden yazma).
2. Türünü ve künyesini çıkar ([references/belge-turleri.md](references/belge-turleri.md)).
3. Yapılandırılmış incele (term-by-term + risk, birebir alıntı) → [references/belge-inceleme.md](references/belge-inceleme.md).
4. Belgedeki kanun/karar atıflarını araçlarla doğrula ([references/arastirma.md](references/arastirma.md)).
5. İlgili süre/faiz hesaplarını yap ([references/hesaplama.md](references/hesaplama.md)).

**Süre/alacak hesabı**
1. Belge/olaydan başlangıç tarihini (tebliğ/temerrüt) ve ilgili usul kanununu belirle.
2. Süre maddesini `mevzuat_madde` ile teyit et; son günü tarih araçlarıyla hesapla.
   Adli tatil ve çoklu-saat ayrımını gözet; hak düşürücü sürede kritik uyarı bas ([hesaplama.md](references/hesaplama.md)).
3. Faiz/güncellemeyi `faiz_orani` / `tufe` / `doviz_kuru` ile hesapla, kaynak oran/tarihle sun.

---

## Önemli kurallar

- **Atıf uydurma.** Her kanun maddesini ve emsal kararı, metne yazmadan önce ilgili araçla
  **doğrula** (mülga mı, güncel metni ne, karar gerçekten o yönde mi).
- **Provenance etiketle.** Tool sonucundan geleni `[Kararla — doğrulandı]`, genel bilgiden geleni
  `[model bilgisi — teyit edin]` ile işaretle; etiket kaynağı anlatır, doğruluğu değil
  → [references/guardrails.md](references/guardrails.md) (provenance + injection + degradation).
- **`mevzuat_no` ≠ `mevzuat_id`.** Resmi numara/ad (5237, TCK) kullanıcıya yazılır; `mevzuat_id`
  ve karar `uid` backend iç kimliğidir — **yalnız araç argümanı**, metne yazma.
- **Hesabı elle yapma.** Süre, faiz, TÜFE/döviz güncellemesini zihinden değil ilgili araçla yap
  (tatil/iş günü ve resmi oranlar araçta doğru gelir); sonucu kullanılan oran/tarihle birlikte sun.
- **Yasal süreyi ezbere verme.** Süreyi önce ilgili usul kanunundan (`mevzuat_madde`) teyit et.
- **Belge gizliliği.** Belgeler hassas kişisel veri içerebilir; analizde kullanıcının istediğine
  odaklan, gereksiz kişisel bilgiyi öne çıkarma.
- **Kaynağı göster.** Verdiğin her hukuki dayanağı (madde no, karar künyesi, oran tarihi) belirt;
  kullanıcı doğrulayabilsin.
