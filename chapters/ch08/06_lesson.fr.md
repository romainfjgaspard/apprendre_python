---
## 📖 Leçon 3 — JSON : Sauvegarder et charger les données du jeu

JSON est parfait pour sauvegarder des dicts et des listes.

```python
import json

# Sauvegarder
with open("data.json", "w") as f:
    json.dump(mon_dict, f)

# Charger
with open("data.json", "r") as f:
    charge = json.load(f)
```
