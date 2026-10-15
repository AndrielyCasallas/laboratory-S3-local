<div align="center">
  <img src="docs/assets/logo_aws_sbg.jpeg" alt="Logo MinIO AIStor" width="180" height="180" style="border-radius: 50%; object-fit: cover; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 3px solid #ff5722;" />

  # Laboratorio S3 local

  Guías para ejecutar **FLOCI** y **MinIO AIStor** localmente con Docker.



  [![Docker](https://img.shields.io/badge/Docker-24.0+-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
  [![MinIO AIStor](https://img.shields.io/badge/MinIO-AIStor-C72C48?style=flat-square&logo=minio&logoColor=white)](https://min.io/)
  [![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-Enterprise%20Free%20Tier-green?style=flat-square)](#licenciamiento)
</div>

---

## ¿Qué incluye este repositorio?

- **FLOCI**: API S3 local en `http://localhost:4566` y una interfaz web en `http://localhost:8080`.
- **MinIO AIStor**: API S3 en `http://localhost:9000` y consola en `http://localhost:9001`.
- **Pruebas de integración** en Python 3.12 con `boto3`.
- Espacios preparados para capturas de las interfaces y documentación complementaria.

## Requisitos rápidos

1. Docker Desktop (Windows o macOS) o Docker Engine + Compose (Linux).
2. Python 3.12 para ejecutar las pruebas.
3. Una licencia válida de MinIO AIStor en `MINIO/minio.license` si se va a levantar MinIO AIStor.

> Los comandos de esta guía se ejecutan desde la carpeta raíz `floci_docs`.

## Documentación

- [Instalación y ejecución en Windows, Linux y macOS](docs/SETUP.md)
- [Pruebas de integración](docs/TESTING.md)
- [Solución de problemas](docs/TROUBLESHOOTING.md)
- [Capturas saneadas de MinIO AIStor](docs/assets/screenshots/minio/README.md)

## Referencias oficiales de MinIO

El punto de partida para descargar MinIO AIStor, el cliente y obtener la licencia es
la página oficial de [descargas de MinIO](https://www.min.io/download). La guía oficial
para ejecutar AIStor en un contenedor está disponible en la
[documentación de instalación con Docker](https://docs.min.io/aistor/installation/container/install/).

En este repositorio, las capturas de la consola y de las operaciones S3 están guardadas
en [`docs/assets/screenshots/minio/`](docs/assets/screenshots/minio/). La licencia y los
datos locales de MinIO no deben publicarse ni incluirse en commits.

### Capturas de MinIO AIStor

| Descarga de AIStor | Solicitud de licencia |
|---|---|
| ![Descarga de MinIO AIStor](docs/assets/screenshots/minio/01-aistor-download.png) | ![Solicitud de licencia AIStor](docs/assets/screenshots/minio/02-license-request.png) |

| Confirmación de licencia | Correo de licencia |
|---|---|
| ![Confirmación de licencia AIStor](docs/assets/screenshots/minio/03-license-confirmation.png) | ![Correo de licencia AIStor](docs/assets/screenshots/minio/04-license-email.png) |

| Clave de licencia | Archivo local de licencia |
|---|---|
| ![Clave de licencia AIStor](docs/assets/screenshots/minio/05-license-key.png) | ![Archivo local de licencia](docs/assets/screenshots/minio/06-license-file.png) |

| Carpeta local de MinIO |
|---|
| ![Carpeta local de MinIO](docs/assets/screenshots/minio/07-minio-folder.png) |

## Inicio rápido

```bash
cd FLOCI
docker compose up -d
```

Comprueba FLOCI en `http://localhost:4566` y su interfaz web en `http://localhost:8080`.
Para detenerlo:

```bash
docker compose down
```

## Licencia y secretos

No se deben subir credenciales reales, archivos `.license`, datos de MinIO ni carpetas `.venv`.
Las credenciales mostradas en los ejemplos son únicamente las credenciales locales definidas
por los archivos Compose.
