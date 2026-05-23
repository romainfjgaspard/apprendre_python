import random

# Roll a die
for _ in range(5):
    print('🎲', random.randint(1, 6))

# Pick a random circuit
tracks = ['Monaco', 'Silverstone', 'Monza', 'Spa', 'Suzuka']
print('\nNext race:', random.choice(tracks))