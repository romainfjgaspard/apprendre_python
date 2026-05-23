---
## 📖 Lesson 2 — `break`: escape a loop early

`break` immediately exits the current loop — even if the condition is still True.

```python
while True:          # would loop forever...
    answer = input("Guess the Pokémon: ")
    if answer == "Pikachu":
        print("✅ Correct!")
        break        # ...but break stops it!
```

> Use `break` when you want to stop a loop as soon as something specific happens.
