import matplotlib.pyplot as plt
import random

random.seed(42)
dots = [Dot(random.uniform(10, 90), random.uniform(10, 90),
            random.uniform(-3, 3), random.uniform(-3, 3))
        for _ in range(20)]

# Move 50 steps
for _ in range(50):
    for d in dots:
        d.move()

# Plot final positions
xs = [d.x for d in dots]
ys = [d.y for d in dots]
plt.figure(figsize=(5, 5))
plt.scatter(xs, ys, s=80, c='blue', edgecolor='black')
plt.xlim(0, WIDTH)
plt.ylim(0, HEIGHT)
plt.title('20 dots after 50 steps')
plt.grid(True, alpha=0.3)
plt.show()