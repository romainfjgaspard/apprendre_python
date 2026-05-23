# --- Build your Pokédex ---

# Here is a small Pokédex:
pokedex = [
    {"name": "Pikachu",   "type": "Electric", "hp": 35},
    {"name": "Charizard", "type": "Fire",     "hp": 78},
    {"name": "Bulbasaur", "type": "Grass",    "hp": 45},
    {"name": "Squirtle",  "type": "Water",    "hp": 44},
    {"name": "Gengar",    "type": "Ghost",    "hp": 60},
]

# 1. What is Charizard's type? Access it from the pokedex list.
#    (Charizard is at index 1)
charizard_type = pokedex[???][???]

# 2. What is the total HP of all Pokémon?
#    Use a for loop or sum() with a list comprehension.
total_hp = ???

# 3. How many Pokémon have HP > 50?
strong_count = len([p for p in pokedex if ???])

# 4. Add a new Pokémon to the Pokédex:
#    Mewtwo, Psychic type, 106 HP
pokedex.append(???)

print(f"Charizard type: {charizard_type}")
print(f"Total HP: {total_hp}")
print(f"Strong Pokémon (>50 HP): {strong_count}")
print(f"Pokédex size: {len(pokedex)}")