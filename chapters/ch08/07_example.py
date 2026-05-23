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

# Save: Python → JSON string
saved = json.dumps(save_data, indent=2)
print("✅ Converted to JSON!")
print(saved)

# Load: JSON string → Python
loaded = json.loads(saved)

print(f"\nTrainer: {loaded['trainer']}")
print(f"Badges: {loaded['badges']}")
print(f"Team: {[p['name'] for p in loaded['team']]}")
print(f"Data matches? {loaded == save_data}")

# ⚠️ Python local only (PyCharm, terminal):
# with open("save.json", "w") as f: json.dump(save_data, f, indent=2)
# with open("save.json", "r") as f: loaded = json.load(f)