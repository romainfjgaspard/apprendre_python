class Dot:
    def __init__(self, x, y, vx, vy):
        self.x  = x
        self.y  = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def __str__(self):
        return f'Dot at ({self.x:.1f}, {self.y:.1f})'

d = Dot(0, 0, 1.5, 2.0)
for step in range(5):
    d.move()
    print(d)