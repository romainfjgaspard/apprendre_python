---
## 📖 Lesson 4 — List comprehensions (magic one-liners!)

Create a new list by transforming or filtering another list.

```python
# Old way:
result = []
for x in items:
    result.append(x * 2)

# List comprehension:
result = [x * 2 for x in items]
```