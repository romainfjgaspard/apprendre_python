---
## 📖 Lesson 3 — Round-trip: save and reload your data

The full pattern: convert to JSON text, then load it back.

```python
import json

# Save: Python → JSON string
save_data = {"trainer": "Ash", "xp": 150, "badges": ["Boulder", "Cascade"]}
saved = json.dumps(save_data, indent=2)
print("Saved:", saved)

# Load: JSON string → Python
loaded = json.loads(saved)
print("Trainer:", loaded["trainer"])
print("Badges:", loaded["badges"])
print("Same?", loaded == save_data)   # True!
```

---
### ⚠️ json.dump / json.load — Python local only

```python
# These use files — not available in the browser:
with open("save.json", "w") as f:
    json.dump(save_data, f)      # ⚠️ Python local only!

with open("save.json", "r") as f:
    loaded = json.load(f)        # ⚠️ Python local only!
```

In the browser: `json.dumps()` / `json.loads()` with strings instead.