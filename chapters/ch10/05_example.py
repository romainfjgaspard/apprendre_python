drivers = ["Verstappen", "Leclerc", "Norris", "Sainz", "Hamilton"]

# Long way
upper1 = []
for d in drivers:
    upper1.append(d.upper())
print(upper1)

# Short way (comprehension)
upper2 = [d.upper() for d in drivers]
print(upper2)

# Filter: only short names (≤ 6 letters)
short = [d for d in drivers if len(d) <= 6]
print("Short names:", short)