def calculate_damage(attack, defense, power):
    damage = (attack / defense) * power
    return damage

# Use the function
result = calculate_damage(55, 40, 50)
print(f"Damage: {result}")

# Use it again with different values!
result2 = calculate_damage(84, 78, 60)
print(f"Damage: {result2:.1f}")