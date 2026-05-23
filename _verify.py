"""Verification module for Python Quest notebooks.

Each notebook just calls:
    from _verify import verify
    verify(chapter_number, locals())

This keeps the verification cell short and the code hidden.
Results are saved to _results.json so jouer.py can read them.
"""

import json
import os
from pathlib import Path

RESULTS_FILE = Path(__file__).parent / "_results.json"


def _load():
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save(data):
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _check(label, condition, hint, results):
    if condition:
        results.append(True)
        print(f"  ✅ {label}")
    else:
        results.append(False)
        print(f"  ❌ {label} — 💡 {hint}")


# ═══════════════════════════════════════════════════════════════════════════════
# Chapter check definitions
# Each function receives ns = locals() from the notebook
# ═══════════════════════════════════════════════════════════════════════════════

def _ch1(ns, r):
    _check("trainer_name is text",
           type(ns.get('trainer_name')) is str and len(ns.get('trainer_name', '')) > 0,
           'Use quotes: trainer_name = "Ash"', r)
    _check("pokemon_name is text",
           type(ns.get('pokemon_name')) is str and len(ns.get('pokemon_name', '')) > 0,
           'Use quotes: pokemon_name = "Pikachu"', r)
    _check("pokemon_hp is a whole number",
           type(ns.get('pokemon_hp')) is int and 1 <= ns.get('pokemon_hp', 0) <= 999,
           'No quotes for numbers: pokemon_hp = 35', r)
    _check("pokemon_level is between 1 and 100",
           type(ns.get('pokemon_level')) is int and 1 <= ns.get('pokemon_level', 0) <= 100,
           'A whole number: pokemon_level = 5', r)
    pname = ns.get('pokemon_name', '')
    php = ns.get('pokemon_hp', '')
    pinfo = ns.get('pokemon_info', '')
    _check("pokemon_info contains your Pokémon's name",
           type(pinfo) is str and str(pname) in pinfo and str(php) in pinfo,
           'Use f-string: pokemon_info = f"{pokemon_name} — HP: {pokemon_hp}"', r)
    ok = sum(r)
    if ok == 5:
        tn = ns.get('trainer_name', '?')
        pn = ns.get('pokemon_name', '?')
        pl = ns.get('pokemon_level', '?')
        ph = ns.get('pokemon_hp', '?')
        print("  🎉 PERFECT! Your Pokémon journey begins!")
        print(f"\n  ┌────────────────────────────┐")
        print(f"  │  📋 TRAINER CARD            │")
        print(f"  │  Trainer: {tn:<17}│")
        print(f"  │  Partner: {pn:<17}│")
        print(f"  │  Level {pl}, HP {str(ph):<13}│")
        print(f"  └────────────────────────────┘")


def _ch2(ns, r):
    _check("new_score = 65", ns.get('new_score') == 65,
           'score - damage_taken → 100 - 35', r)
    _check("total_heal = 60", ns.get('total_heal') == 60,
           'potions * potion_heal → 3 * 20', r)
    _check("final_score = 125", ns.get('final_score') == 125,
           'new_score + total_heal → 65 + 60', r)
    _check("hits_survived = 4", ns.get('hits_survived') == 4,
           '200 // 45 → 4 (integer division)', r)
    _check("is_boosted is True", ns.get('is_boosted') is True,
           'final_score > 100 → 125 > 100 → True', r)
    if sum(r) == 5:
        print("  🎉 PERFECT! You mastered Pokémon math!")


def _ch3(ns, r):
    _check("is_alive is True", ns.get('is_alive') is True,
           'hp > 0 → 25 > 0 → True', r)
    hp = ns.get('health_pct', 0)
    _check("health_pct = 25.0", hp == 25.0 or hp == 25,
           'hp / max_hp * 100 → 25 / 100 * 100 = 25.0', r)
    _check("status is Injured", ns.get('status') == 'Injured',
           '25 > 20 → elif branch → Injured', r)
    _check("can_evolve is False", ns.get('can_evolve') is False,
           'is_alive AND level >= 16 → True AND False → False', r)
    if sum(r) == 4:
        print("  🎉 PERFECT! You master conditions!")


def _ch4(ns, r):
    _check("total_damage = 90", ns.get('total_damage') == 90,
           '6 attacks × 15 damage = 90', r)
    _check("turns = 4", ns.get('turns') == 4,
           '80 HP ÷ 25 damage = 3.2 → need 4 turns', r)
    _check("electric_count = 3", ns.get('electric_count') == 3,
           'There are 3 "Electric" entries in the list', r)
    if sum(r) == 3:
        print("  🎉 PERFECT! You mastered loops!")


