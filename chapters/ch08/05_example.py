import json

# Convert a JSON string back to Python data
json_text = '{"name": "Ash", "badges": 3, "team": ["Pikachu", "Charizard"]}'

data = json.loads(json_text)
print(f"Name: {data['name']}")
print(f"Badges: {data['badges']}")
print(f"Team: {data['team']}")
print(f"Type: {type(data)}")   # dict

# Access nested data
first_pokemon = data["team"][0]
print(f"First Pokémon: {first_pokemon}")

# ⚠️ Python local only (PyCharm, terminal):
# with open("data.json", "r") as f:
#     data = json.load(f)