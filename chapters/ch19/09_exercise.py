import random
random.seed(7)

WIDTH, HEIGHT = 100, 100

class Dot:
    def __init__(self, x, y, vx, vy):
        self.x, self.y   = x, y
        self.vx, self.vy = vx, vy
        self.bounces     = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # TODO: if x is out of [0, WIDTH], reverse vx AND add 1 to self.bounces
        ???
        # TODO: same for y and HEIGHT
        ???

dots = [Dot(random.uniform(10, 90), random.uniform(10, 90),
            random.uniform(-4, 4), random.uniform(-4, 4))
        for _ in range(10)]

# Run 200 steps
for _ in range(200):
    for d in dots:
        d.move()

total_bounces = sum(d.bounces for d in dots)
n_dots = len(dots)
print(f'{n_dots} dots, {total_bounces} total bounces after 200 steps')