#!/usr/bin/env python3
"""Build index.html: inlina iconos de marca, resuelve [[URL:clave]] desde links.json,
fija OG/SITE url y escribe la raiz."""
import json, re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
SITE_URL = "https://sneyder.biolnk.si/"
OG_IMAGE = SITE_URL + "og.png"


def icon(name: str) -> str:
    svg = (ROOT / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    d = re.findall(r'<path[^>]*d="([^"]+)"', svg)
    if not d:
        sys.exit(f"icono {name} sin path")
    paths = "".join(f'<path d="{p}"/>' for p in d)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'


links = json.loads((ROOT / "links.json").read_text(encoding="utf-8"))
urls = {x["id"]: x["url"] for k in ("cards", "accesos", "redes") for x in links.get(k, [])}
if links.get("whatsapp"):
    urls["whatsapp"] = links["whatsapp"]

html = (ROOT / "src" / "index.template.html").read_text(encoding="utf-8")
html = re.sub(r"\[\[ICON:([a-z]+)(?::btn)?\]\]", lambda m: icon(m.group(1)), html)
html = re.sub(r"\[\[URL:([a-z0-9-]+)\]\]", lambda m: urls.get(m.group(1)) or sys.exit(f"url {m.group(1)} sin definir"), html)
html = html.replace("[[SITE_URL]]", SITE_URL).replace("[[OG_IMAGE]]", OG_IMAGE)

leftover = re.findall(r"\[\[[A-Z_:a-z-]+\]\]", html)
if leftover:
    sys.exit(f"placeholders sin resolver: {leftover}")

(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"index.html {len(html)} bytes · {len(urls)} enlaces · iconos inline OK · {SITE_URL}")
