---
## 📖 Lesson 1 — Your first class

```python
class Pokemon:
    def __init__(self, name, hp, attack):
        self.name   = name
        self.hp     = hp
        self.attack = attack
```
- `class` = keyword to create a blueprint
- `__init__` = runs when you create a new Pokémon
- `self` = "this object" (Scratch: "this sprite")