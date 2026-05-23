print("\n🏟️ === POKÉMON ARENA TOURNAMENT ===")
print("="*40)

fighters = random.sample(ALL_POKEMON, 6)  # pick 6 random Pokémon
results = []

for round_num in range(3):
    p1 = fighters[round_num * 2]
    p2 = fighters[round_num * 2 + 1]
    winner = battle(p1, p2)
    results.append(winner)

print("\n" + "="*40)
print("🏆 TOURNAMENT RESULTS:")
for i, w in enumerate(results):
    print(f"  Round {i+1}: {w} wins!")

tournament_complete = len(results) == 3
print(f"\n✅ Tournament complete: {tournament_complete}")