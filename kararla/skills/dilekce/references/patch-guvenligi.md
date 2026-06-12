# Hedefli Düzenleme (Patch) Güvenliği

Var olan bir dilekçeyi düzenlerken **tüm belgeyi yeniden yazma** — yalnız hedeflenen yerleri
değiştir. Her değişiklik bir patch'tir: `{ op, target, content }`.

## Patch kuralları
- **`target` belgeden BİREBİR alıntı** olmalı (karakter-karakter; boşluk/noktalama dahil).
- **Tek eşleşme zorunlu:**
  - `target` belgede **0 kez** geçiyorsa → bu patch'i **ATLA** (`target_not_found`); uydurma yapma.
  - `target` belgede **birden çok** geçiyorsa → **ATLA** (`target_ambiguous`); daha uzun/benzersiz
    bir `target` seç.
- **`op` türleri:**
  - `replace` → `target`'ı `content` ile değiştir.
  - `insert_after` → `target`'tan **sonra** `content` ekle.
  - `insert_before` → `target`'tan **önce** `content` ekle.

## Atomik güvenlik (en kritik)
- Hiçbir patch tutmazsa (hepsi `target_not_found`/`ambiguous`) **orijinal belgeyi ASLA bozma** —
  olduğu gibi bırak, hangi patch'lerin neden tutmadığını kullanıcıya kısaca bildir.
- Patch üretilemiyorsa belgeyi boşaltma/yeniden yazma; brief'i netleştirmesini iste.

## Kapsam disiplini
- **Tüm dokümanı tek patch'te replace etme** — bu "yeniden yaz" demektir, patch değil.
- **Brief'te belirtilmeyen değişiklik yapma — "bonus" iyileştirme YOK.** Yalnız istenen değişiklik.
- Düzenleme sonrası dilekçenin biçim kuralları (dilekce-yazimi.md) bozulmamalı.

> Bu semantik, sandbox'ta dosya düzenlerken Claude Code'un Edit/MultiEdit aracıyla birebir
> örtüşür (birebir-eşleşen string + benzersizlik + atomiklik) — orada da aynı disiplini uygula.
