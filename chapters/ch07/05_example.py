def heal(pokemon_name, current_hp, amount=20):
    new_hp = current_hp + amount
    print(f"💊 {pokemon_name} healed! HP: {current_hp} → {new_hp}")
    return new_hp

# Use default healing amount (20)
hp = heal("Pikachu", 15)

# Use a custom healing amount
hp = heal("Pikachu", hp, amount=50)