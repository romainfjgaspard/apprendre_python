by_team = df.groupby('team').agg(
    total_points=('points', 'sum'),
    total_wins  =('wins',   'sum'),
    drivers     =('driver', 'count'),
).sort_values('total_points', ascending=False)

print('🏆 Constructors Championship:')
print(by_team)