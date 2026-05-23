hp_values = [35, 78, 106, 45, 79, 150]

# Double all HP values
doubled = [hp * 2 for hp in hp_values]
print(f"Doubled: {doubled}")

# Filter: only HP above 70
strong = [hp for hp in hp_values if hp > 70]
print(f"Strong (>70 HP): {strong}")

# Count: how many are above 70?
print(f"Count: {len(strong)}")