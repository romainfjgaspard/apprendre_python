import random

# Wild encounter — try to catch a Pokémon!
for attempt in range(10):
    catch_chance = random.randint(1, 100)
    print(f"  Attempt {attempt + 1}: rolled {catch_chance}...")
    if catch_chance > 70:
        print(f"  ✅ Caught on attempt {attempt + 1}!")
        break
else:
    # This runs only if we never broke out of the loop
    print("  😢 The Pokémon escaped after 10 attempts!")