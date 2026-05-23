import json

# Our team data
save_data = {
    "trainer": "Ash",
    "badges": 3,
    "team": [
        {"name": "Pikachu", "hp": 35, "level": 25},
        {"name": "Charizard", "hp": 78, "level": 36},
    ]
}

# Save to JSON
with open("save_game.json", "w") as f:
    json.dump(save_data, f, indent=2)
print("✅ Game saved!")

# Load from JSON
with open("save_game.json", "r") as f:
    loaded = json.load(f)

print(f"Trainer: {loaded['trainer']}")
print(f"Badges: {loaded['badges']}")
print(f"Team: {[p['name'] for p in loaded['team']]}")
print(f"Data matches? {loaded == save_data}")