import matplotlib.pyplot as plt

races = list(range(1, 11))  # 10 races
max_pts  = [25, 50, 75, 100, 118, 143, 168, 193, 218, 243]
lec_pts  = [18, 33, 51, 76,  94, 119, 137, 162, 180, 205]
nor_pts  = [15, 33, 58, 83, 108, 126, 144, 169, 187, 212]

plt.figure(figsize=(9, 5))
plt.plot(races, max_pts, marker='o', color='navy',   label='Verstappen')
plt.plot(races, lec_pts, marker='s', color='red',    label='Leclerc')
plt.plot(races, nor_pts, marker='^', color='orange', label='Norris')

plt.title('Championship Evolution')
plt.xlabel('Race')
plt.ylabel('Cumulative points')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()