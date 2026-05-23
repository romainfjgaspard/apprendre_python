import numpy as np

class Predator(Boid):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy)
        self.max_speed = 6  # faster than boids

    def hunt(self, flock):
        """Chase the nearest boid."""
        # TODO: find nearest boid (use min + lambda + np.linalg.norm)
        nearest = ???
        # TODO: steer towards it
        self.chase(nearest)
        # Limit speed
        speed = np.linalg.norm(self.vel)
        if speed > self.max_speed:
            self.vel = self.vel / speed * self.max_speed

    def chase(self, target):
        direction = target.pos - self.pos
        dist = np.linalg.norm(direction)
        if dist > 0:
            self.vel += 0.1 * direction / dist

np.random.seed(7)
flock = [Boid(np.random.uniform(10, 90), np.random.uniform(10, 90),
              np.random.uniform(-2, 2), np.random.uniform(-2, 2))
         for _ in range(20)]
pred = Predator(50, 50, 0, 0)

for _ in range(50):
    pred.hunt(flock)
    pred.move(100, 100)

has_hunt = hasattr(pred, 'hunt')
pred_fast = pred.max_speed > 4
print(f'Predator at ({pred.pos[0]:.0f}, {pred.pos[1]:.0f}), speed: {np.linalg.norm(pred.vel):.1f}')
print(f'hunt() exists: {has_hunt}, faster than boids: {pred_fast}')