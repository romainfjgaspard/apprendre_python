---
## 📖 Lesson 2 — json.loads(): JSON text → Python

`json.loads()` converts a JSON string back into Python data:

```python
import json

json_text = '{"name": "Ash", "badges": 3}'
data = json.loads(json_text)

print(data["name"])    # Ash
print(data["badges"])  # 3
print(type(data))      # <class 'dict'>
```

> Memory trick: `dumps` = dump to **S**tring / `loads` = load from **S**tring.

---
### ⚠️ `open()` for reading — Python local only

```python
# This works on your computer, NOT in the browser:
with open("file.txt", "r") as f:
    content = f.read()
```

Use variables and `json.loads()` in the browser instead.