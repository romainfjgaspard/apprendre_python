---
## 📖 Leçon 1 — json.dumps() : Python → texte JSON

`json.dumps()` convertit des données Python en **chaîne** JSON que tu peux stocker ou envoyer :

```python
import json

data = {"name": "Ash", "badges": 3, "team": ["Pikachu", "Charizard"]}
json_text = json.dumps(data, indent=2)
print(json_text)
print(type(json_text))   # <class 'str'>
```

> `indent=2` formate joliment le résultat. Sans lui, tout est sur une seule ligne.

---
### ⚠️ `open()` — Python local uniquement (PyCharm, terminal)

```python
# Ceci fonctionne sur ton ordinateur, PAS dans le navigateur :
with open("fichier.txt", "w") as f:
    f.write("Bonjour !\n")
```

Utilise `json.dumps()` à la place quand tu codes dans le navigateur.
