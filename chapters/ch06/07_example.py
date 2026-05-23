pokedex = [
    {"name": "Pikachu",   "type": "Electric", "hp": 35,  "attack": 55},
    {"name": "Charizard", "type": "Fire",     "hp": 78,  "attack": 84},
    {"name": "Blastoise", "type": "Water",    "hp": 79,  "attack": 83},
    {"name": "Mewtwo",    "type": "Psychic",  "hp": 106, "attack": 110},
    {"name": "Eevee",     "type": "Normal",   "hp": 55,  "attack": 55},
]

# Print all Pokémon
for p in pokedex:
    print(f"  {p['name']:<12} {p['type']:<10} HP:{p['hp']}  ATK:{p['attack']}")

# Find the strongest (highest attack)
strongest = max(pokedex, key=lambda p: p["attack"])
print(f"\n🏆 Strongest: {strongest['name']} (ATK: {strongest['attack']})")

# Filter: only Fire and Water types
selected = [p for p in pokedex if p["type"] in ["Fire", "Water"]]
print(f"Fire/Water: {[p['name'] for p in selected]}")