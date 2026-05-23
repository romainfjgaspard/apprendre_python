---
## 📖 Lesson 3 — JSON: Save and load game data

JSON is perfect for saving dicts and lists.

```python
import json

# Save
with open("data.json", "w") as f:
    json.dump(my_dict, f)

# Load
with open("data.json", "r") as f:
    loaded = json.load(f)
```