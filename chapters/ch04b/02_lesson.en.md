---
## 📖 Lesson 1 — `while`: repeat as long as a condition is True

```python
while condition:
    # runs while condition is True
    # MUST change something to eventually make it False!
```

Example — Pokémon battle:

```python
enemy_hp = 100
my_attack = 25

while enemy_hp > 0:
    enemy_hp = enemy_hp - my_attack
    print(f"  Hit! Enemy HP: {enemy_hp}")

print("🏆 Enemy fainted!")
```

> ⚠️ If the condition **never** becomes False, you get an **infinite loop** — the program freezes!
> Always make sure something inside the loop changes the condition.
