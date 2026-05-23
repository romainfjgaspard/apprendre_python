/* ═══════════════════════════════════════════════════════════════════════════
   Python Quest — Firebase Firestore (SDK modulaire v9+)
   Chargé comme <script type="module"> — fonctions exposées sur window.
   Si aucune config, tout fonctionne hors-ligne via localStorage.
   ═══════════════════════════════════════════════════════════════════════════ */

import { initializeApp }
  from "https://www.gstatic.com/firebasejs/12.13.0/firebase-app.js";
import { getFirestore, doc, setDoc, getDoc, getDocs, collection, query, orderBy }
  from "https://www.gstatic.com/firebasejs/12.13.0/firebase-firestore.js";

// ── Config Firebase ──────────────────────────────────────────────────────────
const FIREBASE_CONFIG = {
  apiKey: "AIzaSyBpjHG9PvRbfg-t1nqzmifDoPpQPnbhG-4",
  authDomain: "apprendre-python-f454a.firebaseapp.com",
  projectId: "apprendre-python-f454a",
  storageBucket: "apprendre-python-f454a.firebasestorage.app",
  messagingSenderId: "502890991106",
  appId: "1:502890991106:web:598ae7dba1954ddcbea11b"
};

let fbDb = null;
let fbEnabled = false;

function playerId(name) {
  return name.toLowerCase().replace(/[^a-z0-9]/g, "_");
}

// ── Initialisation ────────────────────────────────────────────────────────────
async function initFirebase() {
  if (!FIREBASE_CONFIG.apiKey) {
    console.log("[Firebase] Pas de config — mode hors-ligne");
    return false;
  }
  try {
    const app = initializeApp(FIREBASE_CONFIG);
    fbDb = getFirestore(app);
    fbEnabled = true;
    console.log("[Firebase] Firestore connecté !");
    return true;
  } catch (err) {
    console.warn("[Firebase] Échec init :", err);
    return false;
  }
}

// ── Synchroniser la progression ──────────────────────────────────────────────
async function syncProgress(prog) {
  if (!fbEnabled || !fbDb || !prog.name) return;
  try {
    await setDoc(doc(fbDb, "players", playerId(prog.name)), {
      name: prog.name,
      xp: prog.xp || 0,
      chapters_done: prog.chapters_done || [],
      badges: prog.badges || [],
      starter_pokemon: prog.starter_pokemon || "",
      lang: prog.lang || "",
      updated_at: new Date()
    });
  } catch (err) {
    console.warn("[Firebase] Sync échoué :", err);
  }
}

// ── Charger un joueur existant ────────────────────────────────────────────────
async function loadPlayer(name) {
  if (!fbEnabled || !fbDb) return null;
  try {
    const snap = await getDoc(doc(fbDb, "players", playerId(name)));
    return snap.exists() ? snap.data() : null;
  } catch (err) {
    console.warn("[Firebase] Chargement joueur échoué :", err);
    return null;
  }
}

// ── Liste tous les joueurs (triés par XP décroissant) ────────────────────────
async function listAllPlayers() {
  if (!fbEnabled || !fbDb) return [];
  try {
    const q = query(collection(fbDb, "players"), orderBy("xp", "desc"));
    const snap = await getDocs(q);
    return snap.docs.map(d => d.data());
  } catch (err) {
    console.warn("[Firebase] Liste joueurs échoué :", err);
    return [];
  }
}

// ── Exposer sur window (app.js est un script defer classique) ────────────────
window.initFirebase = initFirebase;
window.syncProgress = syncProgress;
window.loadPlayer = loadPlayer;
window.listAllPlayers = listAllPlayers;
