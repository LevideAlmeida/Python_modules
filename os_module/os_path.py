"""

os.path - works with paths in Windows, Linux and Mac

Doc: https://docs.python.org/3/library/os.path.html#module-os.path

os.path is a module that provide functions for works with file paths
in Windows, Mac or Linux without having to worry about the diferences
between the systems.

"""

# os.path exemples commands:
# os.path.join: join strings in a single path.
# This way:
# os.path.join('directory1', 'directory2', 'file.txt') returns
# 'directory1/directory2/file.txt' in Linux or Mac, and
# 'directory1\directory2\file.txt' in Windows.

# os.path.split: divide a path in a tuple (directory, file).
# For exemple, os.path.split('/home/user/file.txt')
# retorns ('/home/user', 'file.txt').

# os.path.exists: checks if a path exists.

# os.path just work with file paths and don't do anyone
# entry/exit operation (I/O) with the files.

import os

path = os.path.join('/home/iqnus', 'workspace', 'project.txt')
print(path)

# Getting the directory path, and file name
directory, file = os.path.split(path)
print(directory, file)

# getting file name and extension
file_name, file_extension = os.path.splitext(file)
print(file_name, file_extension)

# checks if the path exists.
print(os.path.exists(path))
