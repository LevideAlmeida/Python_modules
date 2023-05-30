"""

os.system - execute comands in cmd/shell

the command passed as a parameter, will be executed
in the cmd/shell
"""

import os

# clear screen in windows
# os.system('cls')

# clear screen in Unix
os.system('clear')

# command pwd returns current path
os.system('pwd')

# command echo is the same thing as print
os.system('echo "Hello world"')

# Open htop
# os.system('htop')


os.system('mkdir "te_zuei"')  # create a directory
os.system(' > te_zuei/AAAAAAAA.txt')  # Create a file

print('Your files: ')
os.system('ls')  # list the files/directorys in current directory
