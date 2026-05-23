# Firebase Setup — Python Quest

Procédure pour créer ou recréer l'infra Firebase du projet.
Stack : Firestore uniquement (pas d'Auth, pas de Hosting).

---

## 1. Créer le projet Firebase

1. Aller sur [console.firebase.google.com](https://console.firebase.google.com)
2. **Ajouter un projet** → nom : `python-quest` (ou autre)
3. Google Analytics : facultatif (désactiver pour aller vite)

---

## 2. Créer la base Firestore

1. Menu gauche → **Firestore Database** → **Créer une base de données**
2. Mode de démarrage : **Production**
3. Région : `europe-west1` (Paris) ou `us-central1`

---

## 3. Règles de sécurité Firestore

Une fois Firestore créé → onglet **Règles** → remplacer par :

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /players/{playerId} {
      allow read: if true;
      allow write: if true;
    }
  }
}
```

→ **Publier**

> Pas d'authentification = tout le monde peut lire/écrire.
> Acceptable pour un projet perso/pédagogique. À durcir si le site devient public.

---

## 4. Enregistrer l'application web

1. **Paramètres du projet** (engrenage ⚙️) → onglet **Général**
2. Section **Tes applications** → icône **`</>`** (Web app)
3. Nom : `python-quest-web`
4. **Ne pas cocher** "Configurer Firebase Hosting" (on utilise GitHub Pages)
5. Copier le bloc `firebaseConfig`

---

## 5. Coller la config dans firebase.js

Ouvrir `firebase.js` et remplir `FIREBASE_CONFIG` (lignes ~16-22) :

```js
const FIREBASE_CONFIG = {
  apiKey: "AIzaSyBpjHG9PvRbfg-t1nqzmifDoPpQPnbhG-4",
  authDomain: "apprendre-python-f454a.firebaseapp.com",
  projectId: "apprendre-python-f454a",
  storageBucket: "apprendre-python-f454a.firebasestorage.app",
  messagingSenderId: "502890991106",
  appId: "1:502890991106:web:598ae7dba1954ddcbea11b"
};
```

SDK version utilisée : `12.13.0` (vérifier la dernière sur [firebase.google.com/docs](https://firebase.google.com/docs/web/setup))
`measurementId` (Analytics) non inclus — non utilisé dans le projet.

> Les credentials web Firebase sont publics par nature (visibles dans le navigateur).
> La sécurité repose sur les règles Firestore, pas sur le secret des credentials.

---

## Structure Firestore

Collection : `/players/{playerId}`

| Champ | Type | Description |
|-------|------|-------------|
| `name` | string | Nom affiché du joueur |
| `xp` | number | Points d'expérience totaux |
| `chapters_done` | number[] | Numéros des chapitres complétés |
| `badges` | string[] | Badges gagnés |
| `starter_pokemon` | string | Pokémon de départ (Tâche 9) |
| `lang` | string | Langue préférée : `"en"` ou `"fr"` |
| `updated_at` | timestamp | Dernière mise à jour |

`playerId` = nom en minuscules, caractères non-alphanumériques → `_`
(ex: `"Jean-Paul"` → `"jean_paul"`)
