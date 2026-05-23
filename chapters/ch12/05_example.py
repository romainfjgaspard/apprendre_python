import random
random.seed(42)
print([random.randint(1, 100) for _ in range(5)])

random.seed(42)  # same seed → same numbers
print([random.randint(1, 100) for _ in range(5)])