# Dilekçe Yazım Kuralları (üslup · biçim · zincir · çıktı)

Dilekçeyi yazdıktan sonra bu listeyle **sırayla** kontrol et. Bunlar üslup değil, Türk avukat
gözünde dilekçeyi "amatör" yapan tipik hataları önleyen normlardır.

## 1. Üslup
- Resmi ve hukuki dil; belirsiz ifade yok. Sert ama saygılı; ad hominem ve meslektaşa rencide yok.
- **"biz" değil "müvekkil"**; avukatı taraf yerine koyma.
- Slogan yok ("Bu dava reddedilmelidir!"). "İşbu"yu aşırı kullanma.
- İdeal cümle: en az kelimeyle anlatır. Gereksiz tekrar/vakıa yazma.

## 2. Vakıa-Delil-Hukuki Sonuç zinciri (açıklamaların omurgası)
Her vakıayı hukuki sonuca bağla — ama **"Delil:" / "Hukuki sonuç:" gibi label KULLANMA**;
zinciri doğal anlatım akışında kur (mekanik etiket dilekçeyi yapay gösterir).
- Doğru: *"Müvekkil binayı tamamlayamamıştır. Taraflar arasındaki inşaat sözleşmesi ile sabit olan
  bu durum karşısında TBK m. 117/2 uyarınca davalı temerrüde düşmüş sayılmaktadır."*
- Yanlış: *"Müvekkil binayı tamamlayamamıştır. Delil: İnşaat sözleşmesi. Hukuki sonuç: TBK m. 117/2…"*

## 3. Biçimsel kurallar (norm)
- Başlıkta **sadece** mahkeme/kurum adı — "Sayın", "Hâkimliği'ne" yok.
- Kurum eklerinde kesme işareti YOK: **MAHKEMESİNE**, **BAŞSAVCILIĞINA**. "Nöbetçi" gereksiz.
- Tek hâkimli → **MAHKEMESİNE**; heyet → **BAŞKANLIĞINA**.
- Taraf bölümünde sadece sıfat: "DAVACI"/"DAVALI" ("Cevap Veren Davalı" yazma).
- Ad: ilk harf büyük, **soyad tamamı büyük** (Ahmet YILMAZ). Tarih: gün/ay/yıl.
- Acil istem (ihtiyati tedbir/haciz): başlığın altında **büyük harf + parantez**.

## 4. Hukuki Dayanaklar bölümü
- Yan başlık **"HUKUKİ DAYANAKLAR"** (— "Hukuki Sebepler" değil), **MUTLAKA TEK SATIR**.
- Sadece davanın **özgün kilit maddesi** (belirsiz alacak → HMK m. 107; tahliye → TBK m. 315);
  genel usul maddeleri (114, 119, 120…) yazma — "HMK" zaten kapsar. Kanun adını tekrarlama.
- Kanun kısaltması (HMK). Her zaman **"ve ilgili mevzuat"** ile bitir.

## 5. Sonuç ve İstem
- **"Arz ederim" YASAK** (avukat makamla hiyerarşik değil) → "vekâleten talep ederim"/"talep ederim".
  "Saygılarımla arz ederim" çifte hata.
- Mahkemeden **ifa değil KARAR** istenir: "ödenmesine karar verilmesini talep ederim".
- Talep bölümü **gerekçe içermez**; "Yukarıda izah edilen sebeplerle," ile atıf yap, talepleri sırala.
- Önce usuli, sonra esasa dair talepler. Faiz isteniyorsa **tür + başlangıç tarihi** şart.
- Belirsiz talep ("uygun görülecek diğer kararlar") yok.

## 6. Atıf & link (uydurma yasağı)
- Madde/karar yalnız MCP tool sonucundan; tool çağrılmadıysa atıf yazma.
- **Link UYDURMA**: link yalnız araştırma sonucundaki "Link:" satırından kopyalanır; yoksa düz metin.
- Opak ID: `mevzuat_no` (5237) gösterilir; `mevzuat_id`/`article_slug` metne yazılmaz, türetilmez.

## 7. Sık yapılan dil hataları (yapma)
fesh etmek→**feshetmek** · evraklar→**evrak** · içtihad→**içtihat** · mevzuatlar→**mevzuat** ·
gayrımenkul→**gayrimenkul** · iş bu→**işbu** · muhattap→**muhatap** · hukukğa→**hukuka** (k yumuşamaz).

## HTML Formatı
İzin verilen tag: `p, h1-h4, ul, ol, li, br, strong, em, blockquote, table, colgroup, col,
tbody, tr, th, td, a`. **`html`/`body` tag ve CSS/JS yok.**
- Hizalama: `style="text-align: center|right|left"` (h1-h4 ve p).
- Taraf tablosu kenarlıksız; her satır `<td><strong>DAVACI</strong></td><td>: Ahmet YILMAZ</td>`.
- İmza: `<p style="text-align: right">`.
- Mevzuat/içtihat linki: araştırma sonucundaki "Link:" satırından `<a href="...">`. Link satırı
  yoksa link OLUŞTURMA.
- Bilgi yoksa yer-tutucu: `[AD SOYAD]`, `[ADRES]`, `[T.C. KİMLİK NO]`, `[TARİH]` — uydurma yok.

## Kısa/boş çıktı
Boş ya da anlamsız kısa çıktı reddedilir; eksik bilgi varsa yer-tutucu bırak, dilekçeyi tamamla.
