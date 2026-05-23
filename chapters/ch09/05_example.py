def get_multiplier(atk_type, def_type):
    """Return type effectiveness multiplier."""
    chart = {
        ("Fire", "Grass"): 2.0,  ("Grass", "Water"): 2.0,  ("Water", "Fire"): 2.0,
        ("Fire", "Water"): 0.5,  ("Grass", "Fire"): 0.5,   ("Water", "Grass"): 0.5,
        ("Electric", "Water"): 2.0, ("Electric", "Grass"): 0.5,
    }
    return chart.get((atk_type, def_type), 1.0)

def calc_damage(attacker, defender):
    """Calculate damage from attacker to defender."""
    raw = (attacker["attack"] / defender["defense"]) * 50
    mult = get_multiplier(attacker["type"], defender["type"])
    # Add some randomness (±20%)
    luck = random.uniform(0.8, 1.2)
    return int(raw * mult * luck)

def display_hp(name, hp, max_hp):
    """Show a visual HP bar."""
    bar_len = 20
    filled = max(0, int(hp / max_hp * bar_len))
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"  {name:<12} [{bar}] {hp}/{max_hp} HP")

print("✅ Battle functions ready!")