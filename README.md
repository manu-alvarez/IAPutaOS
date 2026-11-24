# IAPuta OS — React + FastAPI

Aplicación web con frontend React/Vite y backend FastAPI. El repositorio incluye ahora un entorno local reproducible con Docker Compose; **no implica un despliegue en producción**.

## Inicio local

Requisitos: Docker con Compose y credenciales de los proveedores que se vayan a utilizar.

```bash
git clone https://github.com/manu-alvarez/IAPutaOS.git
cd IAPutaOS
cp .env.example .env
# Rellenar GROQ_API_KEY e IAPUTA_API_KEY con valores privados y únicos.
docker compose up --build -d
docker compose ps
```

- Interfaz local: http://127.0.0.1:8080
- Salud del backend: http://127.0.0.1:8080/health
- El backend no publica su puerto en el anfitrión; solo se alcanza desde el proxy Nginx de la red privada del proyecto.
- La interfaz se enlaza exclusivamente a `127.0.0.1`; el acceso remoto debe configurarse aparte mediante un proxy HTTPS con autenticación.

## Seguridad

- Las claves de servicios se configuran en `.env` y no se incluyen en el bundle JavaScript.
- Nginx incorpora `X-API-Key` a las peticiones al backend desde el contenedor, no desde el navegador.
- El backend rechaza todas las operaciones protegidas si `IAPUTA_API_KEY` no está configurada.
- Las credenciales utilizadas anteriormente en archivos frontend versionados pueden seguir presentes en el historial Git. Retirar el valor del árbol actual **no invalida** una credencial ya expuesta.
- El proxy Nginx no aporta autenticación de usuario final: **no publicar su puerto directamente en Internet**. Para uso remoto, colocar un control de acceso perimetral antes del proxy.

## Pruebas

```bash
python -m pytest tests/ -q
cd frontend && npm ci && npm run build
docker compose config -q
```

La CI ejecuta las comprobaciones que no requieren conexiones reales a proveedores. Las funciones Groq, visión, audio y automatizaciones externas requieren pruebas de aceptación adicionales con credenciales propias.

## Estado

Los endpoints básicos, la interfaz y el empaquetado están implementados en este repositorio. Los servicios externos y el acceso remoto de producción **no se consideran verificados** por una compilación correcta.

### Persistent memory

The local Compose topology uses the `iaputa-memory` named volume at `/app/data`. Before replacing an existing deployment, follow [the verified backup and migration procedure](docs/MEMORY-PERSISTENCE.md). Do not publish the local frontend proxy without perimeter authentication. Existing PM2 installations are not automatically migrated by this Compose configuration.
