# pkg_renamer.py

Este script permite renombrar todos los archivos `.pkg` dentro de una carpeta y sus subcarpetas, usando el nombre del directorio donde se encuentran. Si hay más de un archivo `.pkg` en el mismo directorio, se agrega una numeración para evitar conflictos.

## Uso

```sh
python pkg_renamer.py <ruta_base> [--sobrescribir]
```

- `<ruta_base>`: Ruta base donde buscar los archivos `.pkg`.
- `--sobrescribir`: (opcional) Si se indica, los archivos originales serán sobrescritos. Si no, se crea una copia con el nuevo nombre.
- `--ayuda` o `--help`: Muestra el mensaje de ayuda.

## Ejemplos

```sh
python pkg_renamer.py "C:\mi\carpeta"
python pkg_renamer.py "C:\mi\carpeta" --sobrescribir
```

## Notas
- Solo se procesan archivos con extensión `.pkg`.
- Los módulos `os`, `argparse` y `shutil` son parte de la biblioteca estándar de Python.
