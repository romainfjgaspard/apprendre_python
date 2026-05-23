---
## 📖 Lesson 1 — A list inside a list

An F1 starting grid has 2 cars per row. We can model it like this:
```python
grid = [
    ["Verstappen", "Leclerc"],   # row 1 (pole position)
    ["Norris",     "Sainz"],    # row 2
    ["Hamilton",   "Russell"], # row 3
]
```
Access with **two** indices: `grid[0][1]` → `"Leclerc"`.