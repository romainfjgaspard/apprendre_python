# --- Pokémon Battle! ---

# 1. An enemy has 80 HP. You deal 25 damage per turn.
#    Use a while loop to count how many turns to KO it.
enemy_hp = 80
turns = 0
while ???:
    enemy_hp = enemy_hp - 25
    turns = turns + 1

# 2. Your Pokémon starts at 90 HP. Each healing restores 15 HP.
#    How many heals until HP reaches exactly 150?
my_hp = 90
heals = 0
while my_hp < ???:
    my_hp = my_hp + 15
    heals = heals + 1

print(f"Enemy KO'd in: {turns} turns")
print(f"Healed {heals} times, final HP: {my_hp}")
