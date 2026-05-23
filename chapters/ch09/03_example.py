import random
import json

# All available Pokémon
ALL_POKEMON = [
    {"name": "Pikachu",   "type": "Electric", "hp": 35,  "attack": 55,  "defense": 40},
    {"name": "Charizard", "type": "Fire",     "hp": 78,  "attack": 84,  "defense": 78},
    {"name": "Blastoise", "type": "Water",    "hp": 79,  "attack": 83,  "defense": 100},
    {"name": "Venusaur",  "type": "Grass",    "hp": 80,  "attack": 82,  "defense": 83},
    {"name": "Mewtwo",    "type": "Psychic",  "hp": 106, "attack": 110, "defense": 90},
    {"name": "Gengar",    "type": "Ghost",    "hp": 60,  "attack": 65,  "defense": 60},
    {"name": "Dragonite", "type": "Dragon",   "hp": 91,  "attack": 134, "defense": 95},
    {"name": "Snorlax",   "type": "Normal",   "hp": 160, "attack": 110, "defense": 65},
]

# Print them all!
print("🏟️ POKÉMON ARENA — Available fighters:\n")
for i, p in enumerate(ALL_POKEMON):
    print(f"  {i+1}. {p['name']:<12} {p['type']:<10} "
          f"HP:{p['hp']:<4} ATK:{p['attack']:<4} DEF:{p['defense']}")