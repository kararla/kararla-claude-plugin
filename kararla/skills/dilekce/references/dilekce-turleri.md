# Dilekçe Türleri — HMK-dayanaklı iskeletler

Bölüm sıralarını ve format kurallarını AYNEN takip et. Başlığa ilgili HMK maddesi yazılır.
**Bilinmeyen tür → "Genel Dilekçe" iskeleti** (sessiz başarısızlık değil).

## Dava Dilekçesi (HMK m. 119)

1. **TARİH**: Sağa hizalı, başlığın üstünde (ör: 12/03/2026).
2. **BAŞLIK**: Mahkeme adı — büyük harf, ortalı (`<h1 style="text-align: center">`).
   - Acil istem varsa başlığın altına büyük harf + parantez: `(İHTİYATİ TEDBİR TALEBİMİZ VARDIR)`.
3. **TARAFLAR + KONU**: Aynı tablo. DAVACI, VEKİLİ, DAVALI satırları + **D. KONUSU** satırı.
   Konu AYRI başlık (h2) YAPILMAZ — tablo satırı.
   **D. KONUSU TEK CÜMLE.** Örn: "Belirsiz alacak davasıdır. (Harca esas değer: 50.000 TL)" /
   "Kira bedelinin ödenmemesi nedeniyle tahliye talebidir." 3-4 satırlık açıklama/strateji YAZMA.
4. **AÇIKLAMALAR**: Numaralı paragraflar (1-, 2-, 3-) ile kronolojik vakıa anlatımı; her vakıayı
   delili ve hukuki sonucuyla doğal akışta bağla (vakıa-delil-hukuki sonuç zinciri, **label'sız**).
5. **DELİLLER**: Numaralı liste. Açıklamalarda bağ kurulmuşsa sadece listele; elde olanlar "(Ektedir)".
6. **HUKUKİ DAYANAKLAR**: Kısa ve öz, **tek satır** — "HMK, TBK m. 315 ve ilgili mevzuat" formatı.
7. **SONUÇ VE İSTEM**: "Yukarıda açıklanan nedenlerle," ile başla; önce usuli, sonra esasa dair
   talepler (numaralı). "...vekâleten talep ederim." ile bitir. Gerekçe YAZMA.
8. **İMZA**: Sağa hizalı — "Saygılarımla,\nDavacı Vekili\nAv. [AD SOYAD]".
9. **EKLER**: Numaralı (Ek-1, Ek-2…).

## Cevap Dilekçesi (HMK m. 129)

Dava dilekçesi yapısıyla aynı, şu farklarla:
- Taraf sıfatları: **DAVALI** (cevap veren), VEKİLİ, **DAVACI** (karşı taraf).
- KONU: "Davaya cevaplarımızdır".
- AÇIKLAMALAR: Dava dilekçesindeki iddialara **sırasıyla** cevap; her iddia ayrı paragraf.
- SONUÇ: "...davanın reddine karar verilmesini vekâleten talep ederim."

## İstinaf Dilekçesi (HMK m. 342)

1. **BAŞLIK**: **3 satırlı** — BAM ilgili daire başkanlığına / "Gönderilmek Üzere" / İlk derece
   mahkemesine. Her satır ayrı `<h1>`.
2. **TARAFLAR**: Tablo — İSTİNAF EDEN (DAVACI/DAVALI), VEKİLİ, KARŞI TARAF + Dosya No.
3. **KONU**: İstinaf başvurusunun konusu + **tebliğ tarihi**.
4. **KARAR ÖZETİ**: İlk derece kararının kısa özeti.
5. **İSTİNAF SEBEPLERİ**: Numaralı paragraflar; her sebep ayrı başlık (hukuka aykırılık, maddi hata…).
6. **SONUÇ VE İSTEM**: "...kararın kaldırılmasına/bozulmasına karar verilmesini vekâleten talep ederim."
7. **İMZA + EKLER**.

## İhtarname

1. **BAŞLIK**: "İHTARNAME" — ortalı, büyük harf.
2. **İHTAR EDEN / MUHATAP**: Tablo — isim, adres.
3. **KONU**: İhtarın konusu — tek paragraf.
4. **AÇIKLAMALAR**: Numaralı paragraflarla vakıa + hukuki dayanak.
5. **İHTAR**: "...aksi halde yasal yollara başvurulacağını ihtar ederim."
6. **NOTER TALEBİ**: "Sayın noter, işbu ihtarnamenin bir suretinin muhataba tebliğini, bir
   suretinin dairenizde saklanmasını, bir suretinin tarafıma verilmesini talep ederim."
7. **İMZA**.

## Genel Dilekçe (fallback)

1. **BAŞLIK**: Hitap edilen kurum/mahkeme adı — ortalı, büyük harf.
2. **BAŞVURAN BİLGİLERİ**: Tablo — ad soyad, TC, adres.
3. **KONU**: Tek paragraf.
4. **AÇIKLAMALAR**: Paragraflarla açıklama.
5. **TALEP**: Açık ve net.
6. **İMZA**: Sağa hizalı.
