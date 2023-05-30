"""
a
"""
from itertools import count
import os
import math


def format_size(size_in_bytes: int, base: int = 1000) -> str:
    """Format a size, from bytes to appropriate size"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # if size is less then or equal to 0, 0B.
    if size_in_bytes <= 0:
        return "0B"

    # Tuple with the sizes
    #               0    1     2     3     4     5
    size_simbols = "B", "KB", "MB", "GB", "TB", "PB"

    # Log -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log returns the log of size_in_bytes

    # with the base (1000by default), this should match
    # our index on abbreviation for sizes
    abbreviation_sizes_index = int(math.log(size_in_bytes, base))

    # Value to divide the size to do the conversion
    potency = base ** abbreviation_sizes_index

    # final size
    final_size = size_in_bytes / potency

    # The abbreviation
    size_abreviation = size_simbols[abbreviation_sizes_index]
    return f'{final_size:.2f} {size_abreviation}'


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
        full_path = os.path.join(root, file_)
        size = os.path.getsize(full_path)
        print('      ', the_counter, 'file', file_, format_size(size))
