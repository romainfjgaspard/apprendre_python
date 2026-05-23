# Plan de refonte — Python Quest
_Mis à jour le 2026-05-23 — document auto-suffisant pour exécution en nouvelle session_

## Contexte
Site d'apprentissage Python pour Basile (~11 ans, expert Scratch). Autres joueurs potentiels francophones.
Stack : HTML statique + Pyodide + CodeMirror + Firebase Firestore (à implémenter).
Repo cible : https://github.com/romainfjgaspard/apprendre_python.git (pas encore créé).
URL GitHub Pages cible : https://romainfjgaspard.github.io/apprendre_python/

## État actuel des fichiers
```
apprendre_python/
├── web/                        ← tout le site (à déplacer à la racine)
│   ├── index.html              ← GA4 G-HCG77H3QXB déjà en place
│   ├── leaderboard.html        ← GA4 G-HCG77H3QXB, contenu placeholder
│   ├── app.js                  ← moteur principal (719 lignes)
│   ├── chapters.json           ← source de vérité actuelle (26 chapitres)
│   ├── firebase.js             ← stub Realtime DB (à remplacer par Firestore)
│   ├── style.css
│   └── images/pokedex/         ← images Pokémon numérotées par ID Pokédex
├── chapter01.ipynb ... boss03.ipynb  ← notebooks source (récupérés depuis backup)
├── export_web.py               ← script de génération notebooks → chapters.json
├── _verify.py                  ← vérification locale (non utilisé dans browser)
├── PLAN_REFONTE.md             ← ce fichier
└── README.md
```
Pas de dépôt git encore initialisé.

---

## Tâche 1 — Restructurer le contenu (Option B : markdown + .py par chapitre)

### Pourquoi
Le `chapters.json` (1400 lignes) est illisible à éditer. Les notebooks `.ipynb` existent
mais sont aussi pénibles. La cible : des vrais fichiers `.md` et `.py` par chapitre.

### Structure cible
```
chapters/
  ch01/
    meta.json          ← { num, xp, badge, season, boss }
    01_intro.en.md
    01_intro.fr.md
    02_example.py      ← même fichier pour les 2 langues (le code ne se traduit pas)
    03_lesson.en.md
    03_lesson.fr.md
    04_exercise.py     ← contient les ???
  ch02/
    ...
```

### Règles de nommage
- Fichiers numérotés dans l'ordre d'affichage : `01_`, `02_`, `03_`...
- `.md` = cellule texte. Suffixe `.en.md` / `.fr.md` pour les deux langues.
- `.py` = cellule code (exemple ou exercice, détecté par présence de `???`)
- `meta.json` = métadonnées du chapitre (titre, XP, badge, saison)

### Mise à jour de export_web.py
Modifier pour lire `chapters/ch*/` au lieu des notebooks.
Pour chaque chapitre, parcourir les fichiers dans l'ordre numérique et construire les cells.
Générer `chapters.json` avec `source_en` et `source_fr` pour les cellules md,
et `source` unique pour les cellules code.

### Migration du contenu existant
Source de vérité pour la migration : `chapters.json` existant (plus à jour que les notebooks).
Créer un script `migrate_to_chapters.py` qui lit `chapters.json` et génère l'arborescence
`chapters/ch*/`. Les cellules md actuelles ont `source` en anglais → devient `source` dans
`01_lesson.en.md`. La traduction française sera faite manuellement après.

---

## Tâche 2 — Cellules toutes éditables
**Fichier** : `web/app.js` ligne ~282
```js
// Avant

readOnly: cell.type === "code",
// Après
readOnly: false,
```

---

## Tâche 3 — Déplacer web/ → racine
1. Déplacer tout le contenu de `web/` à la racine
2. Supprimer `web/`
3. Vérifier les chemins relatifs dans `index.html` et `leaderboard.html`
4. Créer `.gitignore` :
   ```
   *.pyc
   __pycache__/
   .env
   node_modules/
   ```


---

## Tâche 4 — Firebase Firestore multi-joueur

### Pourquoi Firestore et pas Realtime Database
Le stub actuel (`firebase.js`) utilise Realtime DB (ancien SDK compat).
Migrer vers **Firestore** pour cohérence avec `bredy_ludo` et montée en compétence.
Firestore = collections/documents, requêtes puissantes, SDK modulaire v9+.

### Pattern à suivre
Lire `~/projects/bredy_ludo/src/` pour le pattern `initializeApp` + `getFirestore`.
Credentials Firebase : même projet que bredy_ludo ou nouveau projet Firebase.
Les credentials web sont publics par nature (à mettre directement dans `firebase.js`).

