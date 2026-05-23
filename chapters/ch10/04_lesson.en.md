---
## 📖 Lesson 2 — List comprehension

Instead of writing a `for` loop to build a list, you can do it in **one line**:
```python
# Long way:
squares = []
for x in range(5):
    squares.append(x * x)

# Short way (comprehension):
squares = [x * x for x in range(5)]
```
Both give `[0, 1, 4, 9, 16]`.