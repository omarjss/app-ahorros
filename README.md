# Mis Ahorros

App web para llevar el control de mis ahorros en **efectivo**, **Binance** y **banco**, por día y por mes, con las tasas del día:

- Dólar y euro oficial del BCV (fuente: [ve.dolarapi.com](https://ve.dolarapi.com))
- USDT en Binance P2P, promedio de compra y venta (fuente: [CriptoYa](https://criptoya.com))

Las tasas se actualizan solas cada 10 minutos mientras la app está abierta. Los montos los anoto yo; la app no se conecta a ningún banco ni a Binance.

**Abrir la app:** https://omarjss.github.io/app-ahorros/

## Instalar en el teléfono

- **Android:** abrir el enlace en Chrome → menú ⋮ → «Instalar app» (o «Agregar a pantalla principal»).
- **iPhone:** abrir el enlace en Safari → Compartir → «Agregar a inicio».

## Dónde quedan los datos

En el propio teléfono o navegador (almacenamiento local). No hay servidor ni base de datos. El botón **Respaldo** copia todo como texto para guardarlo o pasarlo a otro equipo, y el botón **Excel** descarga movimientos, resumen por mes, resumen por día y tasas.

## Archivos

| Archivo | Para qué |
|---|---|
| `src/app.html` | Código fuente de la app (HTML, CSS y JavaScript en un solo archivo) |
| `build.py` | Genera `index.html` desde `src/app.html` |
| `index.html` | La app publicada en GitHub Pages |
| `manifest.webmanifest`, `sw.js`, `icon-*` | Lo que permite instalarla y abrirla sin conexión |

Para cambiar algo: editar `src/app.html`, correr `python3 build.py` y hacer commit de ambos archivos.
