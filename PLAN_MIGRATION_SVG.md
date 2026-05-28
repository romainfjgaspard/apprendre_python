# Plan de migration — Overworld Phaser → Cartes SVG

> Document de référence pour la migration de l'overworld Phaser actuel vers des cartes SVG simples pour les 3 saisons.
>
> **Statut :** validé après revue de challenge (18 décisions tranchées)
> **Source de vérité :** ce fichier remplace `python_quest_worldmap_plan.md` (archivé)
> **Exécution :** voir `PROMPTS_PHASES.md` pour les prompts à coller dans chaque nouveau chat

---

## ✅ Décisions validées (après revue de challenge)

| # | Décision | Choix retenu |
|---|---|---|
| 1 | Visibilité repo | Public familial, noms et sprites Pokémon conservés |
| 2 | Appareils cibles | **PC/Mac uniquement** (téléphone/tablette hors-scope) |
| 3 | Style cartes | SVG géométrique stylisé maison (zéro asset externe) |
| 4 | Ordre saisons | S1 d'abord (MVP), S2/S3 après feedback Basile |
| 5 | Anim évolution | Dans le MVP, juste après P2 |
| 6 | Refactor `app.js` | **Aucun maintenant**, tracé en backlog pour plus tard |
| 7 | Layout S2 | Serpentin Monaco-style (à valider) |
| 8-10 | Spec détaillée S2/S3 | **À valider après feedback Basile sur S1** |
| 11 | Format SVG | Inline généré par JS depuis config JSON |
| 12 | 4e forme d'évolution | **OUI**, à XP 1000 |
| 12bis | Cas Dratini (pas de Mega) | **Remplacer par Charmander** (4 formes officielles) |
| 12quater | Starter Fire complet | Charmander → Charmeleon → Charizard → Mega Charizard X |
| 13 | i18n | EN+FR pour tous les nouveaux libellés |
| 14 | Niveau a11y | Best effort (Tab + Enter + aria-label + `prefers-reduced-motion`) |
| 15 | Tests | Manuels uniquement (checklist régression) |
| 16 | Sons P5 | OFF par défaut, toggle "activer le son" |
| 17 | Sprite ambulant P5 | Conservé |
| 18 | Vieux doc design | Archivé dans `_archive/` |

---

## 🥊 Challenges & arbitrages

**Sur le scope :** *Pourquoi pas tout en une seule phase ?* Un seul gros chat = trop de surface, trop de régressions, impossible à débugger. Découpe forcée.

**Sur les priorités :** *Pourquoi anim d'évolution en Phase 3, pas Phase 2 ?* L'anim d'évolution est indépendante, elle peut tomber séparément. Risque isolé = bug isolé.

**Sur la cohérence S1/S2/S3 :** On accepte une période où S1 est en SVG et S2/S3 en snake grid, ~1-2 semaines. Permet de valider l'archi SVG avec un cas réel avant de la généraliser.

**Sur le mobile :** Décision tranchée : PC/Mac uniquement. Toutes les contraintes mobile/tablette/responsive sont **retirées du plan**.

**Sur la maintenance :** Aucun refactor préventif. Le découpage modulaire d'`app.js` est tracé en backlog (voir section "Dette technique différée").

**Sur GitHub Pages :** Le plan reste 100% statique. Aucun risque GH Pages. Basile devra Ctrl+F5 après chaque déploiement.

---

## 🚨 Points irréversibles à acter

1. **Phaser supprimé** → pas de retour en arrière.
2. **Snake grid `#grid-sX` supprimée** (fin Phase 4) → pas de retour.
3. **Format SVG inline généré JS depuis config JSON** → pas de Tiled, pas de tileset.
4. **Structure `PROG` localStorage gelée** (sauf 1 ajout en P5 : `audio_enabled`).
5. **Remplacement de Dratini par Charmander** (Phase 3) → les saves existantes avec `starter_pokemon: 147` devront être migrées.

---

## 🔒 Inventaire — Conserver / Geler / Refactor / Supprimer

**Conserver tel quel :** `chapters/`, `chapters.json`, `export_web.py`, `_verify.py`, `migrate_to_chapters.py`, `images/pokedex/`, `_archive/`, `FIREBASE_SETUP.md`, `leaderboard.html`, `firebase.js`.

**Geler (interdit de toucher pendant migration) :** logique pédagogique d'`app.js` (lessons, run code, victory hors animation), `firebase.js`, `leaderboard.html`, système `data-i18n` EN/FR, tag GA4.

**Refactorer avant toute nouvelle feature :** **rien**. Aucun refactor préventif. Le refactor `app.js` → modules est tracé en backlog.

**Supprimer :**
- `overworld.js` (Phase 1)
- `<script phaser.min.js>` (Phase 1)
- `#overworld-screen`, `#enter-overworld-btn`, `#ow-*` (Phase 1)
- `FROM_OVERWORLD`, `openChapterFromOverworld`, `returnToOverworld`, `destroyOverworld`, `openOverworld` (Phase 1)
- `python_quest_worldmap_plan.md:Zone.Identifier` (Phase 0)
- `python_quest_worldmap_plan.md` → `_archive/` (Phase 0)
- `#grid-sX` HTML + JS associé (fin Phase 4)
- CSS overworld + CSS snake grid (au fil des phases)

