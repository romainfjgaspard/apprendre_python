%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 30
SIZE = 100
np.random.seed(42)
pos = np.random.uniform(10, 90, size=(N, 2))
vel = np.random.uniform(-2, 2, size=(N, 2))

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, SIZE)
ax.set_ylim(0, SIZE)
ax.set_title('🐟 Aquarium — 30 dots')
scatter = ax.scatter(pos[:, 0], pos[:, 1], s=40, c='blue')

def update(frame):
    global pos
    pos = (pos + vel) % SIZE
    scatter.set_offsets(pos)
    return scatter,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()