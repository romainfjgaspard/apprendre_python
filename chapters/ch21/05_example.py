%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 40
SIZE = 100
np.random.seed(7)
pos = np.random.uniform(5, 95, size=(N, 2))
vel = np.random.uniform(-3, 3, size=(N, 2))

# Speed = length of velocity vector
speeds = np.sqrt(vel[:, 0]**2 + vel[:, 1]**2)

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, SIZE)
ax.set_ylim(0, SIZE)
ax.set_title('Speed = colour 🌈')
scatter = ax.scatter(pos[:, 0], pos[:, 1], s=50, c=speeds, cmap='hot', edgecolor='gray')
plt.colorbar(scatter, label='Speed')

def update(frame):
    global pos
    pos = (pos + vel) % SIZE
    scatter.set_offsets(pos)
    return scatter,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()