# Belge / Karar İnceleme (yapılandırılmış)

`belge-okuma.md` belgeyi **okur/dönüştürür**; bu referans okunan belgeyi (sözleşme, mahkeme kararı,
idari işlem, bilirkişi raporu…) **yapılandırılmış** inceler. Önce türü/künyeyi çıkar
([belge-turleri.md](belge-turleri.md)), sonra:

## Özet (hukuki risk) — Bottom line
En başa kısa bir risk özeti:

> **Bottom line:** [N] 🔴 kritik · [N] 🟡 dikkat · [N] 🟢 olağan

En kritik 1-2 maddeyi öne al (kullanıcı önce onları görsün).

## Term-by-term tablo

| Hüküm / Madde | Değer / Özet | Durum | Birebir alıntı (sayfa) |
|---|---|---|---|

- **Birebir alıntı zorunlu:** her hücrenin alıntısı belgeden **karakter-karakter** kopyalanır.
  Bulunamıyorsa `quote_unavailable` yaz + Durum = `inceleme_gerekli`. **Paraphrase'i alıntı diye
  verme; boş hücre bırakma.** (Alıntıyı yazmadan önce belgede gerçekten geçtiğini ikinci kez doğrula.)
- **Durum** sütunu: 🔴 kritik / 🟡 dikkat / 🟢 olağan (ya da `quote_unavailable`).
- **Çapraz kontrol:** bir hüküm kanun/karara dayanıyorsa `mevzuat_madde` / `ictihat_detay` ile
  doğrula (güncel mi, mülga mı, gerçekten o yönde mi) → `[Kararla — doğrulandı]` etiketle
  (bkz. [guardrails.md](guardrails.md)). Bulunmazsa `[model bilgisi — teyit edin]`.

## Bağlayıcı işlem uyarısı
Belge imza/temyiz/feragat/sulh gibi **bağlayıcı** bir işlemse, sonucun sonunda kritik uyarı:
işlemin geri dönüşü olmayabilir; içeriği ve (varsa) süreyi maddeden/dosyadan teyit et. (Kullanıcı
hukukçu — "avukata danış" değil, kendi doğrulamasını vurgula.)

## Gizlilik
Belgeler hassas kişisel veri içerebilir; incelemede kullanıcının istediğine odaklan, gereksiz
kişisel bilgiyi öne çıkarma (SKILL.md "Belge gizliliği").
