import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
W, H = 100, 100
N = 30

# TODO: create N Boid objects
flock = ???

# Move 100 steps
for _ in range(100):
    for b in flock:
        b.move(W, H)

# Plot
xs  = [b.pos[0] for b in flock]
ys  = [b.pos[1] for b in flock]
vxs = [b.vel[0] for b in flock]
vys = [b.vel[1] for b in flock]

plt.figure(figsize=(5, 5))
plt.quiver(xs, ys, vxs, vys, color='teal', scale=50)
plt.xlim(0, W)
plt.ylim(0, H)
plt.title(f'🐦 {N} Boids after 100 steps')
plt.show()

n_boids = len(flock)
all_inside = all(0 <= b.pos[0] <= W and 0 <= b.pos[1] <= H for b in flock)