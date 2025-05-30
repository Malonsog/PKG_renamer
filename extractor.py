# extractor.py
"""
Módulo con funciones para extraer archivos .zip y .rar en carpetas separadas.
"""
import os
import zipfile
try:
    import rarfile
except ImportError:
    rarfile = None

def extract_archives(base_path, dest_root=None):
    """
    Extrae todos los archivos .zip y .rar en subcarpetas con su nombre base.
    """
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_lower = file.lower()
            if file_lower.endswith('.zip') or file_lower.endswith('.rar'):
                archive_path = os.path.join(root, file)
                folder_name = os.path.splitext(file)[0]
                dest_dir = os.path.join(dest_root or root, folder_name)
                os.makedirs(dest_dir, exist_ok=True)
                try:
                    if file_lower.endswith('.zip'):
                        with zipfile.ZipFile(archive_path, 'r') as zf:
                            zf.extractall(dest_dir)
                    elif file_lower.endswith('.rar') and rarfile:
                        with rarfile.RarFile(archive_path, 'r') as rf:
                            rf.extractall(dest_dir)
                    print(f"Extraído: {archive_path} -> {dest_dir}")
                except Exception as e:
                    print(f"Error extrayendo {archive_path}: {e}")
