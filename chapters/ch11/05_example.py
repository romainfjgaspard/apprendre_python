standings = [
    {'name': 'Verstappen', 'team': 'Red Bull',   'points': 410},
    {'name': 'Leclerc',    'team': 'Ferrari',    'points': 280},
    {'name': 'Norris',     'team': 'McLaren',    'points': 350},
    {'name': 'Sainz',      'team': 'Ferrari',    'points': 220},
    {'name': 'Hamilton',   'team': 'Mercedes',   'points': 190},
    {'name': 'Russell',    'team': 'Mercedes',   'points': 175},
    {'name': 'Alonso',     'team': 'Aston',      'points': 95},
]

# Sort by points (descending)
ranked = sorted(standings, key=lambda d: d['points'], reverse=True)

print('🏆 CHAMPIONSHIP STANDINGS')
print('-' * 40)
for i, d in enumerate(ranked, start=1):
    print(f"  P{i:<2} {d['name']:<12} {d['team']:<10} {d['points']:>4} pts")