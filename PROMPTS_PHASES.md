# Prompts d'exécution — Migration SVG

> Chaque prompt ci-dessous est conçu pour être collé tel quel dans un **nouveau chat Claude Code** ouvert dans `~/projects/apprendre_python`.
>
> Le prompt référence `PLAN_MIGRATION_SVG.md` comme source de vérité. L'agent doit lire le plan, exécuter UNIQUEMENT la phase demandée, lancer les tests, mettre à jour le statut, et committer.

---

## 🟢 Prompt Phase 0 — Nettoyage immédiat

```
Tu travailles sur ~/projects/apprendre_python.

Lis le fichier `PLAN_MIGRATION_SVG.md` à la racine du projet — c'est la source de vérité de la migration en cours.

Ta mission : exécuter UNIQUEMENT la **Phase 0 — Nettoyage immédiat**.

Étapes :
1. Lis l'intégralité de `PLAN_MIGRATION_SVG.md` pour comprendre le contexte global et les 18 décisions validées.
2. Concentre-toi sur la section "PHASE 0 — Nettoyage immédiat" : objectif, fichiers à modifier/supprimer, contraintes, Definition of DONE.
3. Exécute la phase exactement comme spécifié.
4. Respecte STRICTEMENT les contraintes "Ne PAS toucher au code" — cette phase ne touche aucun fichier de code.
5. Lance les tests manuels listés.
6. Mets à jour `AGENTS-STATUS.md` (Phase 0 marquée done + section "Migration overworld → SVG en cours" avec les 5 phases listées).
7. Fais le commit avec le message indiqué dans la Definition of DONE.
8. Termine par un résumé court : fichiers modifiés/supprimés/déplacés + état des tests.

Ne fais PAS les autres phases. Ne refactore rien.
```

---

## 🔴 Prompt Phase 1 — Suppression de Phaser

```
Tu travailles sur ~/projects/apprendre_python.

Lis le fichier `PLAN_MIGRATION_SVG.md` à la racine du projet — c'est la source de vérité.

Ta mission : exécuter UNIQUEMENT la **Phase 1 — Suppression de Phaser, retour temporaire à la snake grid S1**.

Prérequis : Phase 0 exécutée. Vérifie via `git log --oneline` que le commit "chore: nettoyage avant migration SVG (Phase 0)" existe. Sinon, arrête-toi et signale.

Étapes :
1. Lis l'intégralité de `PLAN_MIGRATION_SVG.md` pour le contexte (18 décisions validées).
2. Concentre-toi sur la section "PHASE 1" : objectif, fichiers à modifier/supprimer, contraintes, pièges, Definition of DONE.
3. Avant chaque suppression de référence `window.PROG` / `window.DATA` / `window.getPokemonForm` : vérifie avec `grep` qu'aucun autre code ne les utilise. Si encore utilisés, garde-les.
4. Exécute toute la phase.
5. Lance la checklist de régression complète (section "🧪 Checklist régression" du plan) + les tests spécifiques à la Phase 1.
6. Vérifie avec `grep -r "Phaser\|phaser\|OverworldScene\|FROM_OVERWORLD\|openChapterFromOverworld\|returnToOverworld\|destroyOverworld\|openOverworld\|enter-overworld-btn\|overworld-screen" .` que tout est nettoyé (0 résultats hors `_archive/` et docs).
7. Mets à jour `AGENTS-STATUS.md` (Phase 1 done).
8. Fais le commit avec le message indiqué.
9. Résume : fichiers modifiés/supprimés + résultat de la régression + résultat du grep final.

Contexte décisions clés (pour info, voir plan pour détail) :
- Repo public familial, noms Pokémon conservés.
- PC/Mac uniquement (pas de contraintes mobile).
- Aucun refactor préventif d'`app.js`.

Ne fais PAS la Phase 2 (carte SVG). À ce stade, S1 doit afficher la snake grid (comme S2 et S3).
```

---

## 🎨 Prompt Phase 2 — Carte SVG Saison 1

