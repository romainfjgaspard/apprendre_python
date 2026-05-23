pikachu = {"name": "Pikachu", "type": "Electric", "hp": 35, "attack": 55}

# Loop through key-value pairs
for key, value in pikachu.items():
    print(f"  {key}: {value}")

print()

# Check if a key exists
if "type" in pikachu:
    print(f"Type is: {pikachu['type']}")