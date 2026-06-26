# Kararla — Claude Plugin

Türk hukuku asistanı. Tek kurulumla şunları getirir:

- **kararla skill** — içtihat/mevzuat araştırması, yasal süre & faiz/TÜFE/döviz hesaplama, UYAP `.udf` belgelerini HTML/Word'e dönüştürme ve analiz.
- **Kararla MCP connector** — yukarıdaki yetenekleri sağlayan araçlar (`ictihat_*`, `mevzuat_*`, `faiz_orani`, `request_api_usage`, …).

Plugin'in amacı: kullanıcının connector URL'sini elle girip skill'i ayrıca yüklemesini ortadan kaldırmak — **tek "Install"**.

---

## Kullanıcı için kurulum (claude.ai web · Claude Desktop · Cowork)

1. **Customize** (sol menü) → **Plugins** sekmesi.
2. Bu marketplace'i ekle (GitHub repo): `kararla/kararla-claude-plugin`.
3. **kararla** plugin'inde **Install**.
4. Kararla connector'ını **bir kez yetkilendir** (OAuth login — kendi org'unla bağlanırsın).

Bitti. İçtihat/mevzuat/hesaplama/belge araçları + skill aktif. `.udf` yükleyip "Word olarak ver" ya da "bu dilekçeyi incele" diyebilirsin.

> Kuruluma açık tek manuel adım OAuth yetkilendirmesidir — bu kasıtlı (her kullanıcı kendi hesabına bağlanır), paketlenemez.

---

## Yapı

```
kararla-claude-plugin/
├── .claude-plugin/marketplace.json   # bu repo'yu marketplace yapar (plugin source: "./kararla")
└── kararla/                          # plugin (çok-domain'e hazır: ileride kararla-ceza/… eklenebilir)
    ├── .claude-plugin/plugin.json    # plugin manifest (ad, sürüm)
    ├── .mcp.json                     # Kararla uzak connector beyanı
    ├── CLAUDE.md                     # ortak guardrail kuralları (provenance/injection/degradation)
    └── skills/
        ├── kararla/                  # geniş skill: araştırma + memo + hesap/süre + belge okuma/inceleme
        └── dilekce/                  # dilekçe yazma & düzenleme (write + patch)
```

## Geliştirici / yayıncı için

### 1. MCP connector
`.mcp.json` Kararla uzak MCP endpoint'ini işaret eder: `https://mcp.kararla.com/mcp` (streamable HTTP → `type: "http"`). Endpoint değişirse burada güncelle.

### 2. Yayınla
Repo'yu GitHub'a push et. Kullanıcılar marketplace'i `kararla/kararla-claude-plugin` ile ekler. Güncelleme = repoya push; kullanıcı marketplace'i yeniler.

- Team/Enterprise org sahibi plugin'i organizasyona dağıtabilir (hatta auto-install/required).

### Versiyonlama (otomatik)
Claude güncellemeyi `version` alanından algılar (aynı versiyon → cache'i korur). Bu repo bir
**pre-commit hook** ile her commit'te patch'i otomatik artırır (`plugin.json` + `marketplace.json`
senkron) → elle bump derdi yok.

**Yeni clone'da bir kez:** `git config core.hooksPath .githooks`

- Otomatik: her commit `1.1.0 → 1.1.1 → 1.1.2…`
- Manuel minor/major: `version`'ı elle düzenleyip commit et (örn. `1.2.0`); hook senin değerine
  saygı gösterir, otomatik bump'ı atlar.
- Atlamak için: `git commit --no-verify`.

### 3. Pilot doğrulaması (ŞART)
Yayın öncesi **kendi hesabınla** kur ve doğrula:
- claude.ai web (consumer) **özel/3. taraf GitHub marketplace** eklemeye izin veriyor mu (plan/yüzeye göre değişebilir).
- Plugin'le gelen **uzak OAuth connector** kurulumu otomatik mi, yetkilendirme akışı çalışıyor mu.
- `.udf` → `udf-to-docx` uçtan uca (connector + skill) çalışıyor mu.

### Skill kaynak-tekliği
**Bu plugin repo'su skill'in tek kanonik kaynağıdır.** Ana repodaki eski kopya (`kararla/mcp/skill/`) kaldırıldı (drift riski kapandı). Skill değişiklikleri yalnız burada (`skills/kararla/`) yapılır.
