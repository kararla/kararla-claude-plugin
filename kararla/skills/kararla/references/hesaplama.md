# Süre, Faiz ve Güncelleme Hesabı

> **Altın kural:** Yasal süreyi **ezbere verme**. Önce ilgili usul kanunundaki süre maddesini
> `mevzuat_madde` ile oku, sonra tarih araçlarıyla hesapla. Süreler değişir ve istisnaları vardır;
> aşağıdaki tablo yalnızca **başlangıç referansıdır**, otorite değildir.

## Süre hesabı — yöntem
1. **Süre maddesini bul.** Belge/işten ilgili usul kanununu belirle (HMK/CMK/İYUK/İİK),
   `mevzuat_kunye` → `mevzuat_madde` ile süre hükmünü ve başlangıç anını (tefhim mi tebliğ mi) oku.
2. **Başlangıç tarihini al.** Çoğu süre **tebliğ tarihinden** işler (bkz. [belge-turleri.md](belge-turleri.md)).
3. **Genel sayma ilkeleri (teyit et):** başlangıç günü kural olarak sayılmaz; süre gün/hafta/ay
   olarak işler; **son gün resmi tatil/hafta sonu ise süre sonraki iş gününe uzar.**
4. **Son günü hesapla — tarih araçlarıyla:**
   - **Takvim günü** esaslı süreler: nominal son günü bul, `is_gunu_mu` ile tatil mi kontrol et;
     tatilse araç **`nextBusinessDay`** döner → süre o güne uzar.
   - **İş günü** esaslı süreler: `is_gunu_ekle` (`date` + `days`) doğrudan iş günü ekler.
   - Geçen süreyi ölçmek için `is_gunu_say`; bugünü/tatil durumunu öğrenmek için `bugun`.

Araçlar Türkiye resmi tatillerini (Ramazan/Kurban Bayramı dahil) ve hafta sonunu hesaba katar.

### Yaygın süreler (başlangıç referansı — `mevzuat_madde` ile MUTLAKA teyit et)
| Süre | Yaklaşık | Kanun (teyit et) |
|---|---|---|
| HMK istinaf başvurusu | 2 hafta | HMK m.345 |
| HMK temyiz | 2 hafta | HMK m.361 |
| HMK cevap dilekçesi | 2 hafta (uzatılabilir) | HMK m.127 |
| CMK istinaf/temyiz | 7 gün (tefhim/tebliğden) | CMK m.273/291 |
| İdari dava açma (genel) | 60 gün | İYUK m.7 |
| İcra ödeme emrine itiraz | 7 gün | İİK m.62 |

> Bu satırlar hatırlatmadır; somut olayda süre, istisna ve başlangıç anı mutlaka maddeden doğrulanmalı.

### Adli tatil (HMK m. 102-104 — araç BİLMEZ, sen uygula)
`is_gunu_*` araçları resmi tatil + hafta sonunu hesaba katar ama **adli tatili (her yıl 20 Temmuz –
31 Ağustos) BİLMEZ.** Adli tatilde işlemeyen süreler durur; tatilin bittiği günü izleyen tarihten
itibaren **bir hafta uzamış** sayılır (HMK m. 104). Bu yüzden:
- Süre adli tatile denk geliyorsa kuralı `mevzuat_madde` (HMK m. 102-104) ile teyit et.
- Adli tatilde **duran** süre tipi mi (çoğu HMK süresi) yoksa **işleyen** mi (acele işler, m. 103) ayır.
- Araç çıktısını adli tatil için elle düzelt; sonucu "adli tatil dikkate alındı" diye işaretle.

### Çoklu-saat: aynı olayda farklı süreler
Bir olay birden çok süreyi aynı anda başlatabilir; karıştırma:
- **Taraf süresi** vs **mahkeme süresi** (farklı sahip).
- **İstinaf** (BAM, HMK m. 345) ile **temyiz** (Yargıtay, HMK m. 361) **ayrı saatlerdir**.
- Aynı kararda farklı taraflar için tebliğ tarihleri farklı olabilir → her taraf için ayrı say.
Her süreyi **sahibi + dayanağı (madde) + başlangıç tarihiyle** ayrı listele.

### Hak düşürücü / kesin süre uyarısı
Hesaplanan süre hak düşürücü ya da kesin süre ise sonucun sonuna ekle:
> ⚠️ Bu süre hak düşürücüdür; kaçırılması hakkın kaybına yol açar. Başlangıç gününü (tebliğ/tefhim)
> ve süre hükmünü ilgili usul maddesinden teyit edin; otomatik hesaba körü körüne güvenmeyin.

(Kullanıcı hukukçudur — "avukata danışın" değil, **kendi** doğrulamasını vurgula. Gate süreyi
göstermeyi engellemez; sonra teyidi öne çıkarır.)

## Faiz hesabı
Temerrüt/yasal faiz: **`faiz_orani`** (`rate_type` + tarih aralığı).
- `rate_type`: `temerrut` (ticari temerrüt / yasal faiz), `reeskont` (reeskont/avans), `politika` (TCMB politika faizi).
- Faiz başlangıcı genelde temerrüt anıdır (ihtarname/dava tarihi vb.) — belgeden/olaydan tespit et.
- Döner: tarih-oran çiftleri; dönemsel oran değişimlerini araçtan al, oran uydurma.

## Alacak/tazminat güncelleme
- **Enflasyon güncellemesi** (ör. maddi tazminatın bugünkü değeri): **`tufe`** (tarih aralığı).
- **Döviz alacağı**: **`doviz_kuru`** (cins + aralık), tek gün için `doviz_kuru_gunluk`.
- **Altın alacağı**: **`altin_fiyati`** / `altin_fiyati_gunluk`.

## Hesap kuralı
Süre, faiz ve güncelleme tutarlarını **zihinden hesaplama** — tatil günleri ve resmi oranlar
yalnız araçlarda doğru gelir. Hesabı araca yaptır, sonucu **kaynağıyla** (kullanılan oran/tarih) sun.
