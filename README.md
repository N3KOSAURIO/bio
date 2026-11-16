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
`https://n3kosaurio.github.io/bio/` — pendiente mover a dominio propio.
