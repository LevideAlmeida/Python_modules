"""
os.walk - to traverse a directory

This command return a sequence of tuples, where each tuple has three elements:
the current directory (root), a subdirectories list (dirs)
and a root file list (files).

"""

import os
from itertools import count

path = os.path.join('/home', 'iqnus', 'workspace', 'Pygame')
counter = count()

for root, dirs, files in os.walk(path):

    if 'venv' in root.split('/'):
        continue

    the_counter = next(counter)

    print(the_counter, "Current directory", root)

    for dir_ in dirs:
        print('  ', the_counter, 'dir', dir_)

    for file_ in files:
        print('      ', the_counter, 'file', file_)
