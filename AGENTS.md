# AGENTS.md — Python Quest

## Présentation du projet

**Python Quest** est une plateforme pédagogique web interactive pour apprendre Python par la création de projets Pokémon, Formule 1 et simulations d'oiseaux (boids).

- **URL** : À déployer sur GitHub Pages (en cours de configuration)
- **Repo** : `code/apprendre_python/` 
- **Stack** : HTML5 + JavaScript (vanilla) + Pyodide (Python WASM) + Firebase Firestore (futur) + CodeMirror
- **Public** : Enfants/adolescents (11+) ayant expérience Scratch

## Fonctionnalités principales actuelles

| Section | Description | État |
|---------|-------------|------|
| **Map** | Affichage des 3 saisons (Pokémon, F1, Boids) avec progression | ✅ Fonctionnel |
| **Chapitres** | Contenu interactif : leçons + code exécutables + exercices | ✅ Fonctionnel |
| **Exécution Python** | Pyodide (Python 3.11 WASM) dans le navigateur | ✅ Fonctionnel |
| **Vérification** | `_verify.py` valide les exercices côté Python | ✅ Fonctionnel |
| **XP & Niveaux** | localStorage (temporaire) → Firestore (futur) | 🟡 Incomplet |
| **Leaderboard** | Classement multi-joueurs | ❌ Planifié |
| **Sélecteur joueur** | Pas de multi-joueurs aujourd'hui | ❌ Planifié |
| **Pokémon starter** | Pas de personnalisation (futur) | ❌ Planifié |

## Architecture actuelle

```
apprendre_python/
├── web/
│   ├── index.html                # Point d'entrée (splash + map + chapter)
│   ├── leaderboard.html          # Page leaderboard (templat e existant)
│   ├── app.js                    # Engine principal (~720 lignes)
│   ├── firebase.js               # Config Firebase (stub)
│   ├── chapters.json             # Contenu (1400+ lignes)
│   ├── style.css                 # Design (Tailwind-like)
│   └── images/
│       ├── pokedex/              # Images Pokémon
│       └── heat/                 # Images formule 1
├── _verify.py                    # Service vérification exercices
├── export_web.py                 # Utilitaire (non-utilisé)
├── requirements.txt              # numpy, matplotlib (pour export)
└── README.md                      # (À mettre à jour)
```

## Modèle d'apprentissage (3 saisons)

### Saison 1 — Pokémon Edition (Chapitres 1-9)
- **Objectif** : Maîtriser bases Python (print, variables, types, conditionnels, boucles, lists, dicts, fonctions, fichiers)
- **Thème** : Construire une arena Pokémon
- **Niveaux** : 8 chapitres + 1 boss = progression gamifiée

### Saison 2 — Formule 1 (Chapitres 10-17)
- **Objectif** : Données avancées (nested lists, lambda, modules, matplotlib, pandas, CSV)
- **Thème** : Simuler une saison F1 + dashboard
- **Format** : Chapitres progressifs + boss

### Saison 3 — Birds Simulation / Boids (Chapitres 18-26)
- **Objectif** : OOP avancée (classes, héritage, numpy, animation, interactivité)
- **Thème** : Simuler flockinga d'oiseau avec règles d'émergence
- **Format** : Chapitres + boss final

## Système de progression (à améliorer)

### Actuel (localStorage)
```javascript
{
  "playerName": "Basile",
  "progression": {
    "1": { "completed": true, "xp": 50 },
    "2": { "completed": true, "xp": 60 },
    ...
  },
  "xp_total": 500
}
```

### Futur (Firestore)
- **Collection** : `players/{playerId}`
- **Champs** : name, xp, level, starter_pokemon, created_at, last_activity
- **Sous-collection** : `players/{playerId}/progress/{chapterId}`
- **Leaderboard snapshot** : Collection séparée pour classement (optimisation lecture)

## Contenus des chapitres (chapters.json)

