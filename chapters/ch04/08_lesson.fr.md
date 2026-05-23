---
## ⭐ Bonus — `range()` avec début, fin et pas

`range()` accepte 2 ou 3 arguments pour plus de contrôle :

```python
range(1, 6)      # 1, 2, 3, 4, 5  (début=1, fin=6, non incluse)
range(0, 10, 2)  # 0, 2, 4, 6, 8  (compter par 2)
range(5, 0, -1)  # 5, 4, 3, 2, 1  (compter à rebours !)
```

| Appel | Résultat |
|-------|----------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 |
