import numpy as np
import time

N = 100_000

# Python loop
py_x = list(range(N))
t0 = time.time()
py_r = [x * 2 + 1 for x in py_x]
py_time = time.time() - t0

# numpy
np_x = np.arange(N)
t0 = time.time()
np_r = np_x * 2 + 1
np_time = time.time() - t0

print(f'Python loop: {py_time*1000:.1f} ms')
print(f'numpy:       {np_time*1000:.1f} ms')
print(f'numpy is {py_time/np_time:.0f}x faster!')