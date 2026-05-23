grid = [
    ["Verstappen", "Leclerc"],
    ["Norris",     "Sainz"],
    ["Hamilton",   "Russell"],
]

print("Before overtake — P2:", grid[0][1], "| P3:", grid[1][0])

# Norris (P3) overtakes Leclerc (P2)
grid[0][1], grid[1][0] = grid[1][0], grid[0][1]

print("After overtake  — P2:", grid[0][1], "| P3:", grid[1][0])