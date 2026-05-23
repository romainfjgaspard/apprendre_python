---
## ⭐ Bonus — `range()` with start, stop and step

`range()` can take 2 or 3 arguments for more control:

```python
range(1, 6)      # 1, 2, 3, 4, 5  (start=1, stop=6, not included)
range(0, 10, 2)  # 0, 2, 4, 6, 8  (count by 2)
range(5, 0, -1)  # 5, 4, 3, 2, 1  (count down!)
```

| Call | Result |
|------|--------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -2)` | 10, 8, 6, 4, 2 |