**Format par chapitre** :
```json
{
  "num": 1,
  "title": "⚡ Hello Pokémon",
  "desc": "print, variables, f-strings",
  "xp": 50,
  "season": 1,
  "boss": false,
  "cells": [
    { "type": "md", "source": "..." },
    { "type": "code", "source": "...", "readonly": false },
    { "type": "exercise", "source": "..." },
    { "type": "verify", "source": "from _verify import verify\nverify(1, locals())" }
  ]
}
```

**Types de cells** :
- `md` : Markdown (leçon)
- `code` : Code Python exécutable (exemple, readonly)
- `exercise` : Code à compléter (modifiable)
- `verify` : Appel vérification

## Variables d'environnement (.env / config)

Actuellement : **aucune**  
Futur (Firebase) :
```
VITE_FIREBASE_API_KEY=...
VITE_FIREBASE_AUTH_DOMAIN=...
VITE_FIREBASE_PROJECT_ID=...
VITE_FIREBASE_STORAGE_BUCKET=...
VITE_FIREBASE_APP_ID=...
```

## Commandes clés

```bash
# Développement
npm run dev                # Serveur local (si setup npm)
python -m http.server     # Serveur HTTP simple (Python)

# Export/Génération (futurs)
npm run build             # Build production
npm run export:web        # Exporter chapters.json
```

## Conventions de code

- **Langue** : Anglais (code), français (UI/lectures)
- **Fichiers chapitres** : `chapters.json` centralisé (pas de notebooks .ipynb)
- **Images** : `web/images/{pokedex,heat,pokemon}/`
- **Vérification** : `_verify.py` (Python côté serveur, futur Pyodide)

## Points techniques clés

### Pyodide (Python dans le navigateur)
- **CDN** : jsdelivr.net
- **Version** : 0.23.4+
- **Délai** : ~3-5s au premier chargement (cache après)
- **Modules** : Standard library (json, random, csv, etc.), + numpy, matplotlib

### CodeMirror (Éditeur)
- **Version** : 5.x (CDN)
- **Mode** : Python
- **Thème** : Dracula
- **Feature future** : `readOnly: true` pour leçons

### Firebase (futur)
- **Projet** : À créer
- **Région** : europe-west9 (Paris)
- **Auth** : Pas d'auth pour MVP (localStorage)
- **Firestore** : Structure définie dans PLAN_ACTION.md

## Problèmes connus (MVP)

1. **XP/Score confusion** : Concepts mélangés dans code (à clarifier)
2. **Level 3** : Typo `%%` (vérifier si intentionnel)
3. **Level 4** : Trop de concepts (for, while, range, break = 4 d'un coup)
4. **len() not explained** : Utilisé avant d'être présenté
5. **Pas de modifiabilité sélective** : Toutes les cells sont modifiables
6. **Pas de multi-joueurs** : Progression per-browser uniquement
7. **Pas d'images Pokémon custom** : Affichage statique

## Roadmap à court terme

- [ ] Nettoyage : Supprimer .ipynb obsolètes
- [ ] Firebase Firestore : Setup structure données multi-joueurs
- [ ] Sélecteur joueur : Splash screen + liste joueurs
- [ ] Pokémon starter : UI + evolutions
- [ ] Leaderboard : Top 10 + filters (week/month/all-time)
- [ ] Améliorations pédago : Split level 4 & 5, fix typos, readonly cells
- [ ] CI/CD : GitHub Actions → GitHub Pages

## Ressources utiles

- **Pokedex images** : code/pokedex/images/
- **Bredy_ludo** : Modèle Firebase (code/bredy_ludo/)
- **Pyodide docs** : https://pyodide.org
- **CodeMirror** : https://codemirror.net/5/

## Contact & Questions

- **Auteur initial** : Créé pour Basile (11 ans)
- **Contexte** : Progression Scratch → Python
- **Vision** : Gamification + apprentissage progressif + pair programming potentiel

---

**Dernière mise à jour** : 19/05/2026  
**Responsable** : À définir

