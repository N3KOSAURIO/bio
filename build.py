#!/usr/bin/env python3
"""Build index.html: inlina iconos de marca, fija OG/SITE url, escribe la raiz."""
import re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
SITE_URL = "https://n3kosaurio.github.io/bio/"
OG_IMAGE = SITE_URL + "og.png"

def icon(name: str) -> str:
    svg = (ROOT / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    d = re.findall(r'<path[^>]*d="([^"]+)"', svg)
    if not d:
        sys.exit(f"icono {name} sin path")
    paths = "".join(f'<path d="{p}"/>' for p in d)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'

html = (ROOT / "src" / "index.template.html").read_text(encoding="utf-8")

def sub_icon(m: re.Match) -> str:
    return icon(m.group(1))

html = re.sub(r"\[\[ICON:([a-z]+)(?::btn)?\]\]", sub_icon, html)
html = html.replace("[[SITE_URL]]", SITE_URL).replace("[[OG_IMAGE]]", OG_IMAGE)

leftover = re.findall(r"\[\[[A-Z_:a-z]+\]\]", html)
if leftover:
    sys.exit(f"placeholders sin resolver: {leftover}")

(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"index.html {len(html)} bytes · iconos inline OK · {SITE_URL}")
