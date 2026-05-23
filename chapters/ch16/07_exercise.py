import matplotlib.pyplot as plt

races   = list(range(1, 11))
max_evo = [25, 50, 75, 100, 118, 143, 168, 193, 218, 243]
lec_evo = [18, 33, 51, 76,  94, 119, 137, 162, 180, 205]
max_wins, lec_wins = 12, 3

# TODO: build a 1x2 figure — fig, axes = plt.subplots(1, 2, figsize=(11, 4))
fig, axes = ???

# Left: bar chart of wins
axes[0].bar(['Verstappen', 'Leclerc'], [max_wins, lec_wins], color=['navy', 'red'])
axes[0].set_title('Wins')

# Right: line chart of evolution
axes[1].plot(races, max_evo, marker='o', color='navy', label='Verstappen')
axes[1].plot(races, lec_evo, marker='s', color='red',  label='Leclerc')
axes[1].set_title('Championship evolution')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

fig.suptitle('Verstappen vs Leclerc')
plt.tight_layout()
plt.show()

n_subplots = len(axes)
print(f'Number of subplots: {n_subplots}')