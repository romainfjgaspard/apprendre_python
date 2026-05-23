---
## 📖 Leçon 1 — Une liste dans une liste

Une grille de départ F1 a 2 voitures par rangée. On peut la modéliser ainsi :
```python
grid = [
    ["Verstappen", "Leclerc"],   # rangée 1 (pole position)
    ["Norris",     "Sainz"],     # rangée 2
    ["Hamilton",   "Russell"],   # rangée 3
]
```
On accède avec **deux** indices : `grid[0][1]` → `"Leclerc"`.
