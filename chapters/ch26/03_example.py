import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

W, H = 200, 200
N = 50
RADIUS = 25
MAX_SPEED = 4
np.random.seed(42)

class Boid:
    def __init__(self, x, y, vx, vy):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)

    def move(self):
        self.pos += self.vel
        for i, lim in enumerate([W, H]):
            if self.pos[i] < 0: self.pos[i] = 0; self.vel[i] *= -1
            elif self.pos[i] > lim: self.pos[i] = lim; self.vel[i] *= -1

class Predator(Boid):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0)
        self.max_speed = 5

    def hunt(self, flock):
        if not flock: return
        nearest = min(flock, key=lambda b: np.linalg.norm(b.pos - self.pos))
        diff = nearest.pos - self.pos
        dist = np.linalg.norm(diff)
        if dist > 0:
            self.vel += 0.08 * diff / dist
        sp = np.linalg.norm(self.vel)
        if sp > self.max_speed:
            self.vel = self.vel / sp * self.max_speed

flock = [Boid(np.random.uniform(20, W-20), np.random.uniform(20, H-20),
              np.random.uniform(-2, 2), np.random.uniform(-2, 2))
         for _ in range(N)]
pred = Predator(W/2, H/2)

print(f'{N} boids + 1 predator ready!')