/* ═══════════════════════════════════════════════════════════════════════════
   Python Quest — Firebase sync (optional)
   Syncs player progress to Firebase Realtime Database.
   If Firebase is not configured, everything works offline via localStorage.
   ═══════════════════════════════════════════════════════════════════════════ */

// ── Firebase config ──────────────────────────────────────────────────────────
// TODO: Replace with your own Firebase project config
const FIREBASE_CONFIG = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: ""
};

let fbApp = null;
let fbDb = null;
let fbEnabled = false;

// ── Initialize Firebase (called from app.js boot) ────────────────────────────
async function initFirebase() {
  // Skip if no config
  if (!FIREBASE_CONFIG.apiKey) {
    console.log("[Firebase] No config — offline mode");
    return false;
  }

  try {
    // Load Firebase SDK from CDN
    if (typeof firebase === "undefined") {
      await loadScript("https://www.gstatic.com/firebasejs/10.12.0/firebase-app-compat.js");
      await loadScript("https://www.gstatic.com/firebasejs/10.12.0/firebase-database-compat.js");
    }

    fbApp = firebase.initializeApp(FIREBASE_CONFIG);
    fbDb = firebase.database();
    fbEnabled = true;
    console.log("[Firebase] Connected!");
    return true;
  } catch (err) {
    console.warn("[Firebase] Init failed:", err);
    return false;
  }
}

function loadScript(src) {
  return new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = src;
    s.onload = resolve;
    s.onerror = reject;
    document.head.appendChild(s);
  });
}

// ── Sync progress to Firebase ────────────────────────────────────────────────
function syncProgress(prog) {
  if (!fbEnabled || !fbDb || !prog.name) return;

  // Use a sanitized player ID (name lowercase, no special chars)
  const playerId = prog.name.toLowerCase().replace(/[^a-z0-9]/g, "_");

  const data = {
    name: prog.name,
    xp: prog.xp,
    chapters_done: prog.chapters_done.length,
    chapters_list: prog.chapters_done,
    badges: prog.badges,
    level: typeof getLevel === "function" ? getLevel(prog.xp) : "",
    last_updated: new Date().toISOString(),
  };

  fbDb.ref("players/" + playerId).set(data)
    .then(() => console.log("[Firebase] Progress synced"))
    .catch(err => console.warn("[Firebase] Sync failed:", err));
}

// ── Load leaderboard ─────────────────────────────────────────────────────────
async function loadLeaderboard() {
  if (!fbEnabled || !fbDb) return [];

  try {
    const snap = await fbDb.ref("players").orderByChild("xp").once("value");
    const players = [];
    snap.forEach(child => {
      players.push(child.val());
    });
    // Sort descending by XP
    players.sort((a, b) => b.xp - a.xp);
    return players;
  } catch (err) {
    console.warn("[Firebase] Leaderboard load failed:", err);
    return [];
  }
}
