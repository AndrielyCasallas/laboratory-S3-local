# Instalación y ejecución

## 1. Requisitos

### Todos los sistemas

- Docker actualizado con Docker Compose v2 (`docker compose version`).
- Git, si se clona el repositorio.
- Python 3.12 para las pruebas.
- Para MinIO AIStor: una licencia válida guardada como `MINIO/minio.license`.
- En Windows y macOS, Docker Desktop debe estar iniciado y permitir el acceso a la carpeta
  del repositorio desde **Settings > Resources > File sharing** si lo solicita.

### Windows

Instala [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) y
activa el backend WSL 2 recomendado. Usa PowerShell desde la carpeta del repositorio.

### macOS

Instala [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/). Tanto
Apple Silicon como Intel son compatibles con Docker Desktop; abre Docker Desktop antes de
ejecutar los comandos.

### Linux

Instala [Docker Engine y Compose](https://docs.docker.com/engine/install/) para tu distribución.
Si el usuario no puede ejecutar Docker sin `sudo`, añade el usuario al grupo `docker` y vuelve
a iniciar sesión. Verifica la instalación con:

```bash
docker run --rm hello-world
```

## 2. Descargar el proyecto

En PowerShell (Windows):

```powershell
git clone <URL_DEL_REPOSITORIO>
Set-Location floci_docs
```

En Linux o macOS:

```bash
git clone <URL_DEL_REPOSITORIO>
cd floci_docs
```

## 3. Ejecutar FLOCI

FLOCI no requiere licencia adicional:

```text
Windows PowerShell:  Set-Location FLOCI; docker compose up -d
Linux/macOS:        cd FLOCI && docker compose up -d
```

Endpoints:

| Servicio | URL |
|---|---|
| API S3 compatible | http://localhost:4566 |
| Interfaz web | http://localhost:8080 |

Ver estado y logs:

```text
Windows PowerShell:  docker compose ps; docker compose logs -f
Linux/macOS:        docker compose ps && docker compose logs -f
```

Detener FLOCI:

```text
Windows PowerShell:  docker compose down
Linux/macOS:        docker compose down
```

## 4. Ejecutar MinIO AIStor

Antes de iniciar MinIO, consulta la [página oficial de descargas](https://www.min.io/download)
para obtener AIStor y una licencia válida. La guía de referencia para este despliegue es la
[instalación oficial de AIStor en contenedor](https://docs.min.io/aistor/installation/container/install/).
Desde la raíz del repositorio, crea las carpetas de datos y certificados y coloca la licencia
descargada en `MINIO/minio.license`. No la publiques ni la incluyas en commits.

```text
Windows PowerShell:  New-Item -ItemType Directory -Force MINIO\data, MINIO\certs
Linux/macOS:        mkdir -p MINIO/data MINIO/certs
```

La carpeta `MINIO/data` es un volumen local compartido con el contenedor: los objetos
persisten aunque se recree el contenedor. La carpeta `MINIO/certs` queda preparada para
TLS, pero no es necesaria para este laboratorio HTTP local.

```text
Windows PowerShell:  Set-Location MINIO; docker compose up -d
Linux/macOS:        cd MINIO && docker compose up -d
```

Accede a la consola con:

- URL: `http://localhost:9001`
- Usuario local: `admin`
- Contraseña local: `password123`

La API S3 está disponible en `http://localhost:9000`.

Las capturas de esta ejecución se encuentran en
[`docs/assets/screenshots/minio/`](assets/screenshots/minio/).

> Cambia las credenciales antes de usar este entorno fuera de un laboratorio local. Para
> detenerlo, ejecuta `docker compose down` desde `MINIO`.

## 5. Ejecutar ambos servicios

Puedes levantar FLOCI y MinIO AIStor al mismo tiempo porque usan puertos distintos. Si un puerto
ya está ocupado, detén el proceso que lo utiliza o cambia el mapeo en el Compose correspondiente.

## 6. Volúmenes y persistencia

- FLOCI usa el volumen Docker `floci_data`.
- MinIO AIStor guarda datos en `MINIO/data`.
- `MINIO/data`, certificados y licencias son datos locales; no deben versionarse.

Para eliminar los datos de FLOCI:

```bash
cd FLOCI
docker compose down -v
```

Para eliminar los datos de MinIO AIStor, primero detén el servicio y borra únicamente
`MINIO/data` desde el explorador de archivos o con el comando equivalente de tu sistema.
