"""
manage directories with pathlib
"""
from pathlib import Path
from shutil import rmtree

dir_path = Path.home() / 'workspace' / 'PY'

# Create dir
dir_path.mkdir(exist_ok=True)

# Make a subdir in a dir
subdir_path = dir_path / 'subdir'

subdir_path.mkdir(exist_ok=True)

for i in range(1, 6):
    file = subdir_path / f'file{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('+a') as text_file:
        text_file.write(f"H{i * 'e'}{i * 'y'}")

# Erase dir and everything inside it
rmtree(dir_path)
