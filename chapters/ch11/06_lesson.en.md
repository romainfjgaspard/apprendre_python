---
## 📖 Lesson 3 — Filter with a comprehension

Want only Ferrari drivers? Use a **list comprehension** with `if`:
```python
ferrari = [d for d in standings if d['team'] == 'Ferrari']
```