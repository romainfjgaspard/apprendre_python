import matplotlib.pyplot as plt

drivers = ['Verstappen', 'Norris', 'Leclerc', 'Sainz', 'Hamilton']
points  = [410, 350, 280, 220, 190]
colors  = ['navy', 'orange', 'red', 'red', 'silver']

plt.figure(figsize=(8, 4))
plt.bar(drivers, points, color=colors)
plt.title('🏆 Drivers Championship — Top 5')
plt.ylabel('Points')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()