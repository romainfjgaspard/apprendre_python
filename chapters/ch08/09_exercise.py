import json

# --- Save & Load your Pokédex ---

my_pokedex = {
    "trainer": "Basile",
    "pokemon": [
        {"name": "Pikachu", "type": "Electric", "hp": 35},
        {"name": "Charizard", "type": "Fire", "hp": 78},
        {"name": "Mewtwo", "type": "Psychic", "hp": 106},
    ]
}

# 1. Save the Pokédex to "my_pokedex.json" using json.dump
#    Don't forget: "w" mode and indent=2 for readability
with open(???, ???) as f:
    json.???(my_pokedex, f, indent=2)

# 2. Load it back from the file
with open("my_pokedex.json", "r") as f:
    loaded_pokedex = json.???(f)

# 3. How many Pokémon are in the loaded data?
pokemon_count = len(loaded_pokedex[???])

# 4. Does the loaded data match the original?
data_matches = loaded_pokedex == my_pokedex

print(f"Saved and loaded {pokemon_count} Pokémon")
print(f"Data matches: {data_matches}")