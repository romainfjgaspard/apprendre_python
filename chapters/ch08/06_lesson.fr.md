---
## 📖 Leçon 3 — Aller-retour : sauvegarder et recharger tes données

Le schéma complet : convertir en texte JSON, puis recharger.

```python
import json

# Sauvegarder : Python → chaîne JSON
save_data = {"trainer": "Ash", "xp": 150, "badges": ["Rocher", "Cascade"]}
saved = json.dumps(save_data, indent=2)
print("Sauvegardé :", saved)

# Charger : chaîne JSON → Python
loaded = json.loads(saved)
print("Dresseur :", loaded["trainer"])
print("Badges :", loaded["badges"])
print("Identiques ?", loaded == save_data)   # True !
```

---
### ⚠️ json.dump / json.load — Python local uniquement

```python
# Ces fonctions utilisent des fichiers — non disponible dans le navigateur :
with open("save.json", "w") as f:
    json.dump(save_data, f)      # ⚠️ Python local uniquement !

with open("save.json", "r") as f:
    loaded = json.load(f)        # ⚠️ Python local uniquement !
```

Dans le navigateur : utilise `json.dumps()` / `json.loads()` avec des chaînes.