def _ch5(ns, r):
    _check("team has 4 Pokémon", ns.get('team_size') == 4,
           'After adding 2 and removing 1: 3 + 2 - 1 = 4', r)
    team = ns.get('team', [])
    _check("Charizard and Mewtwo in team",
           "Charizard" in team and "Mewtwo" in team,
           'Use team.append("Charizard") and team.append("Mewtwo")', r)
    _check("Bulbasaur removed", "Bulbasaur" not in team,
           'Use team.remove("Bulbasaur")', r)
    st = ns.get('sorted_team', [])
    _check("sorted correctly", st == sorted(team),
           'sorted_team = sorted(team)', r)
    fa = ns.get('first_alpha', '')
    _check("first_alpha correct", fa == sorted(team)[0] if team else False,
           'Index 0 is the first item!', r)
    if sum(r) == 5:
        print("  🎉 PERFECT! Your team is ready!")


def _ch6(ns, r):
    _check("charizard_type is Fire", ns.get('charizard_type') == "Fire",
           'pokedex[1]["type"] — index 1 for Charizard, key "type"', r)
    _check("total_hp = 262", ns.get('total_hp') == 262,
           '35 + 78 + 45 + 44 + 60 = 262', r)
    _check("strong_count = 3", ns.get('strong_count') == 3,
           'Charizard(78), Gengar(60), Eevee(55) have HP > 50', r)
    pdex = ns.get('pokedex', [])
    _check("Mewtwo was added",
           len(pdex) == 6 and any(p.get("name") == "Mewtwo" for p in pdex if isinstance(p, dict)),
           'pokedex.append({"name": "Mewtwo", "type": "Psychic", "hp": 106})', r)
    if sum(r) == 4:
        print("  🎉 PERFECT! Your Pokédex is complete!")


def _ch7(ns, r):
    cd = ns.get('calc_damage')
    ia = ns.get('is_alive')
    hl = ns.get('heal')
    _check("calc_damage(60,40,50) = 75.0",
           callable(cd) and cd(60, 40, 50) == 75.0,
           '(60 / 40) * 50 = 75.0', r)
    _check("is_alive(10) is True",
           callable(ia) and ia(10) is True, '10 > 0 → True', r)
    _check("is_alive(0) is False",
           callable(ia) and ia(0) is False, '0 > 0 → False', r)
    _check("heal(30, 100) = 50",
           callable(hl) and hl(30, 100) == 50, '30 + 20 = 50 (default)', r)
    _check("heal(90, 100, 30) = 100",
           callable(hl) and hl(90, 100, 30) == 100, 'min(90+30, 100) = 100', r)
    if sum(r) == 5:
        print("  🎉 PERFECT! Your battle system is ready!")


def _ch8(ns, r):
    _check("my_pokedex.json exists",
           os.path.exists("my_pokedex.json"),
           'Use: with open("my_pokedex.json", "w") as f:', r)
    _check("pokemon_count is 3", ns.get('pokemon_count') == 3,
           'loaded_pokedex["pokemon"] — use "pokemon" as the key', r)
    _check("data_matches is True", ns.get('data_matches') is True,
           'Use json.dump() to save and json.load() to read', r)
    if sum(r) == 3:
        print("  🎉 PERFECT! You can save and load game data!")


def _boss1(ns, r):
    _check("Tournament completed (3 rounds)",
           ns.get('tournament_complete') is True, 'Run all the cells above!', r)
    _check("Results saved to file",
           os.path.exists("tournament_results.json"), 'Run step 5', r)
    _check("battle() function works",
           callable(ns.get('battle')), 'Run step 3', r)
    if sum(r) == 3:
        print("  🎉🎉🎉 SEASON 1 COMPLETE! You are a Python Pokémon Master!")
        print("  Season 2: Formula 1 is next... 🏎️")


# ─── SEASON 2 ────────────────────────────────────────────────────────────────

