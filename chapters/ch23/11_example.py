import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

W, H = 100, 100
N = 40
RADIUS = 20
MAX_SPEED = 4

# Weights for each rule
W_SEP = 1.5   # separation
W_ALI = 1.0   # alignment
W_COH = 0.5   # cohesion

np.random.seed(42)
flock = [Boid(np.random.uniform(20, 80), np.random.uniform(20, 80),
              np.random.uniform(-2, 2), np.random.uniform(-2, 2))
         for _ in range(N)]

def update_flock(flock):
    for b in flock:
        neighbours = get_neighbours(b, flock, RADIUS)
        force = (W_SEP * separation(b, neighbours)
               + W_ALI * alignment(b, neighbours)
               + W_COH * cohesion(b, neighbours))
        b.vel += force * 0.1
        # Limit speed
        speed = np.linalg.norm(b.vel)
        if speed > MAX_SPEED:
            b.vel = b.vel / speed * MAX_SPEED
        b.move(W, H)

# Run 200 steps and plot every 50
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, ax in enumerate(axes):
    for _ in range(50):
        update_flock(flock)
    xs  = [b.pos[0] for b in flock]
    ys  = [b.pos[1] for b in flock]
    vxs = [b.vel[0] for b in flock]
    vys = [b.vel[1] for b in flock]
    ax.quiver(xs, ys, vxs, vys, color='teal', scale=60)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_title(f'Step {(i+1)*50}')
plt.suptitle('🐦 Flocking over time', fontweight='bold')
plt.tight_layout()
plt.show()

flocking_works = True