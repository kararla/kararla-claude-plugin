#!/usr/bin/env python3
"""
Dilekçe skill — yapısal invariant lint'i.

Model kalitesi test edilemez ama DAVRANIŞ kilitlenir: referans metinlerinde kritik
demir-ibarelerin VARLIĞINI (iskelet madde no'ları, yasak ibare uyarıları, patch kuralları)
doğrular. Bir invariant kaybolursa (ör. "Arz ederim YASAK" silinirse) test kırılır.

Çalıştır:  python test_skill_invariants.py     (skill kök/ scripts'ten)
Yalnız standart kütüphane.
"""
import os
import sys

REF = os.path.join(os.path.dirname(__file__), "..", "references")

# dosya -> içinde MUTLAKA geçmesi gereken ibareler
REQUIRED = {
    "dilekce-turleri.md": [
        "HMK m. 119", "HMK m. 129", "HMK m. 342",   # iskelet demirleri
        "NOTER TALEBİ",                               # ihtarname bloğu
        "3 satırlı",                                  # istinaf başlığı
        "Genel Dilekçe",                              # bilinmeyen tür fallback
        "D. KONUSU TEK CÜMLE",
    ],
    "dilekce-yazimi.md": [
        "label KULLANMA",        # vakıa-sonuç zinciri etiket yasağı
        "Arz ederim",            # "Arz ederim YASAK" kuralı
        "Link UYDURMA",          # link uydurma yasağı
        "[AD SOYAD]",            # yer-tutucu (PII uydurma engeli)
        "MAHKEMESİNE",           # kesme işareti yok kuralı
        "feshetmek",             # dil hataları listesi
    ],
    "patch-guvenligi.md": [
        "BİREBİR alıntı",        # target birebir
        "target_not_found", "target_ambiguous",
        "ASLA bozma",            # atomiklik
        "bonus",                 # bonus iyileştirme yok
    ],
}


def main() -> None:
    failures = []
    for fname, phrases in REQUIRED.items():
        path = os.path.join(REF, fname)
        if not os.path.isfile(path):
            failures.append(f"{fname}: dosya yok")
            continue
        text = open(path, encoding="utf-8").read()
        for p in phrases:
            if p not in text:
                failures.append(f"{fname}: eksik ibare → {p!r}")

    if failures:
        print("FAIL — kayıp invariant(lar):")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    total = sum(len(v) for v in REQUIRED.values())
    print(f"OK — {total} invariant {len(REQUIRED)} dosyada doğrulandı.")


if __name__ == "__main__":
    main()
