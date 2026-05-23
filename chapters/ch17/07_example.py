season = {}
for track in TRACKS:
    season[track] = run_race(track)

# Aggregate driver totals
totals = {d['name']: 0 for d in DRIVERS}
for results in season.values():
    for r in results:
        totals[r['driver']] += r['points']

ranking = sorted(totals.items(), key=lambda x: -x[1])

print('🏆 FINAL DRIVERS CHAMPIONSHIP')
print('-' * 40)
for i, (name, pts) in enumerate(ranking, start=1):
    print(f'  P{i}  {name:<12} {pts:>4} pts')

champion = ranking[0][0]
print(f'\n👑 World Champion: {champion}')