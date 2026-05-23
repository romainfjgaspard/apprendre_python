---
## 📖 Lesson 1 — json.dumps(): Python → JSON text

`json.dumps()` converts Python data into a JSON **string** you can store or send anywhere:

```python
import json

data = {"name": "Ash", "badges": 3, "team": ["Pikachu", "Charizard"]}
json_text = json.dumps(data, indent=2)
print(json_text)
print(type(json_text))   # <class 'str'>
```

> `indent=2` makes the output nicely formatted. Without it, it's one long line.

---
### ⚠️ `open()` — Python local only (PyCharm, terminal)

```python
# This works on your computer, NOT in the browser:
with open("file.txt", "w") as f:
    f.write("Hello!\n")
```

Use `json.dumps()` instead when coding in the browser.