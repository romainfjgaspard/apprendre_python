%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

W, H = 100, 100
N = 30
np.random.seed(42)

# Reuse Boid class from chapter 22
class Boid:
    def __init__(self, x, y, vx, vy):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)
    def move(self, w, h):
        self.pos += self.vel
        for i, lim in enumerate([w, h]):
            if self.pos[i] < 0: self.pos[i] = 0; self.vel[i] *= -1
            elif self.pos[i] > lim: self.pos[i] = lim; self.vel[i] *= -1

flock = [Boid(np.random.uniform(10, 90), np.random.uniform(10, 90),
              np.random.uniform(-2, 2), np.random.uniform(-2, 2))
         for _ in range(N)]

fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(bottom=0.15)
ax.set_xlim(0, W); ax.set_ylim(0, H)
scatter = ax.scatter([b.pos[0] for b in flock],
                     [b.pos[1] for b in flock], s=30, c='teal')

ax_radius = plt.axes([0.2, 0.03, 0.6, 0.03])
radius_slider = Slider(ax_radius, 'Radius', 5, 50, valinit=20)

def get_neighbours(boid, flock, radius):
    return [b for b in flock if b is not boid
            and np.linalg.norm(b.pos - boid.pos) < radius]

def update(frame):
    r = radius_slider.val
    for b in flock:
        nbs = get_neighbours(b, flock, r)
        if nbs:
            centre = np.mean([n.pos for n in nbs], axis=0)
            b.vel += 0.02 * (centre - b.pos)  # cohesion
            avg_vel = np.mean([n.vel for n in nbs], axis=0)
            b.vel += 0.05 * (avg_vel - b.vel)  # alignment
            for n in nbs:
                diff = b.pos - n.pos
                d = np.linalg.norm(diff)
                if d < 10 and d > 0:
                    b.vel += 0.5 * diff / d  # separation
        sp = np.linalg.norm(b.vel)
        if sp > 4: b.vel = b.vel / sp * 4
        b.move(W, H)
    scatter.set_offsets(np.array([b.pos for b in flock]))
    return scatter,

ani = FuncAnimation(fig, update, frames=500, interval=50, blit=True)
plt.show()

interactive_done = True
slider_exists = True