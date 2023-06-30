"""
Module to handle requests to the API
This module is not native to python, install using pip install requests
"""

# Tutorial -> https://youtu.be/Qd8JT0bnJGs

import requests

url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
