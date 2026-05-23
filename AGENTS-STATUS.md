# AGENTS-STATUS.md — Python Quest

_Dernière mise à jour : 2026-05-23 — session Tâche 1 terminée_

---

## État du projet

Site d'apprentissage Python gamifié pour Basile (~11 ans, expert Scratch).
Stack : HTML statique + Pyodide + CodeMirror + Firebase Firestore (à implémenter).
Repo GitHub : **pas encore créé** (cible : `github.com/romainfjgaspard/apprendre_python`).
GitHub Pages cible : `https://romainfjgaspard.github.io/apprendre_python/`

**Source de vérité du contenu** : `chapters/ch{N:02d}/` (depuis 2026-05-23).
`chapters.json` est généré par `export_web.py` — ne pas éditer à la main.

---

## Avancement PLAN_REFONTE.md

| # | Tâche | État | Notes |
|---|-------|------|-------|
| 1 | Restructurer contenu → `chapters/ch*/` | ✅ Done 2026-05-23 | 240 fichiers, 26 chapitres |
| 2 | Cellules toutes éditables (`readOnly: false`) | ⬜ Todo | `app.js` ligne ~282 |
| 3 | Déplacer `web/` → racine + git init | ⬜ Todo | Avant GitHub Pages |
| 4 | Firebase Firestore multi-joueur | ⬜ Todo | Dépend de 3 |
| 5 | Leaderboard | ⬜ Todo | Dépend de 4 |
| 6 | Contenu bilingue EN/FR complet | ⬜ Todo | `.fr.md` à rédiger manuellement |
| 7 | Fixes pédagogiques (Ch2/4/5/6/8) | ⬜ Todo | Voir PLAN_REFONTE.md §7a-7f |
| 8 | UX / Gamification | ⬜ Todo | Bouton "Tout exécuter", sidebar Scratch |
| 9 | Progression Pokémon avec évolution | ⬜ Todo | En dernier (dépend de 4 + contenu stable) |

---

## Stack technique actuelle

```
apprendre_python/
├── chapters/ch{N:02d}/   ← SOURCE DE VÉRITÉ (nouveau depuis T1)
│   ├── meta.json
│   ├── {N}_lesson.en.md
│   ├── {N}_example.py
│   └── {N}_exercise.py
├── web/                  ← site servi (généré / à déplacer à la racine en T3)
│   ├── index.html        ← GA4 G-HCG77H3QXB
│   ├── leaderboard.html  ← placeholder
│   ├── app.js            ← moteur (~719 lignes)
│   ├── chapters.json     ← généré par export_web.py
│   ├── firebase.js       ← stub Realtime DB (à remplacer par Firestore en T4)
│   └── style.css
├── export_web.py         ← lit chapters/ → génère web/chapters.json
├── migrate_to_chapters.py ← one-shot T1, archivable
└── _verify.py
```

---

## Problèmes pédagogiques connus (à traiter en Tâche 7)

- **Ch2** : confusion `score` vs HP → renommer `score → pokemon_hp`
- **Ch4** : trop dense (for + while + break + for/else) → splitter Ch4 (for) + Ch4b (while)
- **Ch5** : list comprehensions prématurées → leçon 4 optionnelle (⭐ Bonus)
- **Ch6** : `lambda` trop tôt dans `max(..., key=lambda...)` → remplacer par boucle explicite
- **Ch8** : `open()` ne fonctionne pas dans Pyodide → reformuler autour de `json.dumps/loads`

---

## Notes de session

**2026-05-23** : Tâche 1 exécutée.
- `migrate_to_chapters.py` : migration one-shot chapters.json → 240 fichiers dans `chapters/ch{N:02d}/`
- `export_web.py` : réécrit pour lire `chapters/ch*/` au lieu des notebooks .ipynb
- `.gitignore` créé, repo git initialisé (commit initial)
- Rétrocompat : champ `source` = `source_en` dans les cellules md (supprimer en Tâche 6)

**Prochaine session — Tâche 2** : `app.js` ligne ~282, `readOnly: false`.
Ensuite Tâche 3 : déplacer `web/` → racine + `git remote add origin`.

**Blocants connus** :
- Firebase credentials à créer manuellement (Tâche 4) — pas de blocant immédiat
- Traduction `.fr.md` à faire manuellement (Tâche 6) — pas de blocant immédiat
