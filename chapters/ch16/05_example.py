import matplotlib.pyplot as plt

drivers = ['Verstappen', 'Leclerc', 'Norris', 'Sainz', 'Hamilton', 'Russell']
wins    = [12, 3, 4, 1, 2, 1]
points  = [410, 280, 350, 220, 190, 175]

plt.figure(figsize=(8, 5))
plt.scatter(wins, points, s=160, c='red', edgecolor='black', zorder=3)

for w, p, name in zip(wins, points, drivers):
    plt.annotate(name, (w, p), xytext=(8, 5), textcoords='offset points')

plt.title('Wins vs Points')
plt.xlabel('Wins')
plt.ylabel('Points')
plt.grid(True, alpha=0.3)
plt.show()