import numpy as np

def get_neighbours(boid, flock, radius):
    """Return list of boids within `radius` distance."""
    neighbours = []
    for other in flock:
        if other is boid:
            continue
        dist = np.linalg.norm(boid.pos - other.pos)
        if dist < radius:
            neighbours.append(other)
    return neighbours

# Test with 5 boids
np.random.seed(0)
flock = [Boid(np.random.uniform(0, 100), np.random.uniform(0, 100),
              np.random.uniform(-2, 2), np.random.uniform(-2, 2))
         for _ in range(5)]

n = get_neighbours(flock[0], flock, radius=40)
print(f'Boid 0 has {len(n)} neighbours within radius 40')