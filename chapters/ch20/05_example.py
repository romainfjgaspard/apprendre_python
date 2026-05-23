import numpy as np

# 5 dots, each with (x, y)
positions = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80],
    [90, 10],
])

velocities = np.array([
    [1, 2],
    [-1, 3],
    [2, -2],
    [-3, 1],
    [0, -1],
])

# Move ALL dots in one line!
positions = positions + velocities
print('New positions:\n', positions)

# All x coordinates
print('\nAll x:', positions[:, 0])
# All y coordinates
print('All y:', positions[:, 1])