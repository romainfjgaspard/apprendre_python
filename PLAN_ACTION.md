# 🐍 Plan d'Action Complet — Python Quest v2

**Date** : 19/05/2026  
**Objectif** : Transformer Python Quest en plateforme multi-joueurs robuste, motivante et pédagogiquement optimisée

---

## 📋 Phase 1 — Nettoyage & Réorganisation (30 min)


### 1.2 — Réorganiser les fichiers Python support
```
apprendre_python/
├── web/                      # Application web (web app)
│   ├── index.html
│   ├── app.js
│   ├── chapters.json         # Contenu des chapitres
│   ├── style.css
│   ├── firebase.js
│   └── images/
├── server/                   # Nouveau dossier (optionnel)
│   ├── verification.py       # Service de vérification
│   └── __init__.py
├── _verify.py               # À migrer vers server/
├── export_web.py            # À migrer vers server/ (optionnel)
├── package.json             # Dépendances Python Quest pour éventuellement npm i
├── requirements.txt         # numpy, matplotlib (peu utilisés pour le web)
├── README.md                # À mettre à jour
├── AGENTS.md                # À créer
├── AGENTS-STATUS.md         # À créer
└── PLAN_ACTION.md          # Ce fichier
```
l'enorme fichier chapters.json est trés compliqué a maintenir et a modifier manuellement, il faut
---

## 📝 Phase 2 — Documentation Projet (20 min)

### 2.1 — Créer `AGENTS.md` (modèle: bredy_ludo)
Template fourni ci-dessous, adapté à Python Quest.

### 2.2 — Créer `AGENTS-STATUS.md`
État actuel du projet + timeline de développement.

### 2.3 — Mettre à jour `README.md`
- Bonnes commandes de lancement
- Accès au site web
- Instructions pour contributeurs

---

## 🏗️ Phase 3 — Architecture Multi-Joueurs (Planning)

### 3.1 — Modèle de données Firebase Firestore

**Collections et schéma** (inspiré de bredy_ludo) :

```
firestore
├── players/
│   └── {playerId}
│       ├── name: string                    # "Basile", "Anna"
│       ├── color: string                  # Couleur d'interface (#FF00FF)
│       ├── createdAt: timestamp           # Inscription
│       ├── lastActivity: timestamp        # Dernier accès
│       ├── level: number                  # Niveau XP actuel (0-7)
│       ├── xp: number                     # Points XP cumulés
│       ├── starter: {
│       │   pokemonId: number              # 1-151
│       │   name: string                   # "Pikachu"
│       │   currentXP: number              # XP de ce pokémon
│       │   evolution: number              # Palier (0=base, 1, 2)
│       │   capturedAt: timestamp
│       ├── progress: {
│       │   [chapterNum]: {
│       │     completed: boolean
│       │     score: number                # Points de succès (optionnel)
│       │     xpEarned: number
│       │     attempts: number
│       │     completedAt: timestamp
│       ├── leaderboardXP: number          # XP total visible (à jour mensuelle)
├── leaderboard/                            # Snapshot du classement
│   └── {monthYearKey} (ex: "202505")
│       └── {rank}__{playerId}            # "001__player123"
│           ├── name: string
│           ├── xp: number
│           ├── level: number
│           ├── snapshot_at: timestamp
```

### 3.2 — Flux utilisateur

1. **Arrivée** : Écran splash
   - Choisir un pseudo OU sélectionner un joueur existant
   - Sauvegarder playerId en localStorage

2. **Accueil** (page map)
   - Afficher: Nom joueur, niveau, XP, progression
   - Lien "Leaderboard 🏆"
   - Choisir pokémon starter à la première visite

3. **Chapitre**
   - Code **modifiable** (premier problème mentionné)
   - Vérification en temps réel
   - Gain XP au succès

4. **Leaderboard**
   - Top 10 des joueurs (par XP)
   - Filtrer par "cette semaine" / "ce mois" / "all-time"
   - Montrer: Rang, Nom, Niveau, XP

### 3.3 — Règles Firestore

```
match /players/{playerId} {
  allow read: if true;                         # Public leaderboard
  allow create: if request.auth.uid != null;  # Logged in (future)
  allow update: if request.auth.uid == playerId;
  allow delete: if false;
}
match /leaderboard/{document=**} {
  allow read: if true;
}
```

### 3.4 — Migration depuis localStorage

**Avant (playerId = localStorage + in-memory)** :
```javascript
let playerName = localStorage.getItem('playerName');
let progression = JSON.parse(localStorage.getItem('progression') || '{}');
```

