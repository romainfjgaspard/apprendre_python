# AGENTS-STATUS.md — Python Quest

_Dernière mise à jour : 2026-05-23 — fix zoom CSS (hors plan)_

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
| 2 | Cellules toutes éditables (`readOnly: false`) | ✅ Done 2026-05-23 | `app.js` ligne 281 — 1 ligne |
| 3 | Déplacer `web/` → racine + git init | ✅ Done 2026-05-23 | `web/` supprimé, `export_web.py` mis à jour |
| 4 | Firebase Firestore multi-joueur | ✅ Done 2026-05-23 | Credentials à remplir dans firebase.js |
| 5 | Leaderboard | ✅ Done 2026-05-23 | `leaderboard.html` réécrit — table + refresh |
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
├── index.html            ← GA4 G-HCG77H3QXB
├── leaderboard.html      ← placeholder
├── app.js                ← moteur (~719 lignes)
├── chapters.json         ← généré par export_web.py
├── firebase.js           ← stub Realtime DB (à remplacer par Firestore en T4)
├── style.css
├── images/pokedex/
├── export_web.py         ← lit chapters/ → génère chapters.json (racine)
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

**2026-05-23** : Tâche 2 exécutée.
- `web/app.js` ligne 281 : `readOnly: cell.type === "code"` → `readOnly: false`
- Toutes les cellules (exemples + exercices) sont maintenant éditables par le joueur

**2026-05-23** : Tâche 3 exécutée.
- `web/` déplacé à la racine (`mv web/* .` + `rmdir web`)
- `export_web.py` : chemin de sortie `web/chapters.json` → `chapters.json`
- Chemins HTML déjà relatifs, aucune modification nécessaire dans index.html / leaderboard.html / app.js

**2026-05-23** : Tâche 4 exécutée.
- `firebase.js` : réécriture complète Realtime DB → Firestore SDK modulaire v9+
  (fonctions : initFirebase, syncProgress, loadPlayer, listAllPlayers exposées sur window)
- `index.html` : firebase.js en `type=module`, app.js en `defer` (ordre d'exécution garanti)
  + dropdown `#existing-player` dans le splash (masqué si Firebase non configuré)
- `app.js` : startGame() async, charge progression Firestore pour joueurs existants,
  boot() peuple le dropdown, i18n complété (splash_existing_label, splash_or)
- `style.css` : style `<select>` aligné sur l'input existant

**2026-05-23** : Fix persistance cellules CodeMirror (hors plan, découvert en test).
- `app.js` : contenu saisi dans les cellules code/exercice sauvegardé en localStorage
  (clé `pq_cell_{num}_{idx}`) et restauré à la réouverture du chapitre

**2026-05-23** : Tâche 5 exécutée.
- `leaderboard.html` : 6 bugs corrigés + bouton refresh ajouté
  - `<script src>` → `<script type="module" src>` (firebase.js est un ES module)
  - Inline script en `type="module"` pour garantir l'ordre d'exécution
  - `loadLeaderboard()` (inexistant) → `window.listAllPlayers()`
  - `p.level` (inexistant) → calculé depuis XP via table LEVELS dupliquée inline
  - `p.chapters_done || 0` → `(p.chapters_done || []).length` (c'est un array)
  - Colonne "Level" → "Pokémon (niveau)" avec `starter_pokemon` + niveau calculé
  - Bouton "Rafraîchir" ajouté

**2026-05-23** : Fix zoom CSS (hors plan).
- `style.css` : `min-width: 640px` + `overflow-x: auto` sur `html`
- Zoom Ctrl+scroll → centrage et top-bar stables ✅
- Zoom pinch trackpad Windows → non résolu ⚠️ (comportement Visual Viewport natif, nécessiterait JS)

**Prochaine session — Tâche 6** : Contenu bilingue EN/FR (`.fr.md` à rédiger).

**Blocants connus** :
- `git remote add origin https://github.com/romainfjgaspard/apprendre_python.git` pas encore fait
- Les `.ipynb` sont untracked — à ajouter à `.gitignore`
- Traduction `.fr.md` à faire manuellement (Tâche 6) — pas de blocant immédiat