### Modèle Firestore
```
/players/{playerName}/
  name: string
  xp: number
  chapters_done: number[]
  badges: string[]
  starter_pokemon: string
  lang: "en" | "fr"
  updated_at: timestamp
```

### Fonctions à implémenter dans firebase.js (remplacer entièrement)
```js
import { initializeApp } from "firebase/app"
import { getFirestore, doc, setDoc, getDoc, getDocs, collection, orderBy, query } from "firebase/firestore"

initFirebase()          → initialize app + firestore
syncProgress(prog)      → setDoc sur /players/{name}
loadPlayer(name)        → getDoc sur /players/{name}
listAllPlayers()        → getDocs sur /players/, tri par xp desc
```

Ces fonctions sont déjà appelées dans `app.js` :
- ligne ~703 : `initFirebase().then(...)`
- ligne ~119 : `syncProgress(prog)` dans `saveProgress()`

### Splash screen — comportement
1. Charger la liste des joueurs depuis Firestore (`listAllPlayers()`)
2. Afficher :
   - Champ texte "Nouveau dresseur — entre ton nom"
   - Dropdown "Dresseur existant" (peuplé depuis Firestore)
   - Sélecteur de langue EN/FR (persiste dans le profil Firestore)
3. Nouveau nom → créer document + choisir starter Pokémon → démarrer
4. Nom existant → charger progression depuis Firestore → démarrer

---

## Tâche 5 — Leaderboard
**Fichier** : `leaderboard.html` (à réécrire, placeholder actuel)

Lire `/players/` via `listAllPlayers()` et afficher :
| Rang | Nom | Pokémon (niveau) | XP | Chapitres complétés |
Lien "← Retour" vers `index.html`.
Bouton refresh.

---

## Tâche 6 — Contenu bilingue EN/FR complet

### Principe
L'i18n actuel traduit l'interface (labels, boutons). Étendre aux cellules de contenu.

### Dans chapters.json (généré par export_web.py)
Les cellules `md` auront deux champs :
```json
{ "type": "md", "source_en": "## Lesson 1 — print()", "source_fr": "## Leçon 1 — print()" }
```
Les cellules `code` et `exercise` ont un seul `source` (le code Python est universel).

### Dans app.js
Remplacer `cell.source` par `cell[LANG === "fr" ? "source_fr" : "source_en"] || cell.source`
Quand le joueur change de langue → re-rendre le chapitre courant.

### Contenu des fichiers .md
- `.en.md` : contenu en anglais (Basile joue en anglais)
- `.fr.md` : contenu en français (autres joueurs)
- Les commentaires dans les `.py` : en anglais (les noms de variables restent en anglais,
  les commentaires explicatifs peuvent être bilingues ou choisis à l'écriture)

---

## Tâche 7 — Fixes pédagogiques (chapters.json / fichiers markdown)

### 7a — Ch2 : HP/Score confusion
Exercice chapitre 2 : renommer `score` → `pokemon_hp`, `new_score` → `hp_after_damage`,
`final_score` → `hp_after_healing`. Mettre à jour `_ch2` dans VERIFY_PY_SOURCE (app.js ~506).

### 7b — Ch4 : Splitter boucles for/while
**Ch4 nouveau — Boucle for uniquement** :
1. `for pokemon in ["Pikachu", "Salameche"]:` — analogie Scratch "pour chaque élément"
2. `for i in [0, 1, 2, 3, 4]:` — compter manuellement
3. `range(5)` — raccourci qui fait la même chose
→ Retirer `while`, `break`, `for/else`

**Ch4b nouveau — Boucle while** (insérer avec num 4.5 ou renuméroter) :
1. Analogie Scratch "répéter jusqu'à"
2. `while hp > 0:` — bataille Pokémon
3. `break` — sortir tôt
→ Pas de `for/else`

### 7c — Ch5 : List comprehensions optionnelles
Marquer la leçon 4 "⭐ Bonus — pour les curieux" et la retirer de l'exercice obligatoire.

### 7d — Ch6 : Lambda trop tôt
Remplacer `max(pokedex, key=lambda p: p["attack"])` par une boucle explicite.
Lambda revient en Ch11 où il est enseigné.

### 7e — Ch8 : File I/O → localStorage / JSON en mémoire
`open()` ne fonctionne pas dans Pyodide. Reformuler :
- Leçon 1 : `json.dumps()` / `json.loads()` (sérialisation en mémoire)
- Leçon 2 : concept de sauvegarde → `localStorage` comme équivalent navigateur
- Garder les exemples `open()` mais les baliser "⚠️ Ceci fonctionne sur Python local (ex: PyCharm)"

### 7f — Apothéose visuelle à chaque fin de chapitre

**Principe** : compléter un chapitre doit provoquer un "wow". Scratch est gratifiant
visuellement à chaque action — Python Quest doit rivaliser. Le modal de victoire actuel
("Score: 5/5 +50 XP") est insuffisant. Chaque chapitre doit se terminer par quelque chose
de visuellement fort, adapté à la saison.

**Saison 1 — Pokémon** :
- Fin de chapitre → animation CSS de l'image du starter (bounce, glow, particules XP)
- Boss Ch9 → battle animée entre deux Pokémon avec barres HP qui descendent
- Si le joueur débloque une évolution → cinématique d'évolution (image avant → image après,
  effet flash, son)

