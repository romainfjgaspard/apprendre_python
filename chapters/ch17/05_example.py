def run_race(track):
    scores = []
    for d in DRIVERS:
        score = d['skill'] + random.uniform(0, 30)
        scores.append((d['name'], d['team'], score))
    scores.sort(key=lambda x: -x[2])  # best first
    return [{'pos': i + 1,
             'driver': name,
             'team':   team,
             'points': POINTS_TABLE[i]}
            for i, (name, team, _) in enumerate(scores)]

# Test on one track
demo = run_race('Bahrain')
print('🇧🇭 Bahrain GP:')
for r in demo:
    print(f"  P{r['pos']}  {r['driver']:<12} {r['team']:<10} {r['points']:>2} pts")