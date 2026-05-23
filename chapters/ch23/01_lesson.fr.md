# 🐦 Chapitre 23 — Les 3 Règles des Boids

Craig Reynolds a découvert que 3 règles simples créent un **vol en groupe réaliste** :

1. **Séparation** 🚫 — Ne pas percuter les voisins
2. **Alignement** ➡️ — Voler dans la même direction que les voisins
3. **Cohésion** 🧲 — Rester proche du centre du groupe

Chaque boid regarde ses **voisins** (les boids dans un certain rayon)
et ajuste sa vitesse.
