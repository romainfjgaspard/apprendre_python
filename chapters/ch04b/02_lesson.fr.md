---
## 📖 Leçon 1 — `while` : répéter tant qu'une condition est True

```python
while condition:
    # s'exécute tant que la condition est True
    # DOIT changer quelque chose pour finir par devenir False !
```

Exemple — combat Pokémon :

```python
enemy_hp = 100
my_attack = 25

while enemy_hp > 0:
    enemy_hp = enemy_hp - my_attack
    print(f"  Touché ! HP ennemi : {enemy_hp}")

print("🏆 L'ennemi s'est évanoui !")
```

> ⚠️ Si la condition ne devient **jamais** False, tu obtiens une **boucle infinie** — le programme se bloque !
> Assure-toi que quelque chose change à l'intérieur de la boucle.
