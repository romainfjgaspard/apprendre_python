%matplotlib notebook

fig, ax = plt.subplots(figsize=(7, 7))
plt.subplots_adjust(bottom=0.22)
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.set_title('🐦 Boids Ultimate')

sc_boids = ax.scatter([b.pos[0] for b in flock],
                      [b.pos[1] for b in flock], s=20, c='teal')
sc_pred  = ax.scatter([pred.pos[0]], [pred.pos[1]], s=120, c='red',
                      marker='^', zorder=5, label='Predator')
ax.legend(loc='upper right')

ax_sep = plt.axes([0.15, 0.12, 0.3, 0.03])
ax_ali = plt.axes([0.15, 0.07, 0.3, 0.03])
ax_coh = plt.axes([0.15, 0.02, 0.3, 0.03])
ax_rad = plt.axes([0.60, 0.07, 0.3, 0.03])

sl_sep = Slider(ax_sep, 'Separation', 0, 5, valinit=1.5)
sl_ali = Slider(ax_ali, 'Alignment',  0, 5, valinit=1.0)
sl_coh = Slider(ax_coh, 'Cohesion',   0, 5, valinit=0.5)
sl_rad = Slider(ax_rad, 'Radius',     5, 60, valinit=25)

# Click to teleport predator
def on_click(event):
    if event.inaxes == ax:
        pred.pos[:] = [event.xdata, event.ydata]
        pred.vel[:] = 0

fig.canvas.mpl_connect('button_press_event', on_click)

def update(frame):
    r = sl_rad.val
    for b in flock:
        nbs = get_neighbours(b, flock, r)
        force = (sl_sep.val * separation(b, nbs)
               + sl_ali.val * alignment(b, nbs)
               + sl_coh.val * cohesion(b, nbs)
               + flee(b, pred))
        b.vel += force * 0.05
        sp = np.linalg.norm(b.vel)
        if sp > MAX_SPEED:
            b.vel = b.vel / sp * MAX_SPEED
        b.move()
    pred.hunt(flock)
    pred.move()
    sc_boids.set_offsets(np.array([b.pos for b in flock]))
    sc_pred.set_offsets(np.array([pred.pos]))
    return sc_boids, sc_pred

ani = FuncAnimation(fig, update, frames=1000, interval=40, blit=True)
plt.show()

simulation_running = True