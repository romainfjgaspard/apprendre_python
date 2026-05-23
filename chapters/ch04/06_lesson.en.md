---
## 📖 Lesson 3 — `range()`: the shortcut

Writing `[0, 1, 2, 3, 4]` every time is tedious. `range(5)` does the same thing!

```python
for i in range(5):   # same as [0, 1, 2, 3, 4]
    print(i)
```

> `range(n)` generates numbers **0 to n−1** (n values, starting from 0).
> `range(5)` → 0, 1, 2, 3, 4

| Manual list | `range()` shortcut |
|-------------|-------------------|
| `[0, 1, 2, 3, 4]` | `range(5)` |
| `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` | `range(10)` |
| `[0, 1]` | `range(2)` |