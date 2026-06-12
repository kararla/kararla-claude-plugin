#!/usr/bin/env python3
"""
UYAP .udf dönüştürücü (Kararla API) — HTML veya DOCX.

Kullanım:
    python convert_udf.py <udf_dosyasi> <url> <token> [cikti_dosyasi]

<url> ve <token>, `request_api_usage` MCP tool'undan gelir
(operation: "udf-to-html" → HTML, ya da "udf-to-docx" → Word .docx).
token 60 sn geçerli ve tek kullanımlıktır — alır almaz çalıştır.

Çıktı operation-agnostik: URL hangi endpoint olduğunu, YANIT ŞEKLİ ne yazılacağını söyler.
- HTML yanıtı (`html`) → metin .html dosyası; artifact (canvas) yapmak için bu dosyayı oku.
- İkili yanıt (`content_base64`, örn. docx) → base64-decode edilip ikili dosya yazılır
  (uzantı yanıttaki `format`'tan). İkili dosyayı canvas'a KOYMA — kullanıcıya indirilebilir yol bildir.
Özet (yol, boyut, kalite, uyarılar) basılır. Hata → açık Türkçe mesaj + sıfırdan farklı kod.

Yalnız standart kütüphane (sandbox'ta her zaman mevcut); pip kurulumu gerekmez.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request

# HTTP kodu -> ne yapılacağı (SKILL.md / belge-okuma.md hata tablosuyla aynı).
ERROR_HINTS = {
    400: "Geçersiz istek.",
    401: "Token geçersiz/süresi dolmuş/zaten kullanılmış. request_api_usage'ı tekrar çağırıp yeni token al.",
    403: "Bu işlem kullanıcının planına dahil değil. Plan yükseltmesi gerektiğini bildir.",
    409: "Token zaten kullanıldı (tek kullanımlık). Yeni token al.",
    413: "Dosya 10MB sınırını aşıyor. Dosyayı küçült veya böl.",
    422: "Belge işlenemedi (bozuk veya desteklenmeyen .udf).",
    429: "Çok fazla istek (hız limiti). Kısa süre bekleyip tekrar dene.",
    503: "Doğrulama servisi geçici olarak kullanılamıyor. Tekrar dene.",
}


def _default_out_path(udf_path: str, ext: str) -> str:
    """Çıktıyı YAZILABİLİR bir dizine koy. Girdinin dizinini KULLANMA — yüklenen dosyalar
    genelde salt-okunur (örn. /mnt/user-data/uploads) ve oraya yazmak OSError [Errno 5] verir.
    Sırayla dener: claude.ai çıktı dizini -> çalışma dizini -> /tmp. Yalnız basename kullanılır.
    Uzantı (`ext`) yanıt formatından gelir: html ya da docx."""
    name = os.path.splitext(os.path.basename(udf_path))[0] + f".{ext}"
    for d in ("/mnt/user-data/outputs", os.getcwd(), "/tmp"):
        if os.path.isdir(d) and os.access(d, os.W_OK):
            return os.path.join(d, name)
    return name


def main() -> None:
    if len(sys.argv) not in (4, 5):
        sys.exit("Kullanım: python convert_udf.py <udf_dosyasi> <url> <token> [cikti_html]")

    udf_path, url, token = sys.argv[1], sys.argv[2], sys.argv[3]
    # 4. argüman verilirse onu kullan; yoksa çıktı YAZILABİLİR dizine yazılır (uploads/
    # salt-okunur). Uzantı yanıt formatına göre seçilir (html/docx) → response parse sonrası.
    explicit_out = sys.argv[4] if len(sys.argv) == 5 else None

    try:
        with open(udf_path, "rb") as f:
            body = f.read()
    except OSError as e:
        sys.exit(f"Dosya okunamadı: {e}")

    req = urllib.request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/octet-stream",
            # Cloudflare bot-koruması default "Python-urllib" UA'sını 1010 ile blokluyor.
            # Kendi adımızla geçiyoruz (curl/tarayıcı zaten geçiyor; yalnız urllib bloklanıyordu).
            "User-Agent": "kararla-skill/1.0",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.load(resp)
    except urllib.error.HTTPError as e:
        hint = ERROR_HINTS.get(e.code, "")
        # Gövdeyi BİR kez oku: JSON ise bizim {"error": ...}, değilse ham (CF/proxy) hatası.
        # JSON değilken ham gövdeyi göster ki edge hatası "plan reddi" sanılmasın.
        try:
            raw = e.read().decode(errors="replace")
        except Exception:
            raw = ""
        try:
            detail = json.loads(raw).get("error", "")
        except Exception:
            detail = raw[:200].strip()
        sys.exit(f"HATA {e.code}: {hint} {detail}".strip())
    except urllib.error.URLError as e:
        sys.exit(f"Bağlantı hatası: {e.reason}")

    # Çıktı operation-agnostik: ikili yanıt (content_base64, örn. docx) → ikili dosya;
    # değilse HTML passthrough → metin dosyası. İçerik dosyada kalır (bağlamı şişirmemek için
    # stdout'a basılmaz); özet (yol, boyut, kalite, uyarı) stdout'a.
    content_b64 = payload.get("content_base64")
    if content_b64:
        blob = base64.b64decode(content_b64)
        ext = payload.get("format", "bin")
        out_path = explicit_out or _default_out_path(udf_path, ext)
        with open(out_path, "wb") as f:
            f.write(blob)
        print(f"Dosya yazıldı: {out_path} ({len(blob)} bayt, {ext})")
    else:
        html = payload.get("html", "")
        out_path = explicit_out or _default_out_path(udf_path, "html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"HTML yazıldı: {out_path} ({len(html)} karakter)")

    quality = payload.get("quality", "")
    warnings = payload.get("warnings") or []
    if quality:
        print(f"Kalite: {quality}")
    for w in warnings:
        print(f"Uyarı: {w}")


if __name__ == "__main__":
    main()
