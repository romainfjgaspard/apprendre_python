import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 20
boids = [Boid(np.random.uniform(10, 90),
              np.random.uniform(10, 90),
              np.random.uniform(-3, 3),
              np.random.uniform(-3, 3))
         for _ in range(N)]

xs  = [b.pos[0] for b in boids]
ys  = [b.pos[1] for b in boids]
vxs = [b.vel[0] for b in boids]
vys = [b.vel[1] for b in boids]

plt.figure(figsize=(5, 5))
plt.quiver(xs, ys, vxs, vys, color='navy', scale=50)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title('🐦 20 Boids')
plt.show()