**Après (Firestore) ** :
```javascript
import { getDoc, doc } from 'firebase/firestore';
const playerRef = doc(db, 'players', playerId);
const playerSnap = await getDoc(playerRef);
const player = playerSnap.data();
```

---

## 🎮 Phase 4 — Système Pokémon Motivant

### 4.1 — Évolutions des Pokémons par chapitre

**Système à 3-4 étapes par starter** :

| Starter | Chapitre 1 (50 XP) | Chapitre 4 (240 XP) | Chapitre 8 | Boss S1 |
|---------|-------------------|-------------------|----------|---------|
| Pikachu | 🥚 Pichu (50) | ⚡ Pikachu (240) | ⚡ Raichu (380) | ⚡ Raichu Master |
| Charmander | 🥚 Charmander (50) | 🔥 Charmeleon (240) | 🔥 Charizard (380) | 🔥 Mega Charizard |
| Squirtle | 🥚 Squirtle (50) | 💧 Wartortle (240) | 💧 Blastoise (380) | 💧 Mega Blastoise |

**Paliers de bossea** :
- **Boss Saison 1** (200 XP) → Évolution finale + titre "Pokémon Catcher" 

### 4.2 — Artwork / Images

Récupérer du dossier `../pokedex/images/` :
- Pokémons de base (première forme)
- Évolutions intermédiaires
- Formes finales

**Structure** :
```
web/images/pokemon/
├── 1_pichu.png           # Étape 0
├── 25_pikachu.png        # Étape 1 (Chapitre 4)
├── 26_raichu.png         # Étape 2 (Chapitre 8)
├── 4_charmander.png
├── 5_charmeleon.png
├── 6_charizard.png
└── ... (copies du pokedex)
```

### 4.3 — Affichage HUD mis à jour

```javascript
// Dans le HUD (top bar) :
<div class="pokemon-evolution">
  <img src="{pokemonImage}" height="40" />
  <div class="stats">
    <div>{pokemonName}</div>
    <div class="xp-bar">
      <div class="fill" style="width: {xpPercent}%"></div>
    </div>
    <small>{xp}/{xpNextLevel} XP</small>
  </div>
</div>
```

---

## 🐛 Phase 5 — Corrections Pédagogiques des Chapitres

### 5.1 — Problèmes à corriger

#### Level 3 — "Typo avec 2 symboles `%%`"
- **Localisation** : Exercise cell
- **Problème** : Dans les f-strings, `%%` → affiche un seul `%`
- **Solution** : Vérifier si c'est voulu (pour afficher pourcentage) ou typo
- **Fix** : Corriger le texte d'exmple dans le exercice

#### Level 4 — "Boucle `for` trop complexe, faire le lien avec Scratch"
- **Problème** : Range() + concepts imbriqués
- **Solution** stratégique** :
  1. **D'abord** : Boucler sur une liste → simple `for item in list:`
  2. **Ensuite** : Ajouter les indices `for i in range(len(list)):`
  3. **Finalement** : Introduire `range(n)` pour répéter N fois

- **Lien Scratch** : Ajouter exemple visuel / pseudo-code Scratch
  ```
  [répéter ▼ (5) fois]
    [ajouter (1) à niveau]
  ```

#### Level 4 — "Expliquer `len()`"
- **Manque** : Fonction `len()` non expliquée avant d'être utilisée en exercice
- **Solution** : Ajouter une leçon dédiée avant level 4
- **Contenu** : "Combien d'éléments dans ma liste ?"

#### Concept général — "Trop de concepts à la fois"
- **Règle à appliquer** : Max 1-2 nouveaux concepts par chapitre
- **À réviser** :
  - Level 4 : `for`, `while`, `range`, `break` = **4 concepts**
    - **Suggestion** : Split en 2 chapitres
      - Level 4A : `for` + listes simples
      - Level 4B : `while` + `break` + `range`
  - Level 5 : Listes + tri + compréhensions = **3 concepts**
    - **Suggestion** : Split aussi

### 5.2 — Restructuration pédagogique proposée

**Plan révisé (plus granulaire)** :

| Ch | Titre | Concept clé | Scratch équiv |
|----|-------|-------------|--------------|
| 1 | Hello | Print + vars | "say" |
| 2 | Types | Math + comparaisons | Opérateurs |
| 3 | Conditions | if/elif/else | if-then-else |
| 4A | Boucles sur listes | `for item in list` | "for each" |
| 4B | Boucles compteurs | `while`, `range`, `break` | "repeat until" |
| 5 | Listes avancées | append, remove, sort | list blocks |
| 6 | Dictionnaires | dicts + Pokédex | maps (custom blocks) |
| 7 | Fonctions | def + return | Custom blocks |
| 8 | Fichiers | JSON save/load | (no equiv) |
| 9🏆 | BOSS | Tout intégré | - |

