# Belge Türleri — Tanıma ve Künye Çıkarımı

Belgeyi HTML'e dönüştürdükten sonra türünü belirle ve künyesini çıkar. Her türde **kritik
tarih(ler)** ayrıca işaretlenmeli; süreler genelde bu tarihlerden işler (bkz. [hesaplama.md](hesaplama.md)).

## Her belgede çıkarılacak ortak künye
- **Mahkeme / merci**: ad ve daire (örn "Ankara 5. Asliye Hukuk Mahkemesi", "Yargıtay 4. HD").
- **Esas no / karar no**: `2021/123 E.`, `2022/456 K.` biçimi.
- **Taraflar ve vekiller**: davacı/davalı, sanık/katılan, alacaklı/borçlu + avukatları.
- **Tarihler**: belge/karar tarihi, tebliğ tarihi, duruşma tarihi.
- **Konu/talep/hüküm**: bir cümlede ne istendiği veya ne karara bağlandığı.

## Dava ve cevap dilekçeleri
- **Dava dilekçesi** — "DAVA", "NETİCE-İ TALEP/TALEP SONUCU", "AÇIKLAMALAR", "HUKUKİ SEBEPLER",
  "DELİLLER" başlıkları. Çıkar: talep sonucu, vakıalar, deliller, dava değeri/harç.
- **Cevap dilekçesi** — Davalının savunması; usule itirazlar (yetki, görev, derdestlik, zamanaşımı),
  esasa cevap. Kritik tarih: **dava dilekçesinin tebliğ tarihi**.
- **Replik / Düplik** — Dilekçeler aşamasının devamı.

## Mahkeme kararları
- **Kısa karar (hüküm)** — Duruşmada açıklanan hüküm fıkrası; gerekçe yok.
- **Gerekçeli karar** — "GEREĞİ DÜŞÜNÜLDÜ", "HÜKÜM", "GEREKÇE", "KANUN YOLU" bölümleri. Çıkar:
  hüküm fıkrası, gerekçenin özü, **kanun yolu ve süresi**, karar tarihi. Kritik tarih: kararın **tebliğ tarihi**.
- **İstinaf kararı (BAM)** — istinafın kabul/ret/düzeltilerek esastan sonucu.
- **Yargıtay/Danıştay kararı** — **onama** veya **bozma** (bozmada gerekçe belirleyici).

## Tutanaklar ve ara belgeler
- **Tensip zaptı/tutanağı** — Dava açılışında ilk işlem listesi: tebligatlar, süreler, ara kararlar.
- **Duruşma tutanağı** — Duruşma tarihi, hazır bulunanlar, beyanlar, ara karar, gelecek duruşma.
- **İhtiyati tedbir / ihtiyati haciz** — Geçici hukuki koruma; teminat ve kapsam.
- **Bilirkişi raporu** — Teknik değerlendirme; sonuç ve hesap tablosu kritik. Kritik tarih: rapor +
  **tebliğ tarihi** (itiraz süresi buradan).
- **Müzekkere** — Mahkemeden başka kuruma bilgi/belge talebi yazısı.
- **Keşif/ekspertiz tutanağı** — Yerinde inceleme tespitleri.

## Tebligat ve icra belgeleri
- **Tebligat / tebliğ mazbatası** — En kritik tarih kaynağı: **tebliğ tarihi**. Kime, nasıl
  (bizzat/mernis/ilan) tebliğ edildiğini de çıkar.
- **İhtarname (noter)** — Temerrüt ihtarı; faiz başlangıcı için önemli.
- **Ödeme emri (icra)** — Örnek no (7/10 vb.), borç tutarı, takip dayanağı; itiraz süresi.
- **Haciz tutanağı / kıymet takdiri** — Haczedilen mal, takdir edilen değer.

## Sınıflandırma ipuçları
- Üst başlık çoğu zaman türü açıkça verir ("DAVA DİLEKÇESİ", "GEREKÇELİ KARAR", "TENSİP TUTANAĞI").
- Daire + "Esas/Karar" + "GEREĞİ DÜŞÜNÜLDÜ/HÜKÜM" → mahkeme kararı.
- "NETİCE-İ TALEP/TALEP SONUCU" → dilekçe.
- "Tebliğ tarihi", "mazbata", "bila tebliğ" → tebligat belgesi.
- Tür belirsizse: en üst blok (merci + başlık) ile imza/onay bloğunu birlikte değerlendir.
