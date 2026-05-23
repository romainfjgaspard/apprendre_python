---
## 📖 Leçon 1 — `for` sur une liste : un élément à la fois

Comme le bloc **"pour chaque élément de la liste"** de Scratch.

```python
for pokemon in ["Pikachu", "Salameche", "Carapuce"]:
    print(pokemon)
```

> Python lit : "Pour chaque `pokemon` dans cette liste, affiche-le."
> Le corps de la boucle s'exécute **une fois par élément** — 3 éléments = 3 tours.

Tu peux parcourir n'importe quelle liste :

```python
team = ["Pikachu", "Charizard", "Mewtwo"]
for p in team:
    print(f"  ⭐ {p} est prêt au combat !")
