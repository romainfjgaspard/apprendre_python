drivers_20 = [
    "Verstappen", "Leclerc", "Norris", "Sainz", "Hamilton",
    "Russell", "Alonso", "Stroll", "Gasly", "Ocon",
    "Albon", "Sargeant", "Hülkenberg", "Magnussen", "Tsunoda",
    "Ricciardo", "Bottas", "Zhou", "Piastri", "Pérez",
]

# TODO: build a list of 10 rows, each row = [drivers_20[i*2], drivers_20[i*2+1]]
# Use a list comprehension with range(10)
grid = ???

# Show the result
for i, row in enumerate(grid):
    print(f"Row {i+1:>2}: {row[0]:<12} {row[1]}")

# How many rows?
n_rows = len(grid)
print(f"\nTotal rows: {n_rows}")