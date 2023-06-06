"""
os and shutil to copy files
"""

import os
import shutil


HOME = os.path.expanduser("~")
WORKSPACE = os.path.join(HOME, 'workspace')
PYTHON_PROJECT = os.path.join(WORKSPACE, "PythonProject")
NEW_DIRECTORY = os.path.join(WORKSPACE, "NEW_DIRECTORY")


# def print_files(directory: str):
#     for file_ in files:
#         if ".git" in directory or "venv" in directory:
#             continue
#         print(os.path.join(directory, file_))


# Creates a new directory in NEW_DIRECTORY if it doesn't exist

# Using an if
# if not os.path.exists(NEW_DIRECTORY):
#     os.makedirs(NEW_DIRECTORY)


# Using the parameter exist_ok in the method
os.makedirs(NEW_DIRECTORY, exist_ok=True)


for root, dirs, files in os.walk(PYTHON_PROJECT):
    for dir_ in dirs:
        new_dir_path = os.path.join(root.replace(
            PYTHON_PROJECT, NEW_DIRECTORY), dir_)

        if ".git" in new_dir_path or 'venv' in new_dir_path:
            continue

        # print(new_dir_path)
        os.makedirs(new_dir_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = os.path.join(root.replace(
            PYTHON_PROJECT, NEW_DIRECTORY), file)

        if ".git" in new_file_path or 'venv' in new_file_path:
            continue

        # print(new_file_path)
        shutil.copy(file_path, new_file_path)
