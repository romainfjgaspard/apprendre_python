import random

events = [
    ('🌧️ Rain starts',       0.10),
    ('🚨 Safety car',        0.05),
    ('💥 Puncture',          0.03),
    ('⚡ Fastest lap',        0.15),
    ('☀️ Clear lap',         0.67),
]

def random_event():
    r = random.random()  # number between 0 and 1
    cum = 0
    for label, prob in events:
        cum += prob
        if r <= cum:
            return label
    return events[-1][0]

random.seed(0)
for lap in range(1, 11):
    print(f'Lap {lap:>2}: {random_event()}')