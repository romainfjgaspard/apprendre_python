# Only Ferrari drivers
ferrari = [d for d in standings if d['team'] == 'Ferrari']
print('🐎 Ferrari drivers:')
for d in ferrari:
    print(f"   {d['name']} — {d['points']} pts")

# Drivers with more than 200 points
top = [d for d in standings if d['points'] > 200]
print(f"\n🔥 {len(top)} drivers have > 200 points")