---
## 📖 Leçon 2 — Compréhension de liste

Au lieu d'écrire une boucle `for` pour construire une liste, tu peux le faire en **une seule ligne** :
```python
# Longue façon :
squares = []
for x in range(5):
    squares.append(x * x)

# Façon courte (compréhension) :
squares = [x * x for x in range(5)]
```
Les deux donnent `[0, 1, 4, 9, 16]`.
