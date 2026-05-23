---
## 📖 Leçon 2 — `sorted()` avec `key` et `lambda`

Si ta liste contient des **dictionnaires**, tu dois dire à Python sur quoi trier.
`lambda` est une mini-fonction en une seule ligne :
```python
sorted(drivers, key=lambda d: d['points'])
# signifie : pour chaque pilote d, utilise d['points'] pour trier
```
