%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 25
SIZE = 100
np.random.seed(3)
pos = np.random.uniform(10, 90, size=(N, 2))
vel = np.random.uniform(-2, 2, size=(N, 2))

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, SIZE)
ax.set_ylim(0, SIZE)
ax.set_title('🐟 Bouncing aquarium')
scatter = ax.scatter(pos[:, 0], pos[:, 1], s=50, c='teal')

def update(frame):
    global pos, vel
    pos += vel
    # TODO: for each axis (0 and 1):
    #   where pos < 0, set pos to 0 and reverse vel
    #   where pos > SIZE, set pos to SIZE and reverse vel
    # Hint: use numpy boolean indexing:
    #   mask = pos[:, 0] < 0
    #   vel[mask, 0] *= -1
    #   pos[mask, 0] = 0
    ???
    scatter.set_offsets(pos)
    return scatter,

ani = FuncAnimation(fig, update, frames=300, interval=50, blit=True)
plt.show()

# Check (run after animation completes)
bounce_anim_created = True
n_dots_anim = N