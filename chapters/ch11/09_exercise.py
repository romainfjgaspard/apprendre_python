# Step 1: list of all unique team names
teams = list({d['team'] for d in standings})
print('Teams:', teams)

# Step 2: total points per team — TODO
# Hint: for each team, sum d['points'] for d in standings if d['team'] == team
team_totals = ???   # should be a list of dicts: [{'team': ..., 'points': ...}, ...]

# Step 3: sort by points, descending — TODO
ranking = ???

print('\n🏆 CONSTRUCTORS CHAMPIONSHIP')
for i, t in enumerate(ranking, start=1):
    print(f"  P{i}  {t['team']:<10} {t['points']:>4} pts")