```
Tu travailles sur ~/projects/apprendre_python.

Lis le fichier `PLAN_MIGRATION_SVG.md` à la racine du projet — c'est la source de vérité.

Ta mission : exécuter UNIQUEMENT la **Phase 2 — Carte SVG S1 (remplace la snake grid S1)**.

Prérequis : Phase 1 exécutée. Vérifie via `git log --oneline` que le commit "chore: suppression Phaser + overworld (Phase 1)" existe. Sinon, arrête-toi et signale.

Étapes :
1. Lis l'intégralité de `PLAN_MIGRATION_SVG.md`. Concentre-toi sur la section "PHASE 2".
2. Implémente la spec de la carte SVG S1 (layout vertical, 10 zones avec leurs noms et thèmes, états visuels, hotspots accessibles).
3. Crée `map.js` (~250 lignes max, vanilla JS, exposé via `window.renderSeasonMap`).
4. Modifie `index.html`, `app.js`, `style.css` selon la spec.
5. S2 et S3 doivent rester en snake grid intactes (migration en Phase 4 conditionnelle).
6. Lance les tests manuels listés (régression + Phase 2 spécifiques).
7. Tests d'affichage : devtools Chrome à 1280×800 et 1920×1080. **Pas de tests mobile** (PC seul, décision 2).
8. Tests a11y : Tab navigue entre hotspots, Enter active, `aria-label` présent.
9. Mets à jour `AGENTS-STATUS.md` (Phase 2 done).
10. Fais le commit avec le message indiqué.
11. Résume : fichiers créés/modifiés + résultat tests + description de la carte rendue.

Contraintes critiques (résumé du plan, voir détail) :
- Ne pas toucher à la structure de `PROG`.
- Ne pas migrer S2/S3.
- Vanilla JS uniquement, aucune lib externe.
- `transform` only pour les animations.
- Respecter `data-i18n` pour les libellés EN+FR.
- Taille hotspots ~80×80 px (PC confort, pas mobile).
- Aucun refactor préventif d'`app.js`.
```

---

## ✨ Prompt Phase 3 — Animation d'évolution + 4e palier + remplacement Dratini

```
Tu travailles sur ~/projects/apprendre_python.

Lis le fichier `PLAN_MIGRATION_SVG.md` à la racine du projet — c'est la source de vérité.

Ta mission : exécuter UNIQUEMENT la **Phase 3 — Animation d'évolution + ajout 4e palier + remplacement Dratini**.

⚠️ Cette phase combine 3 changements liés :
1. Remplacement de Dratini par Charmander dans `STARTERS` (Dratini n'a pas de Mega officielle, Charmander oui).
2. Ajout d'une 4e forme d'évolution à XP 1000 pour les 4 starters (Mega Charizard X, Mega Blastoise, Ash-Greninja, Mega Salamence).
3. Animation cinématique d'évolution déclenchée à chaque transition de forme.

Prérequis : Phase 1 exécutée (Phaser retiré). Phase 2 n'est PAS un prérequis (phase indépendante).

Étapes :
1. Lis l'intégralité de `PLAN_MIGRATION_SVG.md`. Concentre-toi sur la section "PHASE 3".
2. **D'abord** : télécharge les 7 nouveaux sprites nécessaires (Charmander 4, Charmeleon 5, Charizard 6, Mega Charizard X, Mega Blastoise, Ash-Greninja, Mega Salamence). Sources autorisées : PokeAPI ou Bulbapedia (PNG transparents officiels).
3. Mets à jour `STARTERS` dans `app.js` :
   - Retire Dratini (id 147)
   - Ajoute Charmander (id 4) avec 4 formes (XP 0, 150, 500, 1000)
   - Étends les 3 autres starters (Squirtle, Froakie, Bagon) avec une 4e forme à XP 1000
4. Ajoute la migration save dans `loadProgress()` : si `starter_pokemon === 147`, le remplace par 4 (Charmander), saveProgress, et affiche une notification douce.
5. Implémente l'overlay HTML, le CSS (~80 lignes), la logique JS de détection d'évolution dans `showVictory()`.
6. Ajoute les clés i18n EN+FR : `evolution_intro`, `evolution_arrow`, `evolution_continue`, `dratini_migration`.
7. Respecte `prefers-reduced-motion` (juste swap des sprites si activé).
8. **Teste les 4 starters** (Charmander 4, Squirtle 7, Froakie 656, Bagon 371) et leurs **3 transitions** (XP 150, 500, 1000) = **12 cas**.
   - Procédure : ouvre la console, fais `PROG.xp = 100; saveProgress(PROG);` puis reload. Complète un chapitre rapportant ≥50 XP. Vérifie l'anim. Répète pour XP=450 et XP=950.
9. **Teste la migration Dratini** : `PROG.starter_pokemon = 147; saveProgress(PROG);` puis reload → doit afficher Charmander + notif.
10. Teste qu'un chapitre rejoué NE déclenche PAS l'anim.
11. Teste skip via Enter, Space, et clic sur overlay.
12. Lance la checklist de régression complète.
13. Mets à jour `AGENTS-STATUS.md` (Phase 3 done).
14. Fais le commit avec le message indiqué.
15. Résume : fichiers créés (sprites) + modifiés + résultat des 12 cas + résultat migration Dratini + tests régression.

Contraintes critiques :
- Ne PAS modifier `PROG` schema (la migration Dratini change juste la VALEUR de starter_pokemon).
- Ne PAS utiliser `top/left` pour animer (GPU only via `transform`/`opacity`).
- L'overlay s'affiche PAR-DESSUS la victory modal, pas à la place.
- Migration Dratini doit s'exécuter UNE seule fois (sinon notif à chaque load).
- EN+FR pour tous les libellés.
```

