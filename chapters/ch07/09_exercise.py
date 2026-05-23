# --- Battle Functions ---

# 1. Write a function that calculates damage.
#    Formula: (attack / defense) * power
def calc_damage(attack, defense, power):
    return ???

# 2. Write a function that checks if a Pokémon is alive.
#    Return True if hp > 0, False otherwise.
def is_alive(hp):
    return ???

# 3. Write a function that heals a Pokémon.
#    Add heal_amount to current_hp, but do NOT exceed max_hp.
#    Hint: use min(current_hp + heal_amount, max_hp)
def heal(current_hp, max_hp, heal_amount=20):
    return ???

# Test your functions:
dmg = calc_damage(60, 40, 50)
print(f"Damage: {dmg}")

print(f"Alive at 10 HP? {is_alive(10)}")
print(f"Alive at 0 HP? {is_alive(0)}")

new_hp = heal(30, 100)
print(f"Healed: 30 → {new_hp}")

capped = heal(90, 100, 30)
print(f"Healed (capped): 90 → {capped}")