# Save a battle log!
with open("battle_log.txt", "w") as f:
    f.write("=== Pokémon Battle Log ===\n")
    f.write("Pikachu used Thunderbolt!\n")
    f.write("It's super effective!\n")
    f.write("Charizard fainted!\n")

print("✅ File saved!")