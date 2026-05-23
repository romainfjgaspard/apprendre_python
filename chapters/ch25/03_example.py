%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(6, 5))
plt.subplots_adjust(bottom=0.25)

x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))
ax.set_title('Play with the slider!')

ax_freq = plt.axes([0.2, 0.05, 0.6, 0.04])
slider  = Slider(ax_freq, 'Frequency', 0.5, 5.0, valinit=1.0)

def update(val):
    line.set_ydata(np.sin(slider.val * x))
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()