import numpy as np
import matplotlib.pyplot as plt

W, H = 100, 100
FLEE_RADIUS = 25

def flee_from_predator(boid, predator, radius=FLEE_RADIUS):
    diff = boid.pos - predator.pos
    dist = np.linalg.norm(diff)
    if dist < radius and dist > 0:
        return 2.0 * diff / dist  # strong push away
    return np.array([0.0, 0.0])

np.random.seed(42)
flock = [Boid(np.random.uniform(20, 80), np.random.uniform(20, 80),
              np.random.uniform(-2, 2), np.random.uniform(-2, 2))
         for _ in range(30)]
pred = Predator(50, 50, 0, 0)

# Simulate 100 steps
for _ in range(100):
    # Predator chases nearest boid
    nearest = min(flock, key=lambda b: np.linalg.norm(b.pos - pred.pos))
    pred.chase(nearest)
    pred.move(W, H)
    # Boids flee from predator
    for b in flock:
        flee = flee_from_predator(b, pred)
        b.vel += flee * 0.1
        speed = np.linalg.norm(b.vel)
        if speed > 4:
            b.vel = b.vel / speed * 4
        b.move(W, H)

# Plot
fig, ax = plt.subplots(figsize=(6, 6))
for b in flock:
    ax.annotate('', xy=b.pos + b.vel, xytext=b.pos,
                arrowprops=dict(arrowstyle='->', color='teal', lw=1.2))
ax.plot(*pred.pos, 'r^', markersize=15, label='Predator')
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.set_title('🦅 Predator chasing boids')
ax.legend()
plt.show()