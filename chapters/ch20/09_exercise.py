import numpy as np
np.random.seed(42)

N = 20
SIZE = 100

# Random positions (N, 2) between 0 and SIZE
pos = np.random.uniform(0, SIZE, size=(N, 2))
# Random velocities between -2 and 2
vel = np.random.uniform(-2, 2, size=(N, 2))

# TODO: move 100 steps — each step: pos = (pos + vel) % SIZE
for _ in range(100):
    pos = ???

all_inside = bool(np.all((pos >= 0) & (pos <= SIZE)))
n_dots = len(pos)
print(f'{n_dots} dots, all inside: {all_inside}')
print(f'First dot at: ({pos[0, 0]:.1f}, {pos[0, 1]:.1f})')