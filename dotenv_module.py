import os
from dotenv import load_dotenv

# DOC: https://pypi.org/project/python-dotenv/

# search a .env file in the root dir
load_dotenv()

# print(os.environ)  # All environment variables in the system

print(os.getenv('BD_PASSWORD'))  # Get a environment variable
