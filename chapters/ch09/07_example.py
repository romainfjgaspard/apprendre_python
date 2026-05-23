def battle(poke1_data, poke2_data):
    """Simulate a full battle. Returns the winner's name."""
    # Make copies so we don't modify the originals
    p1 = dict(poke1_data)
    p2 = dict(poke2_data)
    p1["max_hp"] = p1["hp"]
    p2["max_hp"] = p2["hp"]

    print(f"\n⚔️  {p1['name']} vs {p2['name']}!")
    print(f"     ({p1['type']})       ({p2['type']})\n")

    turn = 0
    while p1["hp"] > 0 and p2["hp"] > 0:
        turn += 1
        print(f"--- Turn {turn} ---")

        # Player 1 attacks
        dmg = calc_damage(p1, p2)
        p2["hp"] = max(0, p2["hp"] - dmg)
        mult = get_multiplier(p1["type"], p2["type"])
        eff = " 💥 Super effective!" if mult > 1 else (
              " 😕 Not very effective..." if mult < 1 else "")
        print(f"  {p1['name']} attacks! {dmg} damage!{eff}")
        display_hp(p2["name"], p2["hp"], p2["max_hp"])

        if p2["hp"] <= 0:
            break

        # Player 2 attacks
        dmg = calc_damage(p2, p1)
        p1["hp"] = max(0, p1["hp"] - dmg)
        mult = get_multiplier(p2["type"], p1["type"])
        eff = " 💥 Super effective!" if mult > 1 else (
              " 😕 Not very effective..." if mult < 1 else "")
        print(f"  {p2['name']} attacks! {dmg} damage!{eff}")
        display_hp(p1["name"], p1["hp"], p1["max_hp"])
        print()

    winner = p1["name"] if p1["hp"] > 0 else p2["name"]
    print(f"\n🏆 {winner} wins in {turn} turns!")
    return winner

# Run a battle!
winner = battle(ALL_POKEMON[0], ALL_POKEMON[1])  # Pikachu vs Charizard