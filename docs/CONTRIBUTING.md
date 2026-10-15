# Cómo aportar capturas y documentación

## Capturas de las webs

Guarda las imágenes en la carpeta del servicio correspondiente:

- `docs/assets/screenshots/floci/`
- `docs/assets/screenshots/minio/`

Usa nombres descriptivos, por ejemplo `consola-inicio.png` o `bucket-creado.webp`.
Evita incluir contraseñas, tokens, licencias, datos personales o información de terceros.
Incluye debajo de cada imagen una breve descripción del flujo mostrado.

## Documentación adicional

Usa `docs/reference/` para:

- diagramas de arquitectura;
- referencias de la API;
- decisiones técnicas;
- enlaces a recursos externos;
- manuales específicos del equipo.

Cada documento debe indicar su propósito, requisitos y fecha de actualización.

## Plantilla para una captura

```markdown
### Título del flujo

![Descripción breve](./nombre-de-la-imagen.png)

Qué demuestra esta captura y qué resultado se espera.
```

## Plantilla para una guía

```markdown
# Título

## Objetivo

## Requisitos

## Procedimiento

## Verificación

## Problemas conocidos
```
