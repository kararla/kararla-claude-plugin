---
name: dilekce
description: >-
  Türk hukukunda dilekçe ve hukuki doküman yazma & düzenleme asistanı. Sıfırdan dilekçe
  yazar (dava, cevap, istinaf, ihtarname, genel dilekçe) veya var olan bir dilekçeyi
  hedefli olarak düzenler. Türk dilekçe anatomisini (HMK-dayanaklı bölüm sırası), biçim
  kurallarını (başlık, taraflar, sonuç-istem) ve atıf disiplinini uygular. Şu durumlarda
  devreye girer: "dilekçe yaz", "dava dilekçesi", "cevap dilekçesi", "istinaf/temyiz dilekçesi",
  "ihtarname hazırla", "şu dilekçeyi düzenle/revize et", "talep sonucunu değiştir" gibi
  dilekçe yazma/düzenleme istekleri. Araştırma/okuma için kararla skill'i kullanılır.
license: Proprietary
metadata:
  author: Kararla
  version: "1.0"
  domain: Turkish law
---

# Dilekçe Yazımı

Türk hukukuna uygun dilekçe ve hukuki doküman üretir/düzenler. İki mod:

- **Yaz (write)** — sıfırdan dilekçe; tür seç → iskelet → biçim kuralları → HTML çıktı (artifact).
- **Düzenle (patch)** — var olan dilekçede **hedefli** değişiklik (tüm belgeyi yeniden yazmadan).

> Kullanıcı onaylı bir hukukçudur; çıktı **taslaktır**, vekilin denetiminden geçer. "Bir avukata danışın" eklenmez.

## Akış — Yaz

1. **Brief'i topla (5 zorunlu alan).** Eksikse sor ya da yer-tutucu bırak:
   - Taraflar (ad/sıfat/vekil), Mahkeme/merci, Vakıalar & strateji, Talepler, Özel talimat.
   - Bilgi verilmediyse `[AD SOYAD]`, `[ADRES]`, `[T.C. KİMLİK NO]`, `[TARİH]` yer-tutucu — **uydurma yok**.
2. **Türü belirle ve iskeleti al** → [references/dilekce-turleri.md](references/dilekce-turleri.md).
   Bilinmeyen tür → `genel_dilekce` iskeleti (sessiz başarısızlık değil).
3. **Biçim & üslup kurallarını uygula** → [references/dilekce-yazimi.md](references/dilekce-yazimi.md).
4. **Atıfları doğrula:** metne yazılacak her madde/karar `kararla` skill'inin MCP araçlarıyla
   (`mevzuat_madde`, `ictihat_detay`) doğrulanır; link yalnız aracın verdiği "Link:" satırından.
   Doğrulanan kaynak `[Kararla — doğrulandı]` etiketli (bkz. kararla/guardrails.md).
5. **HTML artifact** olarak ver (kapalı tag whitelist; bkz. dilekce-yazimi.md "HTML Formatı").

## Akış — Düzenle

Var olan dilekçeyi **birebir** koruyarak yalnız hedeflenen yerleri değiştir →
[references/patch-guvenligi.md](references/patch-guvenligi.md). Tüm belgeyi yeniden yazma;
brief'te belirtilmeyen "bonus" iyileştirme yapma.

## Kaynak disiplini

Yalnız brief'teki ve **onaylanan** araştırma kaynakları metne girer. Onaylanmayan arama
sonucunu dilekçeye dâhil etme. Atıf/uydurma kuralları kararla guardrails ile aynıdır.