---

## 🧪 Checklist régression — à exécuter à la fin de CHAQUE phase

1. Splash → nom → starter → home → chapitre 1 → run example → exo → run → victoire → retour map. **Aucune erreur console.**
2. Reload page : save préservée (nom, XP, starter, chapitres complétés).
3. Click chapitre verrouillé : refusé.
4. Ouverture chapitre déjà complété : rejouable.
5. Leaderboard accessible et retour OK.
6. Pyodide ne se charge **qu'à** la première ouverture de chapitre.
7. Firebase sync (si configuré) : `PROG` envoyé avec la structure attendue.

---

## ⚠️ Pièges d'implémentation transverses

- Ne pas casser la structure de `PROG` → Firebase sync casse silencieusement.
- Pyodide ne doit être initialisé qu'à la première ouverture de chapitre.
- Hotspots SVG doivent être focusables au clavier (Tab + Enter).
- `viewBox` SVG bien configuré pour différentes tailles d'écran PC (1280/1920/4K).
- Pas d'animation via `top/left` → `transform` only.
- Respecter `data-i18n` pour nouveaux libellés EN/FR.
- GitHub Pages cache : Ctrl+F5 pendant les tests.

---

## 🗺️ ROADMAP — Vue d'ensemble

| Phase | Objectif | Complexité | Indépendance |
|---|---|---|---|
| 0 | Nettoyage immédiat | XS (30 min) | Aucune dépendance |
| 1 | Suppression Phaser + retour snake grid temporaire | S (1 session) | Dépend de Phase 0 |
| 2 | Carte SVG S1 (remplace snake grid S1) | M (2 sessions) | Dépend de Phase 1 |
| 3 | Animation d'évolution + ajout 4e palier + remplacement Dratini | M (1-2 sessions, étendue) | Indépendant de Phase 2 |
| 4 | Cartes SVG S2 + S3 (**conditionnelle**, post-validation Basile) | M (1-2 sessions) | Dépend de Phase 2 + validation |
| 5 | Polish (sons + sprite ambulant) | S (1 session, optionnel) | Dépend de Phase 4 |

**Total : 4-6 sessions de 2h pour MVP complet et cohérent.**

**Coupe-circuit :** si la Phase 2 déçoit après test avec Basile, **ne pas continuer en P4**.

---

## 📦 PHASE 0 — Nettoyage immédiat

### Objectif
Repartir d'une base propre avant toute migration. **Aucun changement de comportement utilisateur.**

### Valeur utilisateur
Aucune visible. Hygiène du repo.

### Complexité
**XS — 30 minutes.**

### Fichiers à modifier
- `.gitignore` (ajout pattern `*:Zone.Identifier`)
- `AGENTS-STATUS.md` (mise à jour état + ajout section "Migration overworld → SVG en cours" listant les 5 phases)

### Fichiers à supprimer / déplacer
- `python_quest_worldmap_plan.md:Zone.Identifier` → suppression
- `python_quest_worldmap_plan.md` → déplacement dans `_archive/`

### Dépendances
Aucune.

### Dette technique
- Créée : 0
- Remboursée : 1 fichier parasite + 1 doc obsolète sortis du chemin de lecture

### Contraintes
- **Ne PAS toucher au code** (`app.js`, `overworld.js`, `index.html`, `style.css`).
- **Ne PAS toucher** à `chapters/`, `chapters.json`, ni au build.

### Risques connus
Aucun.

### Régressions possibles
Aucune (aucun code touché).

### Tests manuels
- `git status` propre après commit.
- App se lance encore (`python3 -m http.server 8000` → `http://localhost:8000`).
- Splash → starter → home → chapitre 1 → run code → victoire → retour map fonctionne.

### Definition of DONE
- [ ] `python_quest_worldmap_plan.md:Zone.Identifier` n'existe plus
- [ ] `python_quest_worldmap_plan.md` est dans `_archive/`
- [ ] `.gitignore` contient `*:Zone.Identifier`
- [ ] `AGENTS-STATUS.md` mentionne la migration overworld → SVG (5 phases listées)
- [ ] Commit : `chore: nettoyage avant migration SVG (Phase 0)`

---

## 🔥 PHASE 1 — Suppression de Phaser, retour temporaire à la snake grid S1

### Objectif
Retirer entièrement Phaser et l'overworld du codebase. Réafficher temporairement la snake grid S1 (en attendant la carte SVG en Phase 2).

### Valeur utilisateur
- App ~800 KB plus légère
- Cohérence visuelle restaurée (3 saisons identiques en snake grid)
- Code base nettoyée pour la suite

### Complexité
**S — 1 session de 1-2h.**

### Fichiers à modifier
- `index.html` :
  - Retirer `<script src="https://cdn.jsdelivr.net/npm/phaser@3.88.2/dist/phaser.min.js"></script>`
  - Retirer `<script defer src="overworld.js"></script>`
  - Retirer tout le bloc `<div id="overworld-screen">…</div>`
  - Retirer le bouton `<button id="enter-overworld-btn">…</button>` dans `#season-1`
  - Retirer la classe `hidden` sur `<div class="map-grid hidden" id="grid-s1">` → doit devenir `<div class="map-grid" id="grid-s1">`
