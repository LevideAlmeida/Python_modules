"""
manage files with shutil module
"""

import os
import shutil


HOME = os.path.expanduser("~")
WORKSPACE = os.path.join(HOME, 'workspace')
PYTHON_PROJECT = os.path.join(WORKSPACE, "PythonProject")
NEW_DIRECTORY = os.path.join(WORKSPACE, "NEW_DIRECTORY")

# Remove a directory recursively
shutil.rmtree(NEW_DIRECTORY, ignore_errors=True)

# Copy a directory recursively
shutil.copytree(PYTHON_PROJECT, NEW_DIRECTORY)

# Move/rename a directory
shutil.move(NEW_DIRECTORY, NEW_DIRECTORY + "_NEW")  # Rename

shutil.move(NEW_DIRECTORY + "_NEW", os.path.join(WORKSPACE, "RPG"))
