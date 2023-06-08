"""
json to save and load data
"""
import json
# from pprint import pprint
# Extra: pprint is a PrettyPrint

string_json: str = '''
{
    "name": "Hyouken no majutsushi",
    "MAL rating": 6.36,
    "is_anime": true,
    "characters": ["Ray White", "Amelia Rose", "Claris Cliveland"],
    "year": 2023,
    "budget": null
}
'''

# json.loads to load a STRING as json
anime = json.loads(string_json)
# print(anime)
# pprint(anime)

# print(anime['name'])
# print(anime["characters"][1])

# json.dumps to dump a json string
print(json.dumps(anime, indent=2))
