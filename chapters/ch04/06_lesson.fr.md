---
## 📖 Leçon 3 — `range()` : le raccourci

Écrire `[0, 1, 2, 3, 4]` à chaque fois, c'est long. `range(5)` fait exactement la même chose !

```python
for i in range(5):   # identique à [0, 1, 2, 3, 4]
    print(i)
```

> `range(n)` génère les nombres **0 à n−1** (n valeurs, en partant de 0).
> `range(5)` → 0, 1, 2, 3, 4

| Liste manuelle | Raccourci `range()` |
|----------------|---------------------|
| `[0, 1, 2, 3, 4]` | `range(5)` |
| `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` | `range(10)` |
| `[0, 1]` | `range(2)` |
