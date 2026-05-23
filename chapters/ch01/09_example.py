# Two Pokémon side by side
poke1_name = "Charizard"
poke1_hp   = 78
poke1_type = "Fire"

poke2_name = "Blastoise"
poke2_hp   = 79
poke2_type = "Water"

print(f"🔥 {poke1_name} ({poke1_type}) — HP: {poke1_hp}")
print(f"💧 {poke2_name} ({poke2_type}) — HP: {poke2_hp}")
print()

# Who has more HP?
if poke1_hp > poke2_hp:
    print(f"{poke1_name} has more HP!")
else:
    print(f"{poke2_name} has more HP!")