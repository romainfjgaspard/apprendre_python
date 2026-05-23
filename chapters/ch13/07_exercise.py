import matplotlib.pyplot as plt
import random

random.seed(3)
n_laps    = 20
lap_times = [random.uniform(79.0, 82.0) for _ in range(n_laps)]
lap_nums  = list(range(1, n_laps + 1))

# TODO: build the chart — use plt.plot, plt.title, plt.xlabel, plt.ylabel
???

fastest = min(lap_times)
slowest = max(lap_times)
average = sum(lap_times) / len(lap_times)
print(f'Fastest: {fastest:.2f}s  |  Slowest: {slowest:.2f}s  |  Average: {average:.2f}s')