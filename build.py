"""Builds index.html, the standalone page for web hosting, from src/chacky-studio.html.

Usage: python3 build.py [source] [output]
Defaults to src/chacky-studio.html and index.html next to this script.
"""
import sys, urllib.parse
from pathlib import Path

root = Path(__file__).resolve().parent
src_path = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'src' / 'chacky-studio.html'
out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else root / 'index.html'
src = src_path.read_text()
cut = src.index('</style>') + len('</style>')
head_part, body_part = src[:cut], src[cut:]
head_part = head_part.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
title_end = head_part.index('</title>') + len('</title>')
title, rest = head_part[:title_end], head_part[title_end:]
favicon_svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-0.2 1.3 35.2 35.2">'
  '<path fill="#F2B705" d="M26.25 9.31A13.5 13.5 0 1 0 28.18 31.34L24.64 27.13A8 8 0 1 1 23.5 14.07Z"/>'
  '<path fill="#1d1d1f" d="M0.39 35.86L8.73 30.06L9.09 30.42L10.08 29.43L9.05 28.4L34.35 3.1A0.85 0.85 0 0 0 33.15 1.9L7.85 27.2L6.83 26.17L5.84 27.16L6.19 27.52Z"/>'
  '<g transform="translate(-10.61 10.61)"><path fill="#E09E00" d="M28.02 6.30L28.02 6.86L28.01 7.43L27.99 7.99L27.96 8.56L27.90 9.12L27.81 9.69L27.71 10.25L27.59 10.81L27.46 11.38L27.35 11.94L27.26 12.51L27.20 13.07L27.19 13.64L27.22 14.20L28.07 13.35L28.92 14.20L28.87 13.64L28.87 13.07L28.91 12.51L28.98 11.94L29.07 11.38L29.18 10.81L29.28 10.25L29.37 9.69L29.44 9.12L29.48 8.56L29.50 7.99L29.50 7.43L29.49 6.86L29.48 6.30Z"/>'
  '<path fill="#FFC400" d="M30.00 6.70L30.04 7.40L30.10 8.10L30.18 8.80L30.26 9.50L30.33 10.20L30.37 10.90L30.37 11.60L30.33 12.30L30.25 13.00L30.14 13.70L30.00 14.40L29.88 15.10L29.78 15.80L29.72 16.50L30.70 15.55L31.68 16.50L31.70 15.80L31.78 15.10L31.88 14.40L31.99 13.70L32.08 13.00L32.13 12.30L32.15 11.60L32.12 10.90L32.05 10.20L31.96 9.50L31.85 8.80L31.75 8.10L31.66 7.40L31.60 6.70Z"/>'
  '<rect fill="#FFC400" x="28.59" y="4.96" width="2.4" height="3" rx="0.55" transform="rotate(-45 29.79 6.46)"/></g></svg>')
favicon = 'data:image/svg+xml,' + urllib.parse.quote(favicon_svg)
base = """<style>
:root { color-scheme: light; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { color-scheme: dark; } }
:root[data-theme="dark"] { color-scheme: dark; }
body { margin: 0; }
img, svg, video, canvas { max-width: 100%; }
[hidden] { display: none !important; }
</style>"""
out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{title}
<meta name="description" content="Chacky Studio designs and builds clean, fast websites for small businesses. See the packages, send a request, and agree on a price by email.">
<meta name="theme-color" content="#FFD43B">
<link rel="icon" type="image/svg+xml" href="{favicon}">
{base}{rest}
</head>
<body>{body_part}
</body>
</html>
"""
out_path.write_text(out)
print('Built', out_path)