### 5.3 — Ajout de non-modifiabilité (Phase future)

**Requête** : "les cellules qu'on peut lancer ne sont pas modifiables"

- **Contexte** : Les cells .md et code d'exemple doivent être READ-ONLY
- **Implémentation** : Dans `app.js`, ajouter flag `readonly: true` aux cells type `code` or `md`
  ```javascript
  if (cell.type === 'code' && !cell.isExercise) {
    codemirror.setOption('readOnly', true);
  }
  ```

---

## 🚀 Phase 6 — Implémentation Web (Priorité)

### 6.1 — Écran de sélection / accueil (Nouvelle)
**Fichier** : `web/pages/player-select.html` (optionnallement, UI dynamique)

UI :
1. Splash avec bouton "Nouveau joueur"
2. Input nom + bouton "Commencer"
3. OU Liste des joueurs existants (from localStorage ou Firebase)
4. Une fois sélectionné → localStorage.setItem('currentPlayerId', id)

### 6.2 — Leaderboard page (Nouveau)
**Fichier** : `web/leaderboard.html` (déjà existe ! vérifier contenu)

### 6.3 — Mise à jour du HUD pour afficher le Pokémon
**Fichier** : `web/app.js` (région du HUD)

### 6.4 — Intégration Firebase (Phase future)
- `web/firebase.js` : déjà existant (check s'il exporte `db`)
- Créer service : `web/services/playerService.js`
  - getPlayer(playerId)
  - saveProgress(playerId, chapterNum, xp)
  - listLeaderboard()
  - switchPlayer()

---

## ⚙️ Phase 7 — Variables d'environnement et déploiement

### 7.1 — `.env.local` (ou `.env.production`)

```
VITE_PYODIDE_URL=https://cdn.jsdelivr.net/pyodide/v0.23.4/full/
VITE_FIREBASE_API_KEY=...
VITE_FIREBASE_PROJECT_ID=...
```

### 7.2 — Règles Firestore pour production

```
match /players/{playerId} {
  allow read: if true;
  allow create: if request.auth != null;
  allow update: if request.auth.uid == resource.data.uid;
}
```

---

## 📊 Timeline estimée

| Phase | Durée | Priorité | Dépendance |
|-------|-------|----------|-----------|
| 1. Nettoyage | 30 min | 🔴 Haute | - |
| 2. Docs | 20 min | 🟡 Moyenne | Phase 1 |
| 3. Architecture | 2h (planning) | 🔴 Haute | Phase 2 |
| 4. Pokémon images | 1h | 🟡 Moyenne | pokedex/ |
| 5. Corrections pédago | 1-2h | 🟡 Moyenne | Phase 3 |
| 6. Dev web (Firebase) | 4-6h | 🔴 Haute | Phase 3 |
| 7. Déploiement | 1h | 🟡 Moyenne | Phase 6 |

**Total estimé** : 10-12 heures (2-3 jours de dev)

---

## 🎯 Résumé des priorités (ordre d'exécution recommandé)

1. ✅ **Phase 1** : Nettoyage (30 min)
2. ✅ **Phase 2** : Documentation (20 min)  → Fournir templates AGENTS.md
3. 📝 **Phase 5.1** : Lister les typos/bugs exact dans chapters.json
4. 🏗️ **Phase 3** : Architecture Firebase (design doc + branchement git)
5. 🎮 **Phase 4** : Collecte des images Pokemon du pokedex
6. 🚀 **Phase 6** : Implémentation web + Firebase (travail majeur)

---

## 👥 Responsabilités futures

| Item | Owner | Timeline |
|------|-------|----------|
| Correction level 3 (%) | - | Phase 5 |
| Images Pokemon avancées | - | Phase 4 |
| Firebase Firestore setup | - | Phase 6 |
| Leaderboard UI | - | Phase 6 |
| Testing/QA | - | Après Phase 6 |

---

## 🔗 Ressources annexes

- **Pokedex** : `../pokedex/images/` (les images existantes)
- **Bredy_ludo** : modèle de code Firebase Firestore prêt à copier
- **Pyodide** CDN : déjà intégré dans web/index.html (ligne 106)
- **CodeMirror** : déjà intégré (vérification read-only possible)

---

**Fin du plan. Prêt à démarrer Phase 1 ?**

