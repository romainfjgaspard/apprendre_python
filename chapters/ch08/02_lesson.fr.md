---
## 📖 Leçon 1 — Écrire dans un fichier

```python
with open("fichier.txt", "w") as f:   # "w" = mode écriture
    f.write("Bonjour !\n")
```

- `"w"` = **write** (crée ou écrase le fichier)
- `"a"` = **append** (ajoute à la fin)
- `with` ferme automatiquement le fichier quand c'est terminé
