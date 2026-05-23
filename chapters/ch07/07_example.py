def get_type_multiplier(atk_type, def_type):
    """Return 2.0, 0.5, or 1.0 based on type matchup."""
    super_effective = [
        ("Fire", "Grass"), ("Grass", "Water"), ("Water", "Fire"),
    ]
    not_effective = [
        ("Fire", "Water"), ("Grass", "Fire"), ("Water", "Grass"),
    ]
    if (atk_type, def_type) in super_effective:
        return 2.0
    elif (atk_type, def_type) in not_effective:
        return 0.5
    return 1.0

def battle_damage(atk, dfn, power, atk_type, def_type):
    """Calculate damage with type effectiveness."""
    raw = (atk / dfn) * power
    mult = get_type_multiplier(atk_type, def_type)  # ← calls the other function!
    return raw * mult

# Fire vs Grass — super effective!
dmg = battle_damage(84, 49, 50, "Fire", "Grass")
print(f"🔥→🌿  Damage: {dmg:.1f}  (super effective!)")

# Fire vs Water — not very effective
dmg = battle_damage(84, 83, 50, "Fire", "Water")
print(f"🔥→💧  Damage: {dmg:.1f}  (not very effective)")