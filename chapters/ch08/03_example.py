import json

# Convert data to a JSON string — works in any Python, including the browser!
data = {"name": "Ash", "badges": 3, "team": ["Pikachu", "Charizard"]}

json_text = json.dumps(data, indent=2)
print("JSON text:")
print(json_text)
print()
print(f"Type: {type(json_text)}")   # str
print(f"Length: {len(json_text)} characters")

# ⚠️ Python local only (PyCharm, terminal):
# with open("data.json", "w") as f:
#     f.write(json_text)