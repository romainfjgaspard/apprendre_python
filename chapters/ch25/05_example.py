%matplotlib notebook
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_title('Click anywhere!')
dot, = ax.plot(50, 50, 'ro', markersize=15)

def on_click(event):
    if event.inaxes == ax:
        dot.set_data([event.xdata], [event.ydata])
        ax.set_title(f'Clicked at ({event.xdata:.0f}, {event.ydata:.0f})')
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()