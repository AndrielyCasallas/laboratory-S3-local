# Solución de problemas

## Docker no está disponible

Comprueba que Docker Desktop esté abierto en Windows/macOS o que el servicio Docker esté
activo en Linux:

```bash
docker info
docker compose version
```

## El puerto ya está ocupado

Consulta el proceso que usa `4566`, `8080`, `9000` o `9001`. Después detenlo o modifica el
lado izquierdo del mapeo `HOST:CONTENEDOR` en el archivo Compose correspondiente.

## MinIO AIStor no inicia

1. Confirma que exista `MINIO/minio.license`.
2. Revisa los logs con `docker compose logs minio-aistor`.
3. Comprueba que `MINIO/data` tenga permisos de lectura y escritura.
4. No reutilices datos creados por una instalación incompatible sin hacer una copia de seguridad.

## La prueba no puede conectarse

Levanta primero el servicio y comprueba el estado con `docker compose ps`. Verifica también
que la prueba use el endpoint correcto: FLOCI usa `4566` y MinIO AIStor usa `9000`.

## Reinicio limpio del laboratorio

Detén el servicio con `docker compose down`. Para FLOCI, `docker compose down -v` también
elimina el volumen Docker. Para MinIO AIStor, conserva o elimina `MINIO/data` manualmente
según necesites conservar los objetos.
