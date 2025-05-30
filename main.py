# main.py
"""
Script principal para orquestar el flujo:
1. Extrae todos los archivos .zip y .rar en subcarpetas.
2. Renombra los archivos .pkg usando pkg_renamer.py.
3. Recolecta todos los .pkg y .rap en carpetas PKG/ y RAP/.
"""
import os
import subprocess
from extractor import extract_archives
from collector import collect_files

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PKG_DIR = os.path.join(BASE_PATH, 'PKG')
RAP_DIR = os.path.join(BASE_PATH, 'RAP')

if __name__ == "__main__":
    # 1. Extraer archivos comprimidos
    print("\n[1] Extrayendo archivos .zip y .rar...")
    extract_archives(BASE_PATH)

    # 2. Renombrar archivos .pkg
    print("\n[2] Renombrando archivos .pkg...")
    subprocess.run(["python", "pkg_renamer.py", BASE_PATH, "--sobrescribir"])

    # 3. Recolectar archivos .pkg y .rap
    print("\n[3] Recolectando archivos .pkg y .rap...")
    collect_files(BASE_PATH, PKG_DIR, RAP_DIR)

    print("\nProceso completo.")
