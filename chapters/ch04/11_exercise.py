# --- Training & Battles ---

# 1. Use a for loop to calculate the total damage of 6 attacks.
#    Each attack does 15 damage. What is the total?
total_damage = 0
for i in range(6):
    total_damage = total_damage + ???

# 2. An enemy has 80 HP. You deal 25 damage per turn.
#    Use a while loop to count how many turns to KO it.
enemy_hp = 80
turns = 0
while ???:
    enemy_hp = enemy_hp - 25
    turns = turns + 1

# 3. Count how many Pokémon in this list are Electric type.
types = ["Fire", "Electric", "Water", "Electric", "Grass", "Electric"]
electric_count = 0
for t in types:
    if t == ???:
        electric_count = electric_count + 1

print(f"Total damage: {total_damage}")
print(f"Turns to KO: {turns}")
print(f"Electric types: {electric_count}")