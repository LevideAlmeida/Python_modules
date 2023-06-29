# ZIP - zip / unzip files with zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
ROOT_PATH = Path(__file__).parent
ZIP_DIR_PATH = ROOT_PATH / 'dir_zip_module'
ZIP_PATH = ROOT_PATH / 'zipped_zip_dir.zip'
UNZIP_PATH = ROOT_PATH / 'unzipped_zip_dir'

shutil.rmtree(ZIP_DIR_PATH, ignore_errors=True)
Path.unlink(ZIP_PATH, missing_ok=True)
shutil.rmtree(str(ZIP_PATH).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(UNZIP_PATH, ignore_errors=True)

# raise Exception()

# Create dir
ZIP_DIR_PATH.mkdir(exist_ok=True)


def create_files(qtd: int, zip_dir: Path):
    for i in range(qtd):
        text = f'file_{i}'
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)


create_files(10, ZIP_DIR_PATH)

# Create zip
with ZipFile(ZIP_PATH, 'w') as zip:
    for root, dirs, files in os.walk(ZIP_DIR_PATH):
        for file in files:
            zip.write(os.path.join(root, file), file)

# Read the zip
with ZipFile(ZIP_PATH, 'r') as zip:
    for file in zip.namelist():
        print(file)

# Extract zip
with ZipFile(ZIP_PATH, 'r') as zip:
    zip.extractall(UNZIP_PATH)
