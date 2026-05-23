---
## 📖 Lesson 1 — `for` with a list: one item at a time

Like Scratch's **"for each item in list"** block.

```python
for pokemon in ["Pikachu", "Salameche", "Carapuce"]:
    print(pokemon)
```

> Python reads: "For each `pokemon` in this list, print it."
> The loop body runs **once per item** — 3 items = 3 runs.

You can loop over any list:

```python
team = ["Pikachu", "Charizard", "Mewtwo"]
for p in team:
    print(f"  ⭐ {p} is ready to battle!")