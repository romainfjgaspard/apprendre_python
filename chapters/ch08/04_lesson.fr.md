---
## 📖 Leçon 2 — json.loads() : texte JSON → Python

`json.loads()` convertit une chaîne JSON en données Python :

```python
import json

json_text = '{"name": "Ash", "badges": 3}'
data = json.loads(json_text)

print(data["name"])    # Ash
print(data["badges"])  # 3
print(type(data))      # <class 'dict'>
```

> Astuce : `dumps` = sauvegarder en **S**tring / `loads` = charger depuis une **S**tring.

---
### ⚠️ `open()` pour lire — Python local uniquement

```python
# Ceci fonctionne sur ton ordinateur, PAS dans le navigateur :
with open("fichier.txt", "r") as f:
    contenu = f.read()
```

Dans le navigateur, utilise des variables et `json.loads()` à la place.
