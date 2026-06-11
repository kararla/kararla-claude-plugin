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
├── .claude-plugin/
│   ├── plugin.json        # plugin manifest (ad, sürüm)
│   └── marketplace.json   # bu repo'yu marketplace yapar (plugin source: "./")
├── .mcp.json              # Kararla uzak connector beyanı
└── skills/
    └── kararla/           # skill (SKILL.md + references + scripts)
```

## Geliştirici / yayıncı için

### 1. MCP connector
`.mcp.json` Kararla uzak MCP endpoint'ini işaret eder: `https://mcp.kararla.com/mcp` (streamable HTTP → `type: "http"`). Endpoint değişirse burada güncelle.

### 2. Yayınla
Repo'yu GitHub'a push et. Kullanıcılar marketplace'i `kararla/kararla-claude-plugin` ile ekler. Güncelleme = repoya push; kullanıcı marketplace'i yeniler.

- Team/Enterprise org sahibi plugin'i organizasyona dağıtabilir (hatta auto-install/required).

### 3. Pilot doğrulaması (ŞART)
Yayın öncesi **kendi hesabınla** kur ve doğrula:
- claude.ai web (consumer) **özel/3. taraf GitHub marketplace** eklemeye izin veriyor mu (plan/yüzeye göre değişebilir).
- Plugin'le gelen **uzak OAuth connector** kurulumu otomatik mi, yetkilendirme akışı çalışıyor mu.
- `.udf` → `udf-to-docx` uçtan uca (connector + skill) çalışıyor mu.

### Skill kaynak-tekliği
Skill'in çalışılan kopyası ana repoda da var (`kararla/mcp/skill/kararla/`). Drift'i önlemek için **bu plugin repo'sunu kanonik** kabul edip ana repodaki kopyayı kaldırmak ya da bir senkron adımı eklemek gerekir — aksi halde iki kopya zamanla ayrışır.
