---
## 📖 Lesson 1 — Write to a file

```python
with open("file.txt", "w") as f:   # "w" = write mode
    f.write("Hello!\n")
```

- `"w"` = **write** (creates or overwrites the file)
- `"a"` = **append** (adds to the end)
- `with` automatically closes the file when done