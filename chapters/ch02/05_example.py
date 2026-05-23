# Pokémon damage formula (simplified)
attack = 55
defense = 40
base_power = 50
level = 5

# Regular damage
damage = (attack / defense) * base_power
print(f"Damage: {damage}")
print(f"Type: {type(damage)}")  # float — division gives float!

# Integer division — rounds down
damage_int = (attack * base_power) // defense
print(f"Integer damage: {damage_int}")

# Critical hit — double damage!
critical = damage * 2
print(f"💥 Critical hit! {critical} damage!")