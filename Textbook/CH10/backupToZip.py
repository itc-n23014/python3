import os
import pathlib
import shutil
import zipfile
from pathlib import Path

def backup(folder):
    i = 1
    while (Path.home() / f'backup{i}.zip').exists():
        i += 1
    backup_zip_path = Path.home() / f'backup{i}.zip'

    # 一時ディレクトリを作成する前に既存のディレクトリを削除
    temp_dir = Path.home() / f'temp_backup_{i}'
    if temp_dir.exists():
        shutil.rmtree(temp_dir)

    shutil.copytree(folder, temp_dir)
    
    with zipfile.ZipFile(backup_zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(temp_dir)
                backup_zip.write(file_path, arcname)
    
    shutil.rmtree(temp_dir)
    print(f'{backup_zip_path}にバックアップが作られました.')

folder = input('圧縮するフォルダを絶対パスで指定: ')
backup(folder)

