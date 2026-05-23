import numpy as np

class Boid:
    def __init__(self, x, y, vx, vy):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)

    def move(self, width, height):
        self.pos += self.vel
        # Bounce off walls
        for i, limit in enumerate([width, height]):
            if self.pos[i] < 0:
                self.pos[i] = 0
                self.vel[i] *= -1
            elif self.pos[i] > limit:
                self.pos[i] = limit
                self.vel[i] *= -1

    def speed(self):
        return np.linalg.norm(self.vel)

b = Boid(50, 50, 2, -1)
for _ in range(5):
    b.move(100, 100)
    print(f'pos=({b.pos[0]:.0f},{b.pos[1]:.0f})  speed={b.speed():.1f}')