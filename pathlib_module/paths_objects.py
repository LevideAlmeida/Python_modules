"""
pathlib to create path objects
"""
from pathlib import Path


project_path = Path()
print(project_path)  # Relative path
print(project_path.absolute())  # Absolute path
# Both paths return the path where the file was executed

file_path = Path(__file__)
print(file_path)  # Return file
print(file_path.absolute())  # Return the file absolute path
print(file_path.parent)  # Return the previous directory

# Path() objects use the / to union paths
new_path = file_path / "new_directory" / "file.txt"
print(new_path)

# User home
print(Path.home())
