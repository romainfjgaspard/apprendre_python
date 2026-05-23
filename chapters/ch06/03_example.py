pikachu = {
    "name": "Pikachu",
    "type": "Electric",
    "hp": 35,
    "attack": 55,
    "defense": 40,
}

print(pikachu["name"])      # Pikachu
print(pikachu["hp"])        # 35
print(pikachu["attack"])    # 55

# Update a value
pikachu["hp"] = 45
print(f"New HP: {pikachu['hp']}")

# Add a new key
pikachu["level"] = 25
print(pikachu)