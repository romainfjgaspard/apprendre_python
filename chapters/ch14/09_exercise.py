import csv

with open('f1_results.csv', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# TODO: build a dict {driver: total_points}
totals = {}
for r in rows:
    name = r['driver']
    pts  = ???   # convert r['points'] to int
    totals[name] = totals.get(name, 0) + pts

# TODO: find the leader (driver with max points)
leader = ???
leader_pts = totals[leader]

print('🏆 Standings:')
for d, p in sorted(totals.items(), key=lambda x: -x[1]):
    print(f'  {d:<12} {p} pts')
print(f'\n👑 Leader: {leader} ({leader_pts} pts)')