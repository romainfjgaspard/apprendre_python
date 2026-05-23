import random
random.seed(7)

drivers = ['Verstappen', 'Leclerc', 'Norris', 'Hamilton', 'Alonso']
n_laps  = 50

# TODO: build a dict {driver: total_time_in_seconds}
# Hint: use random.uniform(80.0, 85.0) for each lap
totals = ???

# Sort by total time (fastest first)
ranking = sorted(totals.items(), key=lambda x: x[1])

print(f'🏁 RACE RESULTS — {n_laps} laps')
print('-' * 40)
for i, (name, t) in enumerate(ranking, start=1):
    gap = t - ranking[0][1]
    gap_str = '   --' if i == 1 else f'+{gap:>5.2f}s'
    print(f'  P{i}  {name:<12} {t:>7.2f}s   {gap_str}')

winner = ranking[0][0]
print(f'\n🏆 Winner: {winner}')