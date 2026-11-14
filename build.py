"""Genera index.html (la app publicada) a partir de src/app.html.
Uso: python3 build.py
"""
import re
src=open('src/app.html').read()
headparts=[]; body=src
# move title/meta/link/style into <head>
m=re.search(r'</style>\n',src); head=src[:m.end()]; body=src[m.end():]
head=head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
pwa='''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#14201c">
<meta name="description" content="Control de ahorros en efectivo, Binance y banco, con tasas BCV y Binance en vivo.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Mis Ahorros">
<style>:root{padding-top:env(safe-area-inset-top,0px)}body{margin:0}[hidden]{display:none!important}</style>
'''+head+'''</head>
<body>
'''+body+'''<script>if("serviceWorker" in navigator && location.protocol==="https:") navigator.serviceWorker.register("sw.js").catch(()=>{});</script>
</body>
</html>
'''
open('index.html','w').write(pwa)
