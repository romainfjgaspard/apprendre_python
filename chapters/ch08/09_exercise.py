import json

# --- Save & Load your Pokédex (in memory) ---

my_pokedex = {
    "trainer": "Basile",
    "pokemon": [
        {"name": "Pikachu", "type": "Electric", "hp": 35},
        {"name": "Charizard", "type": "Fire", "hp": 78},
        {"name": "Mewtwo", "type": "Psychic", "hp": 106},
    ]
}

# 1. Convert the Pokédex to a JSON string using json.dumps
#    Use indent=2 for readability
json_text = json.???(my_pokedex, ???=2)

# 2. Load it back from the JSON string using json.loads
loaded_pokedex = json.???(json_text)

# 3. How many Pokémon are in the loaded data?
pokemon_count = len(loaded_pokedex[???])

# 4. Does the loaded data match the original?
data_matches = loaded_pokedex == my_pokedex

print(f"JSON length: {len(json_text)} characters")
print(f"Pokémon count: {pokemon_count}")
print(f"Data matches: {data_matches}")