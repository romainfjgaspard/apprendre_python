atk_type = "Fire"
def_type = "Grass"
base_damage = 50

if ((atk_type == "Fire" and def_type == "Grass") or
    (atk_type == "Grass" and def_type == "Water") or
    (atk_type == "Water" and def_type == "Fire")):
    multiplier = 2.0
    print("💥 It's super effective!")
elif ((atk_type == "Fire" and def_type == "Water") or
      (atk_type == "Grass" and def_type == "Fire") or
      (atk_type == "Water" and def_type == "Grass")):
    multiplier = 0.5
    print("😕 It's not very effective...")
else:
    multiplier = 1.0
    print("Normal effectiveness.")

final = base_damage * multiplier
print(f"{atk_type} vs {def_type}: {final} damage")