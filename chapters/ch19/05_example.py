WIDTH, HEIGHT = 100, 100

class Dot:
    def __init__(self, x, y, vx, vy):
        self.x, self.y   = x, y
        self.vx, self.vy = vx, vy

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # Bounce!
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

d = Dot(95, 50, 3, 2)
for step in range(10):
    d.move()
    print(f'Step {step+1}: ({d.x:.0f}, {d.y:.0f})  vel=({d.vx}, {d.vy})')