def _ch10(ns, r):
    grid = ns.get('grid', [])
    try:
        _check("grid has 10 rows", len(grid) == 10, 'Use range(10)', r)
        _check("Pole = Verstappen", grid[0][0] == 'Verstappen', 'grid[0][0]', r)
        _check("Last spot = Pérez", grid[9][1] == 'Pérez', 'grid[9][1]', r)
        _check("Each row has 2 cars", len(grid[0]) == 2, '2 drivers per row', r)
    except Exception as e:
        for _ in range(4 - len(r)):
            r.append(False)
        print(f"  💥 {e}")
    if sum(r) == 4:
        print("  🏆 Perfect grid! Lights out — go to Chapter 11!")


def _ch11(ns, r):
    ranking = ns.get('ranking', [])
    try:
        leader = ranking[0]
        _check("Leading team is Ferrari", leader['team'] == 'Ferrari',
               'Leclerc 280 + Sainz 220 = 500', r)
        _check("Leader has 500 pts", leader['points'] == 500, 'Sum Ferrari', r)
        _check("5 teams in ranking", len(ranking) == 5, '5 unique teams', r)
    except Exception as e:
        for _ in range(3 - len(r)):
            r.append(False)
        print(f"  💥 {e}")


def _ch12(ns, r):
    totals = ns.get('totals', {})
    try:
        _check("5 drivers in totals", len(totals) == 5, 'Loop over all drivers', r)
        _check("Times in valid range",
               all(80*50 <= t <= 85*50 for t in totals.values()),
               '50 laps × (80..85)', r)
        _check("totals is a dictionary", isinstance(totals, dict), 'Use {} not []', r)
    except Exception as e:
        for _ in range(3 - len(r)):
            r.append(False)
        print(f"  💥 {e}")


def _ch13(ns, r):
    lt = ns.get('lap_times', [])
    try:
        _check("20 laps generated", len(lt) == 20, 'n_laps must be 20', r)
        _check("All times >= 79.0s", round(min(lt), 1) >= 79.0, 'uniform(79,82)', r)
        _check("All times <= 82.0s", round(max(lt), 1) <= 82.0, 'uniform(79,82)', r)
    except Exception as e:
        for _ in range(3 - len(r)):
            r.append(False)
        print(f"  💥 {e}")


def _ch14(ns, r):
    _check("Leader = Verstappen", ns.get('leader') == 'Verstappen',
           '25+25+18 = 68', r)
    _check("Leader has 68 pts", ns.get('leader_pts') == 68,
           'Sum his 3 race results', r)
    _check("5 drivers in totals", len(ns.get('totals', {})) == 5,
           '5 unique drivers in the CSV', r)


def _ch15(ns, r):
    _check("Ferrari has 2 drivers", ns.get('n_ferrari') == 2, 'Leclerc + Sainz', r)
    _check("Ferrari wins = 4", ns.get('ferrari_wins') == 4, '3 + 1', r)
    _check("Ferrari pts = 500", ns.get('ferrari_points') == 500, '280 + 220', r)


def _ch16(ns, r):
    _check("2 subplots", ns.get('n_subplots') == 2, 'plt.subplots(1, 2, ...)', r)
    me = ns.get('max_evo', [0])
    le = ns.get('lec_evo', [0])
    _check("Verstappen leads at end", me[-1] > le[-1], '243 > 205', r)


def _boss2(ns, r):
    _check("10 races simulated", len(ns.get('season', {})) == 10, 'Run Step 3', r)
    _check("JSON file saved", os.path.exists('f1_season.json'), 'Run Step 4', r)
    _check("Dashboard built", ns.get('dashboard_done') is True, 'Run Step 5', r)
    if sum(r) == 3:
        ch = ns.get('champion', '?')
        print(f"  🏆🏆🏆 SEASON 2 COMPLETE! Champion: {ch}")
        print("  Next stop: Season 3 — Birds simulation 🐦")


# ─── SEASON 3 ────────────────────────────────────────────────────────────────

def _ch18(ns, r):
    _check("Team has 3+ Pokémon", ns.get('team_size', 0) >= 3, 'Add 3+ to the list', r)
    _check("First is Pikachu", ns.get('first_name') == 'Pikachu', 'team[0]', r)
    team = ns.get('team', [])
    _check("battle_cry() exists",
           team and hasattr(team[0], 'battle_cry'), 'def battle_cry(self, attack_name):', r)
    _check("__str__ exists",
           team and hasattr(team[0], '__str__'), 'def __str__(self):', r)


