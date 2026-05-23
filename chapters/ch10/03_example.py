grid = [
    ["Verstappen", "Leclerc"],
    ["Norris",     "Sainz"],
    ["Hamilton",   "Russell"],
    ["Alonso",     "Stroll"],
]

print("🏁 Pole position:", grid[0][0])
print("🏁 P2:           ", grid[0][1])
print("🏁 Row 3 left:   ", grid[2][0])
print("\nFull grid:")
for i, row in enumerate(grid):
    print(f"  Row {i+1}: {row[0]:<12} {row[1]}")