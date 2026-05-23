import numpy as np

class Boid:
    def __init__(self, x, y, vx, vy):
        self.pos = np.array([x, y], dtype=float)
        self.vel = np.array([vx, vy], dtype=float)

    def move(self, w, h):
        self.pos += self.vel
        for i, limit in enumerate([w, h]):
            if self.pos[i] < 0:
                self.pos[i] = 0; self.vel[i] *= -1
            elif self.pos[i] > limit:
                self.pos[i] = limit; self.vel[i] *= -1

class Predator(Boid):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy)
        self.is_predator = True

    def chase(self, target):
        direction = target.pos - self.pos
        dist = np.linalg.norm(direction)
        if dist > 0:
            self.vel += 0.05 * direction / dist

p = Predator(10, 10, 1, 1)
prey = Boid(80, 80, 0, 0)
print(f'Predator at {p.pos}, prey at {prey.pos}')
for _ in range(20):
    p.chase(prey)
    p.move(100, 100)
print(f'Predator at ({p.pos[0]:.0f}, {p.pos[1]:.0f}) — getting closer!')