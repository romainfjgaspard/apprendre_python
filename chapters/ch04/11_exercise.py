# --- Pokémon Training ---

# 1. Print each Pokémon in the team using a for loop.
team = ["Pikachu", "Charizard", "Bulbasaur", "Snorlax"]
for pokemon in ???:
    print(f"  ⭐ {pokemon}")

# 2. Use range() to simulate 5 training sessions.
#    Each session adds 10 XP. What is the total XP?
xp = 0
for i in range(???):
    xp = xp + 10

# 3. Count how many Pokémon in this list are Fire type.
types = ["Fire", "Electric", "Water", "Fire", "Grass", "Fire"]
fire_count = 0
for t in types:
    if t == ???:
        fire_count = fire_count + 1

print(f"Total XP after training: {xp}")
print(f"Fire types: {fire_count}")