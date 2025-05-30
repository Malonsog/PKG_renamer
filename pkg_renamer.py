"""
Uso:
    python pkg_renamer.py <ruta_base> [--sobrescribir]

Argumentos:
    ruta_base        Ruta base donde buscar los archivos .pkg
    --sobrescribir   Si se indica, los archivos originales serán sobrescritos. Si no, se crea una copia con el nuevo nombre.

Ejemplos:
    python pkg_renamer.py "C:\\mi\\carpeta"
    python pkg_renamer.py "C:\\mi\\carpeta" --sobrescribir
"""

import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="Renombra archivos .pkg usando el nombre del directorio.")
parser.add_argument("ruta_base", help="Ruta base donde buscar los archivos .pkg")
parser.add_argument("--sobrescribir", action="store_true", help="Si se indica, los archivos originales serán sobrescritos. Si no, se crea una copia con el nuevo nombre.")
parser.add_argument('--ayuda', action='help', help='Muestra este mensaje de ayuda y termina.')
args = parser.parse_args()

directorio_base = args.ruta_base

resultados = []
errores = []

for root, dirs, files in os.walk(directorio_base):
    pkg_files = [f for f in files if f.lower().endswith('.pkg')]
    if not pkg_files:
        continue
    dir_name = os.path.basename(root)
    for idx, pkg_file in enumerate(pkg_files, start=1):
        ext = '.pkg'
        if idx == 1:
            new_name = f"{dir_name}{ext}"
        else:
            new_name = f"{dir_name}_{idx}{ext}"
        old_path = os.path.join(root, pkg_file)
        new_path = os.path.join(root, new_name)
        count = idx
        while os.path.exists(new_path):
            count += 1
            new_name = f"{dir_name}_{count}{ext}"
            new_path = os.path.join(root, new_name)
        try:
            if args.sobrescribir:
                os.rename(old_path, new_path)
                resultados.append(f"Renombrado: {old_path} -> {new_path}")
            else:
                shutil.copy2(old_path, new_path)
                resultados.append(f"Copiado: {old_path} -> {new_path}")
        except Exception as e:
            errores.append(f"Error con '{old_path}' en '{root}': {e}")

for r in resultados:
    print(r)

if errores:
    print("\nSe produjeron errores:")
    for e in errores:
        print(e)
else:
    print("\nTodos los archivos fueron procesados correctamente.")
