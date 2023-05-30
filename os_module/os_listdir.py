"""
os.listdir to list itens in a directory
"""

import os

path = os.path.join('/home', 'iqnus', 'workspace', 'Pygame')

for item in os.listdir(path):
    full_path = os.path.join(path, item)
    print(item)

    if not os.path.isdir(full_path):
        print()
        continue

    for file in os.listdir(full_path):
        print('    ', file)

    print()
