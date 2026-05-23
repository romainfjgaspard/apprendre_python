---
## 📖 Leçon 2 — `break` : sortir d'une boucle en avance

`break` quitte immédiatement la boucle en cours — même si la condition est encore True.

```python
while True:          # bouclerait indéfiniment...
    answer = input("Devine le Pokémon : ")
    if answer == "Pikachu":
        print("✅ Correct !")
        break        # ...mais break l'arrête !
```

> Utilise `break` quand tu veux stopper une boucle dès qu'un événement précis se produit.
