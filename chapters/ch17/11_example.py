import matplotlib.pyplot as plt

names = [n for n, _ in ranking]
pts   = [p for _, p in ranking]

# Cumulative points race by race for top 3
top3 = names[:3]
cum  = {n: [] for n in top3}
running = {n: 0 for n in top3}
for track in TRACKS:
    for r in season[track]:
        if r['driver'] in running:
            running[r['driver']] += r['points']
    for n in top3:
        cum[n].append(running[n])

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].bar(names, pts, color='navy')
axes[0].set_title('Final points')
axes[0].tick_params(axis='x', rotation=30)

for n in top3:
    axes[1].plot(range(1, len(TRACKS) + 1), cum[n], marker='o', label=n)
axes[1].set_title('Top 3 evolution')
axes[1].set_xlabel('Race')
axes[1].set_ylabel('Cumulative points')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

fig.suptitle(f'🏆 F1 Championship — Champion: {champion}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

dashboard_done = True