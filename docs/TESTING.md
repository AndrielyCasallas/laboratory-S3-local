# Pruebas de integración

Las pruebas crean un bucket, suben un archivo y listan sus objetos mediante `boto3`.
Cada prueba apunta a un servicio diferente:

| Prueba | Proyecto | Endpoint |
|---|---|---|
| FLOCI | `tests/floci` | `http://localhost:4566` |
| MinIO AIStor | `tests/minio` | `http://localhost:9000` |

## Opción recomendada: uv

Instala [uv](https://docs.astral.sh/uv/getting-started/installation/) y ejecuta desde la
raíz del repositorio:

```text
Windows PowerShell:  cd tests/floci; uv run main.py
Linux/macOS:        cd tests/floci && uv run main.py
```

Para MinIO AIStor:

```text
Windows PowerShell:  cd tests/minio; uv run main.py
Linux/macOS:        cd tests/minio && uv run main.py
```

`uv` creará el entorno virtual local automáticamente. Asegúrate de levantar el servicio
correspondiente antes de ejecutar la prueba.

## Opción con Python y pip

```text
Windows PowerShell:  cd tests/floci; py -3.12 -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install -e .
Linux/macOS:        cd tests/floci && python3.12 -m venv .venv && . .venv/bin/activate && python -m pip install -e .
```

Luego ejecuta:

```bash
python main.py
```

Repite los comandos sustituyendo `tests/floci` por `tests/minio` para probar MinIO AIStor.
