# AGENTS-STATUS.md — Python Quest

_Dernière mise à jour : 2026-05-28 — Phase 1 migration SVG terminée (Phaser supprimé, snake grid S1 restaurée)_

---

## État du projet

Site d'apprentissage Python gamifié pour Basile (~11 ans, expert Scratch).
Stack : HTML statique + Pyodide + CodeMirror + Firebase Firestore.
Repo GitHub : https://github.com/romainfjgaspard/apprendre_python
GitHub Pages : https://romainfjgaspard.github.io/apprendre_python/
Firebase : projet `apprendre-python-f454a` — Firestore opérationnel ✅

**Source de vérité du contenu** : `chapters/ch{N:02d}/`
`chapters.json` est généré par `export_web.py` — ne pas éditer à la main.

---

## Avancement global

| # | Tâche | État | Notes |
|---|-------|------|-------|
| 1 | Restructurer contenu → `chapters/ch*/` | ✅ Done | 240 fichiers, 26 chapitres |
| 2 | Cellules toutes éditables | ✅ Done | `app.js` ligne ~281 |
| 3 | Déplacer `web/` → racine | ✅ Done | `web/` supprimé |
| 4 | Firebase Firestore multi-joueur | ✅ Done | Projet `apprendre-python-f454a` |
| 5 | Leaderboard | ✅ Done | `leaderboard.html` |
| 6 | Contenu bilingue EN/FR complet | ✅ Done | 130 fichiers .fr.md |
| 7 | Fixes pédagogiques (Ch2/4/5/6/8) | ✅ Done | 7a-7f + ch04b ajouté |
| 8 | UX / Gamification | ✅ Done | Run all, Scratch panel, Journey modal |
| 9 | Progression Pokémon avec évolution | ✅ Done | 4 starters × 3 évolutions |
| 10 | Overworld map Phaser.js (S1) | ✅ Done | Carte Pokémon scrollable, WASD, zones |
| 11 | Phase 0 — Nettoyage avant migration SVG | ✅ Done | Zone.Identifier supprimé, .gitignore, archive |
| 12 | Phase 1 — Suppression Phaser + snake grid S1 | ✅ Done | overworld.js supprimé, ~800 KB lib retirée, grid-s1 visible |

---

## Stack technique actuelle

```
apprendre_python/
├── chapters/
│   ├── ch{N:02d}/        ← SOURCE DE VÉRITÉ (27 chapitres, ch04b inclus)
│   │   ├── meta.json     ← { num, title, desc, badge, xp, season, boss }
│   │   ├── {N}_lesson.en.md / {N}_lesson.fr.md
│   │   ├── {N}_example.py
│   │   └── {N}_exercise.py
│   └── ch04b/            ← num=4.5, boucle while
├── index.html            ← GA4 G-HCG77H3QXB
├── leaderboard.html      ← Firestore multi-joueur
├── app.js                ← moteur principal
├── chapters.json         ← généré par export_web.py (27 chapitres)
├── firebase.js           ← Firestore SDK v9+ (credentials à configurer)
├── style.css
├── images/pokedex/       ← sprites Pokémon starters (12 PNG)
├── export_web.py         ← génère chapters.json depuis chapters/
├── _archive/             ← docs de planification archivés
└── _verify.py
```

---

## Points d'attention

### Bloquants connus
- **Firebase credentials** manquants dans `firebase.js` (section `firebaseConfig`) — Firebase non fonctionnel sans ça
- **Firestore rules** : actuellement `write: true` — à durcir avant usage réel

### Non résolu
- **Zoom trackpad** Windows (pinch-to-zoom visuel) — non traité, hors plan

### Saisons à traiter (migration SVG)
- **S1** : snake grid temporaire — sera remplacée par carte SVG en Phase 2
- **S2 (Formule 1)** : snake grid — carte SVG conditionnelle Phase 4
- **S3 (Birds)** : snake grid — carte SVG conditionnelle Phase 4

---

## Lancer en local

```bash
cd ~/projects/apprendre_python
python3 -m http.server 8000
# → http://localhost:8000/index.html
```

---

## Notes de session

**2026-05-26** : Tâche 10 — Overworld Phaser.js S1.
- `overworld.js` créé (~260 lignes) : scène Phaser 3 avec carte dessinée programmatiquement
- 10 zones (Bourg Palette → Arène Finale) avec type de terrain (ville/route/forêt/montagne/arène)
- Joueur = sprite Pokémon choisi (ou cercle jaune fallback), WASD + flèches, caméra qui suit
- Prompt ESPACE quand joueur est dans une zone débloquée → `openChapter(num)`
- Bouton "🎮 Explorer la Région Pokémon →" dans `#home-screen` S1
- `FROM_OVERWORLD` flag dans `app.js` pour le retour back/victory → overworld
- `renderMap()` : `#grid-s1` caché par défaut (`class="map-grid hidden"`)

**2026-05-26** : Ménage fichiers.
- 7 .md archivés dans `_archive/` (PLAN_ACTION, PLAN_REFONTE, SYNTHESE_ACTIONS, AGENTS, Map Python, mode_jeu, python_quest_worldmap_plan)
- `.ipynb` : déjà dans `.gitignore` (hors repo), contenu migré dans `chapters/` depuis T1 → supprimables en local si besoin de place
- `FIREBASE_SETUP.md` conservé (documentation utile)

**2026-05-28** : Phase 1 — Suppression Phaser + snake grid S1 restaurée.
- `overworld.js` supprimé (~287 lignes, 800 KB lib Phaser retirée)
- `index.html` : script Phaser, `<script defer src="overworld.js">`, `#overworld-screen`, bouton `#enter-overworld-btn` supprimés — `#grid-s1` plus `hidden`
- `app.js` : `FROM_OVERWORLD`, `window.getPokemonForm`, `Object.defineProperty(window,'PROG')`, `Object.defineProperty(window,'DATA')`, `window.openChapterFromOverworld`, blocs conditionnels `if (FROM_OVERWORLD)` (back-btn + victory-btn), handlers overworld supprimés
- `style.css` : `.btn-overworld`, `#overworld-screen`, `.ow-season-label`, `#phaser-container`, `.ow-prompt` supprimés
- Grep final : 0 référence Phaser/overworld hors `_archive/`
- S1 affiche désormais la snake grid comme S2 et S3 — cohérence restaurée

**2026-05-28** : Phase 0 — Nettoyage avant migration SVG.
- `python_quest_worldmap_plan.md:Zone.Identifier` supprimé
- `python_quest_worldmap_plan.md` racine supprimé (copie identique déjà dans `_archive/`)
- `.gitignore` : ajout `*:Zone.Identifier`

---

## Migration overworld → SVG en cours

Source de vérité : `PLAN_MIGRATION_SVG.md`
Prompts d'exécution : `PROMPTS_PHASES.md`

| Phase | Objectif | État |
|---|---|---|
| **0** | Nettoyage fichiers parasites (Zone.Identifier, archive, .gitignore) | ✅ Done |
| **1** | Suppression Phaser + retour temporaire snake grid S1 | ✅ Done |
| **2** | Carte SVG S1 (remplace snake grid S1) | ⏳ À faire |
| **3** | Animation évolution + 4e palier + remplacement Dratini par Charmander | ⏳ À faire |
| **4** | Cartes SVG S2 + S3 — **conditionnelle** (post-validation Basile) | ⏳ À faire |
| **5** | Polish : sons + sprite ambulant — **optionnel** | ⏳ À faire |
