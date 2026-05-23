# ⚡ Python Quest — Learn Python by building games!

A progressive Python course for Basile (11, Scratch expert) with 3 themed seasons.

## Requirements

- **Modern browser** (Chrome, Firefox, Safari, Edge) — No installation needed!
- Optionally: Python 3.11+ (for local development only)

---

## How to play

### 🌐 Online (Recommended)

1. **Start a local server:**
   ```bash
   # Using Python
   python -m http.server 8000
   
   # OR using Node.js
   npx http-server
   
   # OR using Ruby
   ruby -run -ehttpd . -p8000
   ```

2. **Open in browser:**
   ```
   http://localhost:8000/web/index.html
   ```

3. **Create your trainer:**
   - Enter your name on splash screen
   - Choose your starter Pokémon 
   - Start learning! 🚀

### 📝 Offline (Jupyter Notebooks - Deprecated)

The old Jupyter notebooks have been removed. The web version is now the recommended way to learn.

---

## 🎮 Gameplay Overview

### Season 1 — Pokémon Edition ⚡
Master Python basics by building a battle system!

| Chapters | Topics | Project |
|----------|--------|---------|
| 1-3 | Print, variables, types, conditionals | Pokémon starter card |
| 4-5 | Loops, lists | Team management |
| 6-7 | Dictionaries, functions | Pokédex + battle engine |
| 8 | Files & JSON | Save game data |
| **Boss 1** 🏆 | Everything combined! | **Pokémon Arena Tournament** |

**Learn** : print(), variables, f-strings, types, if/elif/else, for/while loops, lists, dictionaries, functions, file I/O

### Season 2 — Formula 1 🏎️
Analyze data and build a championship simulator!

| Chapters | Topics | Project |
|----------|--------|---------|
| 10-12 | Nested lists, sorted(), lambda, random, modules | F1 grid & race sim |
| 13-14 | CSV, pandas, matplotlib | Dashboard & statistics |
| 15-16 | Advanced charts, subplots | Championship visualization |
| **Boss 2** 🏆 | Everything combined! | **Full season simulator** |

**Learn** : nested data structures, advanced sorting, data visualization, CSV/JSON, pandas DataFrames

### Season 3 — Birds Simulation 🐦
Create emergent behavior with OOP and animation!

| Chapters | Topics | Project |
|----------|--------|---------|
| 18-19 | Classes, `__init__`, methods | Moving objects |
| 20-22 | numpy arrays, animation, Boid class | Flocking basics |
| 23-24 | Flocking rules (separation, alignment, cohesion), inheritance | Predator simulation |
| 25 | Interactivity (sliders, mouse events) | Interactive sim |
| **Boss 3** 🏆 | Everything combined! | **Boids Ultimate** |

**Learn** : Object-oriented programming, numpy, matplotlib animation, inheritance, emergent systems

---

## 📊 Progression System

- **XP & Levels** : 🥚 Egg → ⚡ Pikachu → 🔥 Charizard → 🏆 Pokémon Master (8 tiers)
- **Pokémon Evolution** : Your starter evolves at key XP thresholds
- **Leaderboard** : Compete with other trainers globally (future)
- **Badges** : Earn one for each completed chapter
- **Progress** : Auto-saved to browser (future: cloud sync)

---

## 🛠️ Development

### Modifying content

Edit `web/chapters.json` to add/modify chapters:

```json
{
  "num": 1,
  "title": "⚡ Hello Pokémon",
  "xp": 50,
  "cells": [
    { "type": "md", "source": "# Your lesson here" },
    { "type": "code", "source": "print('Hello')" },
    { "type": "exercise", "source": "name = ???" },
    { "type": "verify", "source": "from _verify import verify\nverify(1, locals())" }
  ]
}
```

### Testing exercises locally

```bash
# Verify level 1
python _verify.py 1

# Run full suite (needs adjustments)
python -m pytest _verify.py
```

---

## 🚀 Deployment

### Deploy to GitHub Pages

```bash
# 1. Push to branch
git add . && git commit -m "Update Python Quest" && git push

# 2. GitHub Actions will auto-deploy to:
#    https://yourusername.github.io/apprendre_python/web/index.html
```

### Local hosting

```bash
# Simple HTTP server
python -m http.server 8000

# Then open http://localhost:8000/web/index.html
```

---

## 📚 Resources

- **Scratch to Python** : Started as Basile's progression from Scratch (age 11)
- **Inspiration** : Craig Reynolds' Boids, Khan Academy, Codecademy
- **Tech** : Pyodide (Python in browser), CodeMirror (editor), Tailwind (styling)
- **Images** : Pokémon art from official sources, F1 circuits, generative Boids

---

## 🐛 Known Issues

See **AGENTS-STATUS.md** for detailed bug reports and roadmap.

**Current limitations** :
- Multi-player support coming soon (Firebase integration)
- Pokémon images not yet dynamic (future update)
- Leaderboard placeholder (waiting for backend)