---

## 🌍 Prompt Phase 4 — Cartes SVG Saisons 2 + 3 (CONDITIONNELLE)

```
Tu travailles sur ~/projects/apprendre_python.

Lis le fichier `PLAN_MIGRATION_SVG.md` à la racine du projet — c'est la source de vérité.

⚠️ AVANT TOUT : cette phase est CONDITIONNELLE. Vérifie avec l'utilisateur :
1. Que Basile a testé la carte S1 (Phase 2) et qu'elle lui plaît.
2. Que le nombre exact de chapitres S2 et S3 est confirmé (peut bouger après feedback).
3. Que les noms de zones S2 et S3 sont validés (les noms dans le plan sont des SUGGESTIONS).

Si l'une de ces conditions n'est pas remplie, ARRÊTE-TOI et signale à l'utilisateur qu'il faut d'abord valider les specs S2/S3.

Ta mission (si conditions OK) : exécuter UNIQUEMENT la **Phase 4 — Cartes SVG S2 + S3 (suppression définitive snake grid)**.

Prérequis techniques : Phase 2 exécutée. Vérifie via `git log --oneline` que le commit "feat: carte SVG saison 1 (Phase 2)" existe.

Étapes :
1. Lis l'intégralité de `PLAN_MIGRATION_SVG.md`. Concentre-toi sur la section "PHASE 4".
2. Confirme avec l'utilisateur les specs finales S2 et S3 (noms zones + nombre).
3. Étends `map.js` avec `MAPS.s2` (F1, layout serpentin Monaco-style) et `MAPS.s3` (Birds, montée vers ciel) selon les specs validées.
4. Factorise proprement le rendu via un paramètre `theme` — pas d'overengineering : `if/else` sur `theme` est OK.
5. Modifie `index.html` (remplace `#grid-s2` et `#grid-s3` par `#map-s2` et `#map-s3`).
6. Dans `app.js`, simplifie `renderMap()` à `updateHUD(); renderSeasonMap('s1'); renderSeasonMap('s2'); renderSeasonMap('s3');`. Supprime toute la logique snake grid (boucles rows, displayOrder, arrowChar, tile-spacer, création .map-tile, event listeners).
7. Dans `style.css`, supprime les classes snake grid (`.map-grid`, `.map-row`, `.arrow-h`, `.tile-spacer`, `.map-tile` et variantes). Ajoute les classes thématiques `.season-map[data-theme="f1"]` et `[data-theme="birds"]`.
8. AVANT de supprimer du CSS, exécute `grep -rn "\.map-grid\|\.map-tile\|arrow-h\|tile-spacer" .` (hors `_archive/`) pour identifier toutes les références. Supprime-les toutes.
9. Lance la checklist de régression complète + tests Phase 4 (3 saisons en SVG, click chapitre 11 et 22, Tab).
10. Vérifie final : `grep -r "\.map-grid\|\.map-tile\|arrow-h\|tile-spacer" .` doit retourner 0 résultats hors `_archive/`.
11. Mets à jour `AGENTS-STATUS.md` (Phase 4 done + mention "snake grid retirée définitivement").
12. Fais le commit avec le message indiqué.
13. Résume : fichiers modifiés + résultat grep final + tests.

