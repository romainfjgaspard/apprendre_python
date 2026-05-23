# 🐦 Chapter 23 — The 3 Rules of Boids

Craig Reynolds discovered that 3 simple rules create **realistic flocking**:

1. **Separation** 🚫 — Don't crash into neighbours
2. **Alignment** ➡️ — Fly in the same direction as neighbours
3. **Cohesion** 🧲 — Stay close to the centre of the group

Each boid looks at its **neighbours** (boids within a certain distance)
and adjusts its velocity.