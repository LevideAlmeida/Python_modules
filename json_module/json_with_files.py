"""
json to save and load .json files
"""
import json
import os

FILE_NAME = 'anime.json'
ABSOLUTE_PATH_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

anime = {
    "name": "Hyouken no majutsushi",
    "MAL rating": 6.36,
    "is_anime": True,
    "characters": [
        "Ray White",
        "Amelia Rose",
        "Claris Cliveland"
    ],
    "year": 2023,
    "budget": None
}

with open(ABSOLUTE_PATH_FILE, 'w', encoding="UTF-8") as file:
    # Saving data in a json file
    json.dump(anime, file, indent=2)

with open(ABSOLUTE_PATH_FILE, 'r', encoding="UTF-8") as file:
    # Loading the data into a json file
    anime_json = json.load(file)
    print(anime_json)
