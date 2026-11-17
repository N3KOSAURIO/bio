# ney.bio — bio link de Sneyder Arroyave

Una sola página, un solo archivo: HTML + CSS + SVG inlineados, sin dependencias
de JS ni iconos remotos. Solo las fuentes vienen de Google Fonts.

## Qué enlaza

| Bloque | Destino |
|---|---|
| MØRK Studios | https://www.mork.click/ |
| Ney Agency | https://kumo.mork.click/ |
| Instagram | https://www.instagram.com/sneyder_skr/ |
| TikTok | https://www.tiktok.com/@neycreator404 |
| Facebook | https://www.facebook.com/sneyder.arroyave.5 |
| WhatsApp | wa.me con mensaje precargado |

## Estructura

```
src/index.template.html   plantilla con [[ICON:x]], [[SITE_URL]], [[OG_IMAGE]]
src/og.template.html      tarjeta OG 1200x630 (se rasteriza a og.png)
icons/*.svg               simpleicons en blanco, se inlinean en el build
assets/mork-card.webp     arte de MØRK recortado 760x950
build.py                  resuelve placeholders -> index.html
```

## Build

```bash
python3 build.py            # escribe index.html en la raíz
```

`build.py` falla con exit != 0 si queda algún `[[PLACEHOLDER]]` sin resolver.

La tarjeta OG se genera abriendo `src/og.template.html` en un navegador a
1200x630 y capturando a PNG (`og.png`). Si cambia el arte, hay que regenerarla.

## Cambiar un enlace

Se edita `src/index.template.html` y se vuelve a correr `python3 build.py`.
No editar `index.html` a mano: se sobreescribe.

## Publicación

GitHub Pages, rama `main`, raíz del repo.

**Dominio vivo: <https://sneyder.biolnk.si>** (desde 2026-11-16). El archivo `CNAME` de la
raíz fija el dominio (`sneyder.biolnk.si`); GitHub emite y renueva el certificado Let's Encrypt
y fuerza HTTPS (`https_enforced`). El `SITE_URL` de `build.py` debe coincidir con ese dominio —
de ahí salen `canonical`, `og:url` y `og:image`.

`https://n3kosaurio.github.io/bio/` ahora responde 301 hacia el dominio propio.

DNS: zona en Hostinger (`lunar`/`solar.dns-parking.com`), registro `sneyder` CNAME →
`n3kosaurio.github.io`. El apex `biolnk.si` queda **libre** (reservado para el producto de
bio-links); no se toca ni el apex ni los MX de Hostinger.
