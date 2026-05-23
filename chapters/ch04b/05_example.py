import random

# Try to find a rare Pokémon — stop as soon as you find it!
found = False
attempts = 0

while not found:
    attempts = attempts + 1
    encounter = random.randint(1, 10)
    print(f"  Attempt {attempts}: encountered Pokémon #{encounter}")
    if encounter == 7:   # Rare Pokémon #7!
        print(f"  ✅ Found rare Pokémon after {attempts} attempts!")
        break
    if attempts >= 10:
        print("  😢 Gave up after 10 attempts.")
        break