**Saison 2 — F1** :
- matplotlib fonctionne en statique dans Pyodide (génère un PNG)
- Fin de chapitre → le graphique généré s'affiche en grand dans le modal de victoire
- Boss Ch17 → podium animé F1 avec les 3 premiers du championnat simulé

**Saison 3 — Boids (canvas HTML)** :
`FuncAnimation` de matplotlib ne s'affiche pas dans Pyodide/navigateur.
**Solution retenue : canvas HTML piloté depuis Python via Pyodide.**

Pyodide permet d'appeler le DOM depuis Python :
```python
from js import document, requestAnimationFrame
canvas = document.getElementById("sim-canvas")
ctx = canvas.getContext("2d")
ctx.fillRect(x, y, 5, 5)
```

Chaque chapitre de la Saison 3 se termine avec la simulation canvas en direct.
La progression est visible : Ch18 = 1 objet qui bouge, Ch22 = 10 boids, Ch26 = 50 boids
+ prédateur + sliders interactifs.

**Implémentation technique** :
- Ajouter `<canvas id="sim-canvas" width="600" height="400">` dans le template de chapitre
- Visible uniquement pour les chapitres de Saison 3 (attribut `season: 3` dans meta.json)
- Boucle d'animation : `requestAnimationFrame` côté JS, appelé depuis Python via Pyodide bridge

---

## Tâche 8 — UX / Gamification

### 8a — Bouton "Tout exécuter depuis le début"
Les cellules partagent le même namespace Pyodide. Si Basile exécute la cellule 5
avant la cellule 2, il a des `NameError` confus.
Ajouter un bouton "▶ Tout exécuter" en haut du chapitre qui exécute toutes les cellules
dans l'ordre (sauf les verify).

### 8b — Préchargement Pyodide
Lancer `ensurePyodide()` en arrière-plan dès que l'utilisateur ouvre un chapitre
(pas au premier clic sur "▶ Run"). Pendant la lecture de la leçon, Pyodide charge silencieusement.

### 8c — Aide-mémoire Scratch → Python (sidebar)
Bouton "📋 Scratch?" dans le HUD, ouvre un panneau latéral :
| Scratch | Python |
|---------|--------|
| `dire "Bonjour"` | `print("Bonjour")` |
| `répéter 10 fois` | `for i in range(10):` |
| `si <> alors` | `if condition:` |
| `attendre jusqu'à` | `while not condition:` |
| `variable = valeur` | `variable = valeur` |
| `ma liste` | `ma_liste = []` |
Contenu statique, facile à enrichir.

### 8d — Panneau "Mon parcours" joueur
Accessible depuis le HUD (icône profil), affiche :
- Pokémon actuel + XP + niveau
- Liste des concepts maîtrisés (déduits des chapitres complétés) :
  ex: "✅ print() ✅ Variables ✅ f-strings ✅ Conditions..."
- Badges gagnés avec leur chapitre source
- Progression dans chaque saison (ex: "Saison 1 : 5/9 chapitres")
Données déjà disponibles dans `PROG.chapters_done` — juste du rendu.

---

## Tâche 9 — Progression Pokémon avec évolution
À faire en dernier (dépend de Firebase et du contenu stable).

- Au démarrage (nouveau joueur) : choisir son Pokémon starter
- Consulter `~/projects/pokedex/` pour la liste des Pokémon disponibles + évolutions
- Images disponibles dans `images/pokedex/` (numérotées par ID Pokédex)
- Le Pokémon évolue automatiquement aux seuils XP déjà définis dans `LEVELS` (app.js)
- Afficher l'image dans le HUD et l'écran de victoire

---

## Push final
```bash
git add .
git commit -m "feat: refonte complète Python Quest"
git push -u origin main
```
Activer GitHub Pages : branche `main`, dossier `/`.
