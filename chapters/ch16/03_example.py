import matplotlib.pyplot as plt

drivers = ['Verstappen', 'Leclerc', 'Norris', 'Sainz', 'Hamilton', 'Russell']
wins    = [12, 3, 4, 1, 2, 1]
podiums = [18, 9, 11, 5, 7, 4]
points  = [410, 280, 350, 220, 190, 175]
races   = list(range(1, 11))
evol    = [25, 50, 75, 100, 125, 150, 175, 200, 220, 243]

fig, axes = plt.subplots(2, 2, figsize=(11, 7))

axes[0, 0].bar(drivers, wins, color='gold')
axes[0, 0].set_title('🥇 Wins')
axes[0, 0].tick_params(axis='x', rotation=30)

axes[0, 1].bar(drivers, podiums, color='silver')
axes[0, 1].set_title('🏆 Podiums')
axes[0, 1].tick_params(axis='x', rotation=30)

axes[1, 0].bar(drivers, points, color='navy')
axes[1, 0].set_title('⭐ Points')
axes[1, 0].tick_params(axis='x', rotation=30)

axes[1, 1].plot(races, evol, marker='o', color='red')
axes[1, 1].set_title('📈 Verstappen evolution')
axes[1, 1].set_xlabel('Race')
axes[1, 1].grid(True, alpha=0.3)

fig.suptitle('🏎️  F1 Season Dashboard', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()