def _ch19(ns, r):
    _check("10 dots created", ns.get('n_dots') == 10, 'Create 10 dots', r)
    _check("Bounces > 0", ns.get('total_bounces', 0) > 0,
           'Increment self.bounces on each bounce', r)
    dots = ns.get('dots', [])
    W, H = ns.get('WIDTH', 100), ns.get('HEIGHT', 100)
    _check("All dots inside walls",
           all(0 <= d.x <= W and 0 <= d.y <= H for d in dots) if dots else False,
           'Reverse velocity when out of bounds', r)


def _ch20(ns, r):
    import numpy as np
    _check("20 dots", ns.get('n_dots') == 20, 'N = 20', r)
    _check("All inside [0, 100]", ns.get('all_inside') is True, 'Use % SIZE', r)
    pos = ns.get('pos')
    _check("Shape is (20, 2)",
           hasattr(pos, 'shape') and pos.shape == (20, 2), 'pos = 2D array', r)


def _ch21(ns, r):
    _check("Animation created", ns.get('bounce_anim_created') is True,
           'Run the animation cell', r)
    _check("25 dots in animation", ns.get('n_dots_anim') == 25, 'N = 25', r)


def _ch22(ns, r):
    _check("30 boids created", ns.get('n_boids') == 30, 'range(30)', r)
    _check("All inside walls", ns.get('all_inside') is True, 'Bounce logic', r)


def _ch23(ns, r):
    _check("Flocking ran", ns.get('flocking_works') is True,
           'Run the big code cell with 3 rules', r)
    _check("Separation observed", ns.get('obs_separation', '???') != '???',
           'Replace ??? with your observation', r)
    _check("Cohesion observed", ns.get('obs_cohesion', '???') != '???',
           'Replace ??? with your observation', r)


def _ch24(ns, r):
    _check("hunt() exists", ns.get('has_hunt') is True, 'def hunt(self, flock)', r)
    _check("Predator is faster", ns.get('pred_fast') is True, 'max_speed > 4', r)
    pred = ns.get('pred')
    Boid = ns.get('Boid')
    _check("Predator inherits Boid",
           pred is not None and Boid is not None and isinstance(pred, Boid),
           'class Predator(Boid):', r)


def _ch25(ns, r):
    _check("Interactive sim created", ns.get('interactive_done') is True,
           'Run the animation cell', r)
    _check("Slider exists", ns.get('slider_exists') is True,
           'radius_slider should be defined', r)


def _boss3(ns, r):
    _check("Simulation running", ns.get('simulation_running') is True, 'Run Step 3', r)
    _check("50 boids in flock", len(ns.get('flock', [])) == 50, 'N = 50', r)
    pred = ns.get('pred')
    Predator = ns.get('Predator')
    _check("Predator exists",
           pred is not None and Predator is not None and isinstance(pred, Predator),
           'pred = Predator(...)', r)
    if sum(r) == 3:
        print("\n  🏆🏆🏆 PYTHON QUEST COMPLETE!")
        print("  🎓 You are now a Pokémon Master of Python!")
        print("  🐦 Your birds are flocking beautifully!")


# ═══════════════════════════════════════════════════════════════════════════════
# Map chapter numbers → check functions
# ═══════════════════════════════════════════════════════════════════════════════

CHECKS = {
    1: _ch1,  2: _ch2,  3: _ch3,  4: _ch4,  5: _ch5,
    6: _ch6,  7: _ch7,  8: _ch8,  9: _boss1,
    10: _ch10, 11: _ch11, 12: _ch12, 13: _ch13, 14: _ch14,
    15: _ch15, 16: _ch16, 17: _boss2,
    18: _ch18, 19: _ch19, 20: _ch20, 21: _ch21, 22: _ch22,
    23: _ch23, 24: _ch24, 25: _ch25, 26: _boss3,
}


def verify(chapter, ns):
    """Run checks for a chapter. Call from notebook: verify(N, locals())"""
    fn = CHECKS.get(chapter)
    if fn is None:
        print(f"  ⚠️ No checks defined for chapter {chapter}")
        return

    print(f"  ✅ VERIFICATION — Chapter {chapter}")
    print()

    results = []
    try:
        fn(ns, results)
    except Exception as e:
        print(f"  💥 Error during verification: {e}")

    ok = sum(results)
    total = len(results)
    print(f"\n  Score: {ok}/{total}")

    # Save results for jouer.py
    all_results = _load()
    all_results[str(chapter)] = {"ok": ok, "total": total, "passed": ok == total}
    _save(all_results)
