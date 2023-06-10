"""
manage files with pathlib
"""
from pathlib import Path

file = Path.home() / 'workspace' / 'file.txt'

# Create empty file
file.touch()

print(file)

# Write in the file
file.write_text('Hello World')

# Read file
print(file.read_text())

# Erase file
file.unlink()


# Overwrite with open
file_path = Path.home() / 'workspace' / 'file2.txt'

with file_path.open('+a') as file2:
    file2.write('one line\n')
    file2.write('two line')

file_path.unlink()
