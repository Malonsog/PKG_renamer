# collector.py
"""
Módulo para recolectar archivos .pkg y .rap en carpetas destino.
"""
import os
import shutil

def collect_files(base_path, pkg_dest, rap_dest):
    os.makedirs(pkg_dest, exist_ok=True)
    os.makedirs(rap_dest, exist_ok=True)
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_lower = file.lower()
            src = os.path.join(root, file)
            if file_lower.endswith('.pkg'):
                dest = os.path.join(pkg_dest, file)
                try:
                    shutil.copy2(src, dest)
                    print(f"Copiado: {src} -> {dest}")
                except Exception as e:
                    print(f"Error copiando {src}: {e}")
            elif file_lower.endswith('.rap'):
                dest = os.path.join(rap_dest, file)
                try:
                    shutil.copy2(src, dest)
                    print(f"Copiado: {src} -> {dest}")
                except Exception as e:
                    print(f"Error copiando {src}: {e}")