Contraintes critiques :
- Ne PAS toucher au système d'évolution (Phase 3 indépendante, ne pas régresser).
- Ne PAS toucher à `PROG`, `firebase.js`, `leaderboard.html`, `chapters/`.
- Ne PAS overengineer la factorisation des thèmes.
- Contraste WCAG AA min pour S2 (ambiance sombre).
- EN+FR pour les nouveaux libellés.
```

---

## 🎁 Prompt Phase 5 — Polish (optionnel)

```
Tu travailles sur ~/projects/apprendre_python.

Lis le fichier `PLAN_MIGRATION_SVG.md` à la racine du projet — c'est la source de vérité.

Ta mission : exécuter UNIQUEMENT la **Phase 5 — Polish (sons + sprite ambulant)**.

⚠️ Phase optionnelle. Ne lance cette phase QUE si l'utilisateur le demande explicitement (Basile utilise activement le produit et veut "plus").

Prérequis : Phase 4 exécutée. Vérifie via `git log --oneline` que le commit "feat: cartes SVG saisons 2 et 3 + suppression snake grid (Phase 4)" existe. Sinon, arrête-toi et signale.

Étapes :
1. Lis l'intégralité de `PLAN_MIGRATION_SVG.md`. Concentre-toi sur la section "PHASE 5".
2. Génère ou trouve 3 fichiers audio CC0 : `audio/click.wav`, `audio/victory.wav`, `audio/evolution.wav`. Total ≤ 100 KB. Sources autorisées : sfxr (chiptune), freesound.org CC0. **JAMAIS de samples Pokémon officiels.**
3. Ajoute le toggle 🔊/🔇 dans le HUD, persisté dans `PROG.audio_enabled`. **Default `false` (sons OFF par défaut)**.
4. Implémente les triggers audio (click hotspot, victory, evolution) — ils ne jouent QUE si `PROG.audio_enabled === true`.
5. Implémente le sprite ambulant S1 dans `map.js` :
   - Mini sprite du starter qui trotte sur le chemin entre dernière zone complétée et "current"
   - Animation CSS `@keyframes walk-path` avec `offset-path: path(...)`
   - Apparaît à l'arrivée sur home, dure ~2s, puis disparaît
6. Respecte `prefers-reduced-motion` : désactive l'anim.
7. Lance les tests : sons OFF au premier lancement, toggle active, persistant après reload, sprite ambulant visible, reduced-motion désactive.
8. Lance la checklist de régression complète.
9. Mets à jour `AGENTS-STATUS.md` (Phase 5 done).
10. Fais le commit avec le message indiqué.
11. Résume : fichiers créés/modifiés + résultat tests.

Contraintes critiques :
- Aucun sample Pokémon officiel (juridique).
- Pas de musique de fond.
- **Sons OFF par défaut** (décision 16 validée).
```

---

## 🔄 Comment utiliser ces prompts

1. Ouvre un nouveau chat Claude Code dans le dossier projet (`cd ~/projects/apprendre_python && claude`).
2. Copie-colle le prompt correspondant à la phase à exécuter.
3. Laisse l'agent travailler. Il lit `PLAN_MIGRATION_SVG.md`, exécute, teste, commite.
4. Vérifie le résumé final. Si OK, passe à la phase suivante dans un nouveau chat.
5. Si l'agent signale un problème (prérequis manquant, test échoué), traite-le avant de passer à la suivante.

**Avant de lancer la Phase 4 :** valider avec Basile que la carte S1 fonctionne et que les specs S2/S3 sont confirmées (nombre/noms de chapitres).

**Astuce :** entre deux phases, tu peux faire jouer Basile une session pour valider l'expérience. Si l'effet ne te plaît pas, le coupe-circuit est documenté dans `PLAN_MIGRATION_SVG.md` (notamment : ne pas continuer en P4 si la P2 déçoit).
