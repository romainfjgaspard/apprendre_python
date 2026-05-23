---
## 📖 Lesson 2 — `sorted()` with `key` and `lambda`

If your list contains **dictionaries**, you must tell Python what to sort by.
`lambda` is a mini-function on one line:
```python
sorted(drivers, key=lambda d: d['points'])
# means: for each driver d, use d['points'] to sort
```