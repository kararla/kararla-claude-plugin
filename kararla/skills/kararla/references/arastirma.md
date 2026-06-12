# İçtihat & Mevzuat Araştırması

Doğru aracı seçmek hız ve isabet kazandırır. Aşağıda hangi durumda hangi araç, hangi zincirle.

## İçtihat (mahkeme kararları)

**Araç seçimi**
- **Olay/hukuki soru** ile emsal aranıyorsa → `ictihat_semantik_arama` (`question`).
  Numarayı buraya YAZMA; anlamsal arama künye bulamaz.
- **Esas/karar numarası** verilmişse (örn `2021/123 E. 2022/456 K.`) → `ictihat_kunye`.
- **Belirli bir ibare/terim** geçen kararları taramak için → `ictihat_metin_arama` (Bleve:
  `"tam ibare"`, `+zorunlu`, `-hariç`, `kelime~1` fuzzy; hızlı, sayfalı). Çok sonuç gelirse
  sorguyu daralt (+zorunlu terim, tarih/`court_types` filtresi).
- Filtreler: `court_types` (yargitay_hukuk, yargitay_ceza, danistay, bam, bim, kurul, yerel),
  `start_date`/`end_date`.

**Zincir:** arama → sonuçtan `uid` → `ictihat_detay(uid)` ile **tam metin**.
- Arama sonucu özet + ilgililik puanı (0-10) + birebir alıntı + atıf maddelerini verir; tam metni
  vermez. Kararın gerçekten ne dediğini doğrulamak için `ictihat_detay` şarttır.
- Aynı künye birden çok mahkemede olabilir; hepsini değerlendir.

## Mevzuat (kanun maddeleri)

**Araç seçimi**
- **Konu** ile madde aranıyorsa → `mevzuat_semantik_arama` (`question`). `exclude_mulga` ile
  mülga maddeleri ele.
- **Belirli kanun** anılıyorsa (TCK, 5237) → `mevzuat_kunye` (öncelik: `mevzuat_no` > `short_name`
  > `mevzuat_adi`) → `mevzuat_id`.
- **Belirli madde** isteniyorsa (TCK 81, HMK 389) → önce `mevzuat_kunye` ile `mevzuat_id` bul,
  sonra `mevzuat_madde(mevzuat_id, article_number[, article_type])` → tam metin.
  - `article_type`: normal | gecici | ek | mukerrer (aynı no'da birden çoksa daralt).

## Atıf doğrulama (çapraz referans)
Bir belgedeki ya da kullanıcının verdiği atıfları **olduğu gibi kabul etme**; eski/mülga/hatalı olabilir.

- **Kanun atfı** ("TCK 86", "HMK m.119"): `mevzuat_kunye` → `mevzuat_madde` → güncel metin +
  **mülga mı**. Belgedeki ifade güncel metinle örtüşüyor mu, karşılaştır.
- **Emsal karar atfı** ("Yargıtay 4. HD 2021/123 E."): `ictihat_kunye` → `ictihat_detay`. Karar
  gerçekten o yönde mi, onama mı bozma mı?
- Bir hukuki argümanı güçlendirmek için güncel emsal: `ictihat_semantik_arama`.

## Kimlik kuralı (önemli)
- `mevzuat_no` (resmi numara, 5237/6100), `short_name` (TCK/HMK), `mevzuat_adi` → **kullanıcıya yazılır**.
- `mevzuat_id` ve karar `uid` → **backend iç kimliği**; yalnız araç argümanı, metne yazma, resmi numarayla karıştırma.
- `article_slug` madde linki içindir; link kurarken birebir kopyala.

## Sunum
- Maddeyi/kararı tırnaklarken **birebir alıntı** kullan, resmi numara/künye ile birlikte ver.
- Mülga/değişmiş hükümleri açıkça işaretle.
- Kararın yönünü (kabul/ret, onama/bozma) doğru aktar; özet ile hüküm fıkrasını karıştırma.

## Hukuki mütalaa (memo) formatı
Bir hukuki soruyu araştırıp yanıtlarken — özellikle karmaşık/çok-dayanaklı analizde — cevabı dağınık
paragraf yerine yapılandır (kısa, kesin sorularda memo şart değildir):

- **Olay** → kullanıcının anlattığı maddi vakıalar (kısa).
- **Hukuki Sorun** → çözülecek hukuki soru(lar), net cümleyle.
- **İlgili Mevzuat / Emsal Kararlar** → her dayanak künyesiyle ve `[Kararla — doğrulandı]` etiketiyle
  (madde no / karar künyesi + birebir alıntı). Yalnız tool sonucundan geleni etiketle.
- **Değerlendirme** → mevzuat/emsali olaya uygula; karşı argümanı da belirt.
- **Sonuç** → soruya net cevap + (varsa) izlenecek yol/süre.

Kurallar:
- **No silent supplement:** arama boş dönerse künye/madde **UYDURMA** — "emsal/madde bulunamadı" de,
  boşluğu doldurma. (`ictihat_*` boş sonuç sinyali: "Sonuç bulunamadı.")
- Provenance ayrımı (`[Kararla — doğrulandı]` ↔ `[model bilgisi — teyit edin]`) ve yukarıdaki
  "Atıf doğrulama" bu formatın çekirdeğidir (bkz. [guardrails.md](guardrails.md)).