- `app.js` :
  - Retirer `let FROM_OVERWORLD = false;`
  - Retirer `window.openChapterFromOverworld`
  - Retirer les blocs `if (FROM_OVERWORLD) { … window.returnToOverworld(); }` dans `#back-btn` et `#victory-btn` (garder uniquement la branche `else`)
  - Retirer `Object.defineProperty(window, 'PROG', …)` et `Object.defineProperty(window, 'DATA', …)` SI aucun autre code ne les utilise (vérifier avec grep)
  - Retirer `window.getPokemonForm = getPokemonForm;` SI plus utilisé
  - Retirer le handler du bouton `#enter-overworld-btn` (s'il existe)
- `style.css` : retirer les règles `.btn-overworld`, `#phaser-container`, `.ow-prompt`, `.ow-season-label`, `#ow-hud-*`, `#overworld-screen`
- `AGENTS-STATUS.md` : marquer Phase 1 done

### Fichiers à supprimer
- `overworld.js`

### Dépendances
Phase 0.

### Dette technique
- Créée : 0
- Remboursée : ~290 lignes JS, ~800 KB de lib externe, ~50 lignes CSS, ~15 lignes HTML

### Contraintes
- **Ne PAS toucher** à la structure de `PROG` (localStorage).
- **Ne PAS toucher** à `firebase.js`, `leaderboard.html`, `chapters/`, `chapters.json`, `export_web.py`, `_verify.py`.
- **Ne PAS refactorer `app.js` en modules.**
- **Ne PAS toucher** au système `data-i18n` ni au tag GA4.

### Risques connus
- Casser le rendu de `renderMap()` en retirant la classe `hidden` mal.
- Oublier de retirer des références à `window.PROG` / `window.DATA` exposées pour Phaser.

### Régressions possibles
- Le bouton 🎮 disparaît : intention, mais vérifier qu'aucun raccourci ne le déclenche.

### Tests manuels
Checklist régression complète +
- F12 → Network : aucune requête vers `phaser.min.js`.
- F12 → Console : aucune référence à `Phaser`, `_game`, `OverworldScene`.
- `#grid-s1` visible avec tous les chapitres S1.
- Click sur chapitre S1 → ouverture lesson OK.
- `grep -r "Phaser\|phaser\|OverworldScene\|FROM_OVERWORLD\|openChapterFromOverworld\|returnToOverworld\|destroyOverworld\|openOverworld\|enter-overworld-btn\|overworld-screen" .` → 0 résultats (hors `_archive/` et docs).

### Definition of DONE
- [ ] `overworld.js` supprimé
- [ ] `index.html` ne charge plus Phaser et n'a plus `#overworld-screen`
- [ ] `app.js` n'a plus de référence à `FROM_OVERWORLD`, `openChapterFromOverworld`, `returnToOverworld`
- [ ] `style.css` nettoyé des règles overworld
- [ ] `#grid-s1` visible (plus de classe `hidden`)
- [ ] Checklist régression complète passe
- [ ] Commit : `chore: suppression Phaser + overworld (Phase 1)`

### TODO futurs
- Phase 2 : construire la carte SVG S1

---

## 🎨 PHASE 2 — Carte SVG S1 (remplace la snake grid S1)

### Objectif
Construire une carte SVG illustrée stylisée pour la Saison 1 (Pokémon), remplaçant la snake grid `#grid-s1`. Hotspots cliquables, états visuels (verrouillé/disponible/complété), sprite du starter affiché sur la zone "active".

### Valeur utilisateur
- "Wow" visuel sur S1 : la map ressemble enfin à une vraie carte d'aventure.
- Progression visualisée comme un parcours, pas comme une liste.
- Sprite du starter visible "sur" la map.

### Complexité
**M — 2 sessions de 2h.**

### Spec de la carte SVG S1

1. **Layout vertical** (haut = arène boss, bas = bourg de départ). ViewBox configuré pour s'adapter aux tailles d'écran PC (1280 × 1920).
2. **Background stylisé** : herbe verte, chemin sinueux entre zones, éléments décoratifs (arbres, eau, rochers) en formes SVG simples (cercles, triangles, rectangles arrondis, gradients).
3. **10 zones (hotspots)** pour les chapitres 1 à 9 (avec 4.5) :
   - Chapitre 1 : "Bourg Palette" (town) — bas
   - Chapitre 2 : "Route 1" (route)
   - Chapitre 3 : "Forêt de Viridian" (forêt)
   - Chapitre 4 : "Mont Sélénite" (montagne)
   - Chapitre 4.5 : "Mont Sélénite (suite)" (montagne)
   - Chapitre 5 : "Azuria City" (town)
   - Chapitre 6 : "Musée d'Azuria" (town)
   - Chapitre 7 : "Route 24" (route)
   - Chapitre 8 : "Pélipuces City" (town)
   - Chapitre 9 : "Arène Finale" (boss) — haut
4. **États visuels par zone** :
   - Verrouillée : grise, opaque, cadenas 🔒, non-cliquable
   - Disponible : couleur vive, légère pulsation, cliquable
   - Complétée : couleur verte, checkmark ✅, cliquable (rejouable)
   - "Current" (premier non-done disponible) : encadrée d'une bordure dorée + sprite du starter affiché à côté
5. **Hotspots** : `tabindex="0"`, `role="button"`, `aria-label="Chapitre N — Nom (état)"`. Click ET Enter/Space ouvrent le chapitre via `openChapter(num)`.
6. **Taille hotspot** : ~80×80 px (cible PC confort, pas mobile).

### Fichiers à créer
- `map.js` (~250 lignes max) :
  - Vanilla JS, pas de modules ES6
  - `window.renderSeasonMap = function(seasonId) { … }`
  - Config inline : `const MAPS = { s1: { width: 600, height: 1200, zones: [...] } }`
  - Génère SVG avec `document.createElementNS('http://www.w3.org/2000/svg', 'svg')`
  - Lit `window.PROG.chapters_done`, `window.PROG.starter_pokemon`
  - Utilise `window.getPokemonForm` pour le sprite

### Fichiers à modifier
- `index.html` :
  - Remplacer `<div class="map-grid" id="grid-s1"></div>` par `<div class="season-map" id="map-s1"></div>`
  - Ajouter `<script defer src="map.js"></script>` avant `app.js`
- `app.js` :
  - Dans `renderMap()`, pour S1 : appeler `window.renderSeasonMap('s1')` au lieu de générer la snake grid
  - S2 et S3 : garder logique snake grid
  - Réexposer `window.PROG`, `window.DATA`, `window.getPokemonForm`, `window.openChapter` si retirés en Phase 1
- `style.css` :
  - Ajouter `.season-map`, `.svg-hotspot`, `.svg-hotspot--locked/available/done/current`
  - Animations : pulse (`--available`), glow doré (`--current`), glow vert (`--done`)
  - Layout PC : SVG `max-width:600px; margin:0 auto`
- `AGENTS-STATUS.md` : marquer Phase 2 done

### Dépendances
Phase 1 (Phaser retiré).

### Dette technique
- Créée : nouveau module `map.js`. Coexistence avec snake grid (S2/S3) pendant ~1-2 semaines. Acceptable.
- Remboursée : grille snake S1 retirée

### Contraintes
- **Ne PAS toucher** à la structure de `PROG`.
- **Ne PAS toucher** à `firebase.js`, `leaderboard.html`, `chapters/`, `chapters.json`.
- **Ne PAS toucher** à la logique pédagogique d'`app.js` (lessons, run code, victory).
- **Ne PAS migrer S2/S3** : ils restent en snake grid jusqu'à la Phase 4.
- **Ne PAS introduire** de framework ni de lib externe.
- **Ne PAS utiliser** `top/left` pour les animations → `transform` only.
- **Respecter `data-i18n`** pour les libellés EN/FR.

### Risques connus
- Sprite du starter mal positionné par rapport à la zone "current"
- Pyodide se charge à l'arrivée sur map (régression de perf)

### Régressions possibles
- Si `renderMap()` mal modifié, S2/S3 peuvent disparaître
- Sync Firebase affecté si globals mal exposés

### Pièges à éviter
- Hotspots SVG sans `pointer-events:auto` → click non capté
- "current" = premier chapitre non-done disponible (pas un complété)
- Réexposer les globals `window.PROG`, `window.DATA`, etc. retirés en P1 mais nécessaires pour `map.js`

### Tests manuels
Checklist régression +
- Carte SVG S1 s'affiche (Bourg Palette en bas, Arène en haut)
- Click sur Bourg Palette → ouverture lesson
- Click sur Arène verrouillée → refusé
- Sprite du starter visible sur zone "current"
- Clavier : Tab navigue, Enter active
- Affichage cohérent à 1280×800 et 1920×1080

### Definition of DONE
- [ ] `map.js` créé (~250 lignes max)
- [ ] `#map-s1` rend un SVG avec 10 hotspots positionnés
- [ ] États locked/available/done/current visuellement distincts
- [ ] Sprite du starter affiché sur la zone "current"
- [ ] Click ou Enter sur hotspot disponible → ouvre le chapitre
- [ ] Click sur hotspot verrouillé → ne fait rien
- [ ] S2 et S3 toujours en snake grid
- [ ] A11y : Tab + Enter + `aria-label`
- [ ] Console F12 : zéro erreur
- [ ] Save préservée après reload
- [ ] Firebase sync (si configuré) fonctionnel
- [ ] Leaderboard accessible
- [ ] Commit : `feat: carte SVG saison 1 (Phase 2)`

### TODO futurs
- Phase 3 : anim évolution + ajout 4e palier + remplacement Dratini
- Phase 4 (conditionnelle) : étendre à S2 et S3

---

## ✨ PHASE 3 — Animation d'évolution + ajout 4e palier + remplacement Dratini

### Objectif
Trois changements liés au système d'évolution Pokémon :
1. **Remplacer Dratini par Charmander** (qui a 4 formes officielles)
2. **Ajouter une 4e forme d'évolution** (Mega) à XP 1000 pour les 4 starters
3. **Animation cinématique d'évolution** à chaque transition de forme

### Valeur utilisateur
**LE moment "wow" du projet.** L'enfant voit son Pokémon évoluer — paie tout l'effort de progression. Avec 4 paliers au lieu de 3, motivation longue durée renforcée.

### Complexité
**M — 1-2 sessions de 2h.**

### Spec — Changement 1 : remplacement Dratini par Charmander

- Retirer le starter `id: 147` (Dratini) de `STARTERS`.
- Ajouter `id: 4` (Charmander) avec 4 formes :
  - Forme 0 (XP 0) : Charmander (ID 4) — EN "Charmander" / FR "Salamèche"
  - Forme 1 (XP 150) : Charmeleon (ID 5) — EN "Charmeleon" / FR "Reptincel"
  - Forme 2 (XP 500) : Charizard (ID 6) — EN "Charizard" / FR "Dracaufeu"
  - Forme 3 (XP 1000) : Mega Charizard X (ID custom) — EN "Mega Charizard X" / FR "Méga-Dracaufeu X"

### Spec — Changement 2 : ajout 4e palier pour les autres starters

Étendre les 3 autres starters avec une 4e forme :
- Squirtle (7) → ajouter Mega Blastoise (ID custom) à XP 1000 — FR "Méga-Tortank"
- Froakie (656) → ajouter Ash-Greninja (ID custom) à XP 1000 — FR "Amphinobi-Ash"
- Bagon (371) → ajouter Mega Salamence (ID custom) à XP 1000 — FR "Méga-Drattak"

### Spec — Changement 3 : animation d'évolution

1. **Déclenchement** : dans `showVictory()`, calculer `oldForm = getPokemonForm(oldXp, starterId)` (avant ajout XP) et `newForm = getPokemonForm(newXp, starterId)` (après). Si `oldForm.pokeId !== newForm.pokeId` ET `isNew === true`, déclencher l'anim.

2. **Séquence (~3 secondes)** :
   - Overlay plein écran semi-transparent noir (z-index au-dessus de victory modal)
   - Sprite ancienne forme centré, grossit légèrement
   - Flash blanc (~500 ms)
   - Pendant le flash : swap d'image (ancienne → nouvelle)
   - Flash s'estompe → nouvelle forme révélée, légère pulsation, particules CSS
   - Texte : "Ton {nom_ancien} évolue en {nom_nouveau} !" (EN/FR via `data-i18n`)
   - Bouton "Continuer" (Enter/Space/clic overlay pour skip)
   - Disparition overlay, retour à victory modal

3. **Pas d'évolution si** :
   - Chapitre rejoué (`isNew === false`)
   - XP gagné ne franchit aucun seuil
   - Pas de starter

### Spec — Migration save existante

Au démarrage de l'app (dans `loadProgress()` ou juste après), vérifier :
- Si `PROG.starter_pokemon === 147` (Dratini) : remplacer par `4` (Charmander), `saveProgress(PROG)`, et afficher une notification douce ("Ton Dratini a été transformé en Salamèche suite à une mise à jour 🔥")
- Le HUD doit reprendre normalement après cette migration

### Fichiers à modifier
- `app.js` :
  - Mettre à jour `STARTERS` (retirer Dratini, ajouter Charmander, étendre les 3 autres avec une 4e forme)
  - Dans `loadProgress()`, ajouter la migration Dratini → Charmander
  - Dans `showVictory()`, capturer `oldXp` avant `PROG.xp += ch.xp;`
  - Après ajout XP, calculer `oldForm` et `newForm`
  - Si évolution + `isNew`, appeler `playEvolutionAnimation(oldForm, newForm)`
  - Ajouter clés i18n : `evolution_intro`, `evolution_arrow`, `evolution_continue`, `dratini_migration` (notification)
- `index.html` : ajouter avant `</body>` un `<div id="evolution-overlay">` avec sprite, flash, texte, bouton
- `style.css` (~80 lignes) :
  - `.evolution-overlay` : position fixed, z-index très haut, fond noir 0.9
  - `.evolution-stage` : flex column, centré
  - `#evolution-sprite` : ~200px, transition transform
  - `#evolution-flash` : div blanche absolue, opacity 0→1→0
  - `@keyframes evolution-pulse` (scale 1→1.1→1) et `evolution-flash` (opacity)
  - Animations GPU only (`transform`, `opacity`)
  - Respect `prefers-reduced-motion` : pas de flash, juste swap sprite
- `AGENTS-STATUS.md` : marquer Phase 3 done

### Fichiers à créer
- `images/pokedex/4.png` (Charmander)
- `images/pokedex/5.png` (Charmeleon)
- `images/pokedex/6.png` (Charizard)
- `images/pokedex/6-mega-x.png` (Mega Charizard X, ID custom)
- `images/pokedex/9-mega.png` (Mega Blastoise)
- `images/pokedex/658-ash.png` (Ash-Greninja)
- `images/pokedex/373-mega.png` (Mega Salamence)

**Source des sprites :** PokeAPI ou Bulbapedia (PNG transparents officiels). À sourcer avant le commit.

**Structure HTML à ajouter :**
```html
<div id="evolution-overlay" class="modal hidden">
  <div class="evolution-stage">
    <img id="evolution-sprite" src="" alt="">
    <div id="evolution-flash"></div>
    <div class="evolution-text">
      <span data-i18n="evolution_intro">Ton</span>
      <span id="evolution-old-name"></span>
      <span data-i18n="evolution_arrow">évolue en</span>
      <span id="evolution-new-name"></span>
      <span>!</span>
    </div>
    <button id="evolution-continue" class="btn btn-primary" data-i18n="evolution_continue">Continuer</button>
  </div>
</div>
```

### Dépendances
Indépendant de Phase 2. Peut être fait avant ou après.

### Dette technique
- Créée : ~80 lignes CSS + ~80 lignes JS (anim + migration + extension STARTERS). Acceptable.
- Remboursée : 0

### Contraintes
- **Ne PAS** déclencher l'anim si chapitre rejoué.
- **Ne PAS** modifier la structure de `PROG` (la migration Dratini ne change que la valeur de `starter_pokemon`, pas le schéma).
- **Ne PAS** ajouter de dépendance externe.
- **Ne PAS** utiliser `top/left` (GPU only).
- **Respecter `prefers-reduced-motion`** : juste swap sprites sans flash si activé.

### Risques connus
- Sprites Mega introuvables en PNG transparent → fallback nécessaire
- Migration Dratini → Charmander mal faite : starter invisible ou save corrompue
- Double déclenchement de l'anim

### Régressions possibles
- Si victory modal cassée, retour map en boucle
- Si la migration tourne en boucle (oubli de save après migration)

### Pièges à éviter
- `getPokemonForm` AVANT et APRÈS l'ajout XP pour voir la transition
- Si XP gagné fait sauter 2 paliers, transition directement à la forme finale
- Bouton "Continuer" doit refocus correctement (a11y)
- Overlay évolution PAR-DESSUS victory modal, pas la remplacer
- Migration Dratini : ne le faire QU'UNE fois (sinon notif à chaque load)

### Tests manuels
- 4 starters testés (Charmander 4, Squirtle 7, Froakie 656, Bagon 371)
- 3 transitions par starter (forme 0→1 à XP 150, forme 1→2 à XP 500, forme 2→3 à XP 1000) = **12 cas**
- Procédure : `PROG.xp = 100; saveProgress(PROG);` puis reload → compléter un chapitre rapportant ≥50 XP → vérifier anim
- Rejouer un chapitre déjà complété : pas d'anim
- Skip via Enter/Space/clic overlay
- `prefers-reduced-motion` : flash désactivé
- Migration Dratini : simuler `PROG.starter_pokemon = 147; saveProgress(PROG);` puis reload → vérifier conversion en Charmander + notif

### Definition of DONE
- [ ] `STARTERS` contient 4 starters (Charmander, Squirtle, Froakie, Bagon) chacun avec 4 formes
- [ ] Sprites Mega téléchargés et présents dans `images/pokedex/`
- [ ] Migration Dratini → Charmander fonctionnelle (test reproductible)
- [ ] Anim joue UNIQUEMENT en cas d'évolution + chapitre fraîchement complété
- [ ] Sprite swap visible (flash blanc)
- [ ] Texte affiche les bons noms (EN/FR)
- [ ] Skip Enter/Space/clic overlay
- [ ] Bouton "Continuer" ferme l'overlay
- [ ] Victory modal reste affichée après
- [ ] **12 cas testés** (4 starters × 3 transitions)
- [ ] Chapitre rejoué : pas d'anim
- [ ] `prefers-reduced-motion` respecté
- [ ] Console : zéro erreur
- [ ] Commit : `feat: anim évolution + 4e palier + remplacement Dratini par Charmander (Phase 3)`

---

## 🌍 PHASE 4 — Cartes SVG S2 + S3 (suppression définitive snake grid)

### ⚠️ Phase conditionnelle

**À exécuter UNIQUEMENT après :**
1. Validation de la P2 par Basile (carte S1 testée et plait)
2. Confirmation du nombre exact de chapitres S2 et S3 (peut bouger après feedback)
3. Confirmation des noms de zones S2 et S3 (les noms proposés ci-dessous sont des suggestions, à valider)

**Si Basile veut ajouter ou supprimer des chapitres en S2/S3 avant cette phase**, c'est le bon moment. Cette spec sera mise à jour avant exécution.

### Objectif
Étendre `map.js` pour gérer S2 (F1) et S3 (Birds), avec une **ambiance visuelle propre à chaque saison**. Puis supprimer définitivement la snake grid.

### Valeur utilisateur
- Cohérence visuelle complète : les 3 saisons ont la même UX qualitative.
- Identités visuelles : circuit F1 pour S2, ciel/oiseaux pour S3.

### Complexité
**M — 1-2 sessions de 2h.**

### Spec S2 (F1) — suggestion à valider
- **Ambiance** : asphalte gris foncé, lignes blanches de piste, drapeaux à damier en accents, gradient bleu nuit en arrière-plan
- **Layout** : circuit serpentin Monaco-style (lignes droites + virages serrés), zones le long du tracé
- **8 zones** (à confirmer) pour chapitres 10 à 17 :
  - ch 10 : "Stand des mécaniciens" (entrée)
  - ch 11 : "Première chicane"
  - ch 12 : "Ligne droite"
  - ch 13 : "Virage des stats"
  - ch 14 : "Tunnel des données"
  - ch 15 : "Pandas Square"
  - ch 16 : "Dernière épingle"
  - ch 17 : "Drapeau à damier 🏁" (boss)

### Spec S3 (Birds) — suggestion à valider
- **Ambiance** : dégradé ciel bleu → orange (sunset), nuages cotonneux blancs, oiseaux stylisés (triangles fins) en groupe
- **Layout** : montée vers le ciel, zones en altitude croissante
- **9 zones** (à confirmer) pour chapitres 18 à 26 :
  - ch 18 : "Le sol" (base)
  - ch 19 : "Premiers vols"
  - ch 20 : "Nuage des matrices"
  - ch 21 : "Animation de l'air"
  - ch 22 : "Premier Boid"
  - ch 23 : "Les 3 règles"
  - ch 24 : "Predator"
  - ch 25 : "Simulation"
  - ch 26 : "Sommet ☁️" (boss)

### Fichiers à modifier
- `map.js` :
  - Étendre config : `MAPS.s2 = { width, height, theme: 'f1', zones: [...] }` et `MAPS.s3 = { width, height, theme: 'birds', zones: [...] }`
  - Factoriser : `renderSeasonMap(seasonId)` utilise `theme` pour bg/palette
  - Réutiliser logique S1 pour les états/hotspots/a11y
  - Pas d'overengineering : `if (theme === 'f1') drawF1Background()` est OK
- `index.html` :
  - Remplacer `<div class="map-grid" id="grid-s2"></div>` par `<div class="season-map" id="map-s2"></div>`
  - Idem pour `s3`
- `app.js` :
  - `renderMap()` devient `updateHUD(); renderSeasonMap('s1'); renderSeasonMap('s2'); renderSeasonMap('s3');`
  - **Supprimer** toute la logique snake grid (boucles `rows`, `displayOrder`, `arrowChar`, `tile-spacer`, création `.map-tile`)
- `style.css` :
  - **Supprimer** `.map-grid`, `.map-row`, `.arrow-h`, `.tile-spacer`, `.map-tile` et variantes
  - **Ajouter** classes thématiques : `.season-map[data-theme="f1"]`, `.season-map[data-theme="birds"]` (gradients/couleurs)
  - Keyframes : drapeau à damier (S2 boss), oiseaux qui volent (S3, subtil)
- `AGENTS-STATUS.md` : marquer Phase 4 done + "snake grid retirée définitivement"

### Dépendances
Phase 2 + validation Basile + confirmation specs S2/S3.

### Dette technique
- Créée : 0
- Remboursée : ~150 lignes JS + ~200 lignes CSS

### Contraintes
- **Ne PAS toucher** à `PROG`, `firebase.js`, `leaderboard.html`, `chapters/`.
- **Ne PAS toucher** au système d'évolution (Phase 3 indépendante).
- **Ne PAS introduire** de framework.
- **Ne PAS overengineer** la factorisation : `if/else` sur `theme` suffit pour 3 saisons.
- **Respecter `data-i18n`**.

### Risques connus
- Layout S2/S3 mal pensé (8 et 9 chapitres respectivement)
- Identités visuelles trop semblables

### Régressions possibles
- Suppression trop tôt des classes CSS snake grid → S2/S3 invisibles temporairement

### Pièges à éviter
- Avant de supprimer les classes CSS snake grid, `grep -r ".map-grid\|.map-tile\|arrow-h\|tile-spacer" .` doit ne retourner que les fichiers à modifier
- S3 a 9 chapitres : layout sans débordement
- Ambiance S2 (sombre) : contraste WCAG AA min pour les libellés
- Boss de chaque saison visuellement distinct (taille zone plus grande, icône spéciale)

### Tests manuels
Checklist régression +
- 3 saisons en SVG, chacune avec sa palette
- Click chapitre 11 (S2) → leçon
- Click chapitre 22 (S3) → leçon (si débloqué) ou refusé
- Tab : parcours complet sans saut
- `grep -r "\.map-grid\|\.map-tile\|arrow-h\|tile-spacer" .` → 0 résultats (hors `_archive/`)

### Definition of DONE
- [ ] S2 affichée en SVG avec ambiance F1 (N hotspots — N à confirmer)
- [ ] S3 affichée en SVG avec ambiance Birds (N hotspots — N à confirmer)
- [ ] Les 3 saisons ont la même UX qualitative
- [ ] Aucune trace de snake grid (grep clean)
- [ ] Tous les chapitres accessibles
- [ ] A11y OK
- [ ] Save préservée
- [ ] Console F12 : zéro erreur
- [ ] Commit : `feat: cartes SVG saisons 2 et 3 + suppression snake grid (Phase 4)`

---

## 🎁 PHASE 5 — Polish (optionnel)

### Objectif
Ajouter sons et micro-animations pour finir l'expérience.

### Valeur utilisateur
Marginal mais agréable. **À ne lancer que si Basile utilise activement et demande "plus".**

### Complexité
**S — 1 session de 2h.**

### Spec

1. **Sons (3 max)** :
   - `audio/click.wav` : son court hotspot click (~50 ms)
   - `audio/victory.wav` : fanfare courte fin de chapitre (~1 s)
   - `audio/evolution.wav` : son d'évolution (~2 s)
   - **Sources** : sfxr (chiptune généré) ou freesound.org CC0. **Pas de samples Pokémon officiels.**
   - Trigger : `new Audio('audio/xxx.wav').play()`. Préchargement à l'arrivée sur home.
   - **OFF par défaut**. Toggle "Activer le son" 🔊/🔇 dans HUD, persisté dans `PROG.audio_enabled`.

2. **Sprite Pokémon ambulant (S1 uniquement)** :
   - Mini sprite du starter qui "trotte" le long du chemin SVG entre la dernière zone complétée et la zone "current"
   - Animation CSS `@keyframes walk-path` avec `offset-path: path(...)`
   - Apparaît à l'arrivée sur home, dure ~2 s, puis disparaît
   - Désactivé si `prefers-reduced-motion`

### Fichiers à modifier
- `map.js` (sprite ambulant)
- `app.js` (audio toggle + triggers, ajout `PROG.audio_enabled = false` par défaut)
- `style.css` (keyframes walk-path + styles toggle son)
- `index.html` (bouton 🔊 dans le HUD)
- `AGENTS-STATUS.md` : marquer Phase 5 done

### Fichiers à créer
- `audio/click.wav`, `audio/victory.wav`, `audio/evolution.wav` (≤ 100 KB total)

### Dépendances
Phase 4.

### Contraintes
- **Pas de samples Pokémon officiels** (juridique).
- **Pas de musique de fond**.
- **Sons OFF par défaut** (toggle pour activer).
- **Toggle son persistant** dans `PROG.audio_enabled` (ajout autorisé pour cette phase).
- **`prefers-reduced-motion` respecté**.

### Tests manuels
- Sons OFF au premier lancement
- Toggle 🔊 active les sons, persiste après reload
- Sons jouent au bon moment quand activés
- Sprite ambulant s'affiche à l'arrivée S1
- `prefers-reduced-motion` désactive l'anim

### Definition of DONE
- [ ] 3 fichiers audio dans `audio/` (≤ 100 KB total)
- [ ] Toggle 🔊/🔇 dans HUD, persisté dans `PROG.audio_enabled` (default `false`)
- [ ] Sons OFF par défaut, jouent quand activés
- [ ] Sprite ambulant joue à l'arrivée sur home S1
- [ ] `prefers-reduced-motion` désactive l'anim
- [ ] Pas de régression
- [ ] Commit : `feat: polish — sons et sprite ambulant (Phase 5)`

---

## 📚 Dette technique différée / Backlog (post-migration)

Ces éléments sont identifiés mais **volontairement reportés** pour ne pas alourdir la migration. À traiter quand une feature future le justifiera.

### Refactor `app.js` en modules
- **État actuel** : 1155 lignes vanilla, sans modules, sans typage.
- **Découpe suggérée** :
  - `core/progress.js` — `PROG`, `LEVELS`, `STARTERS`, `getPokemonForm`, `loadProgress`, `saveProgress`
  - `core/pyodide.js` — chargement et exécution Python
  - `ui/hud.js` — `updateHUD`, langage toggle
  - `ui/chapter.js` — `openChapter`, rendu lessons, run code
  - `ui/victory.js` — `showVictory`, retour map
  - `ui/evolution.js` — `playEvolutionAnimation` (extrait de P3)
- **Quand le faire :** lors de l'ajout d'une feature non-triviale qui rend `app.js` ingérable (ex: système de quêtes, multi-langue avancé, refonte UI).
- **Effort estimé :** 1 jour avec tests de régression complets.
- **Risque :** moyen (logique pédagogique éprouvée à ne pas casser).

### Migration CodeMirror 5 → 6
- **État actuel** : CodeMirror 5.65.16 (deprecated, plus de maintenance active).
- **Quand le faire :** si CM5 commence à poser des bugs ou si on veut des features modernes (LSP, autocomplete avancée).
- **Effort estimé :** 0.5-1 jour.
- **Risque :** modéré, API très différente.

### Tests automatisés (smoke ou e2e)
- **État actuel** : tests manuels uniquement.
- **Quand le faire :** si le projet devient plus collaboratif ou si les régressions deviennent fréquentes.
- **Effort estimé :** 1-2 jours pour mettre en place Playwright + écrire les premiers tests.

### Refonte juridique (si projet devient public)
- **Quand le faire :** si on décide un jour de communiquer largement sur le projet, ou s'il commence à attirer de l'audience.
- **Travail nécessaire :** neutraliser noms Pokémon (variables, libellés UI), remplacer sprites officiels par illustrations originales, retirer mentions Mega/Gigantamax.
- **Effort estimé :** 1-2 jours.

---

## 📋 Récapitulatif

| Phase | Action | Temps | Risque | Indep. |
|---|---|---|---|---|
| **0** | Nettoyage fichiers parasites | 30 min | Nul | Oui |
| **1** | Suppression Phaser | 1-2h | Faible | Dépend P0 |
| **2** | Carte SVG S1 | 2 sessions | Moyen | Dépend P1 |
| **3** | Anim évolution + 4e palier + remplacement Dratini | 1-2 sessions | Moyen | Indep P2 |
| **4** | Cartes SVG S2+S3 (**conditionnelle**) | 1-2 sessions | Moyen | Dépend P2 + validation |
| **5** | Polish (optionnel) | 2h | Nul | Dépend P4 |

**Total : 4-6 sessions de 2h pour MVP complet et cohérent.**

**Ordre recommandé : P0 → P1 → P2 → P3 → (validation Basile) → P4 → P5 (optionnel).**

**Coupe-circuit :** si la Phase 2 déçoit après test avec Basile, **ne pas continuer en P4**.
