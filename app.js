/* ═══════════════════════════════════════════════════════════════════════════
   Python Quest — Web App Engine v2
   ═══════════════════════════════════════════════════════════════════════════ */

// ── i18n ─────────────────────────────────────────────────────────────────────
const I18N = {
  en: {
    splash_subtitle: "Learn Python by building games!",
    splash_label: "New Trainer — enter your name",
    splash_existing_label: "Existing Trainer:",
    splash_or: "— or —",
    splash_start: "Start Adventure! ⚡",
    map_title: "🗺️ Adventure Map",
    season1_title: "⚡ Season 1 — Pokémon Edition",
    season2_title: "🏎️ Season 2 — Formula 1",
    season3_title: "🐦 Season 3 — Birds Simulation",
    chapter_back: "← Map",
    victory_back: "Back to Map 🗺️",
    victory_perfect: "🎉 PERFECT!",
    victory_already: "Already completed",
    verify_btn: "✅ Verify my answers!",
    verify_checking: "Checking...",
    loading_pyodide: "Loading Python engine... (first time may take a few seconds)",
    example_label: "📝 Example",
    exercise_label: "✏️ Your code",
    run_btn: "▶ Run",
    no_output: "(no output)",
  },
  fr: {
    splash_subtitle: "Apprends Python en créant des jeux !",
    splash_label: "Nouveau dresseur — entre ton nom",
    splash_existing_label: "Dresseur existant :",
    splash_or: "— ou —",
    splash_start: "Lancer l'aventure ! ⚡",
    map_title: "🗺️ Carte d'aventure",
    season1_title: "⚡ Saison 1 — Édition Pokémon",
    season2_title: "🏎️ Saison 2 — Formule 1",
    season3_title: "🐦 Saison 3 — Simulation d'oiseaux",
    chapter_back: "← Carte",
    victory_back: "Retour à la carte 🗺️",
    victory_perfect: "🎉 PARFAIT !",
    victory_already: "Déjà terminé",
    verify_btn: "✅ Vérifier mes réponses !",
    verify_checking: "Vérification...",
    loading_pyodide: "Chargement du moteur Python... (peut prendre quelques secondes la première fois)",
    example_label: "📝 Exemple",
    exercise_label: "✏️ Ton code",
    run_btn: "▶ Run",
    no_output: "(pas de sortie)",
    // Chapter titles & descriptions (map)
    ch1_title: "⚡ Salut Pokémon", ch1_desc: "print, variables, f-strings",
    ch2_title: "🔢 Types & Calculs", ch2_desc: "int, float, opérateurs",
    ch3_title: "🔀 Conditions", ch3_desc: "if/elif/else, types Pokémon",
    ch4_title: "🔁 La Boucle for", ch4_desc: "for, liste, range()",
    "ch4.5_title": "🔄 La Boucle while", "ch4.5_desc": "while, break",
    ch5_title: "📋 Listes", ch5_desc: "créer, indexer, trier",
    ch6_title: "📖 Dictionnaires", ch6_desc: "dicts, Pokédex",
    ch7_title: "🧩 Fonctions", ch7_desc: "def, return, paramètres",
    ch8_title: "💾 Fichiers & JSON", ch8_desc: "lire/écrire, sauvegarder",
    ch9_title: "🏆 BOSS — Arène Pokémon", ch9_desc: "tout combiner !",
    ch10_title: "🏎️ Listes de listes", ch10_desc: "listes imbriquées, grille F1",
    ch11_title: "🏆 Trier & Filtrer", ch11_desc: "sorted, lambda",
    ch12_title: "🎲 Modules & Random", ch12_desc: "import, random, simulateur",
    ch13_title: "📊 Premier graphique", ch13_desc: "matplotlib barres & lignes",
    ch14_title: "📑 Lire un CSV", ch14_desc: "module csv, résultats F1",
    ch15_title: "🐼 Pandas DataFrames", ch15_desc: "DataFrame, groupby",
    ch16_title: "🎨 Graphiques avancés", ch16_desc: "subplots, tableaux de bord",
    ch17_title: "🏆 BOSS — Championnat F1", ch17_desc: "saison complète + dashboard",
    ch18_title: "🧬 Classes (POO)", ch18_desc: "class, __init__, méthodes",
    ch19_title: "🟢 Objets en mouvement", ch19_desc: "position, vitesse, rebond",
    ch20_title: "🔢 Bases de numpy", ch20_desc: "tableaux, maths vectorielles",
    ch21_title: "🎬 Animation", ch21_desc: "FuncAnimation, scatter",
    ch22_title: "🐦 Classe Boid", ch22_desc: "classe Boid, flèches",
    ch23_title: "🐦 3 Règles de vol", ch23_desc: "séparation, alignement, cohésion",
    ch24_title: "🦅 Héritage : Prédateur", ch24_desc: "super(), override, chasse",
    ch25_title: "🎮 Simulation interactive", ch25_desc: "curseurs, événements souris",
    ch26_title: "🏆 BOSS — Oiseaux Ultime", ch26_desc: "50 oiseaux + prédateur + curseurs",
  }
};

let LANG = localStorage.getItem("python_quest_lang") || "en";

function t(key) { return (I18N[LANG] || I18N.en)[key] || (I18N.en)[key] || key; }

function applyI18n() {
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    el.textContent = t(key);
  });
  // Update all lang buttons (splash + map header)
  document.querySelectorAll(".lang-toggle button").forEach(btn => {
    const lang = btn.id.replace("lang-", "").replace("2", "");
    btn.classList.toggle("active", lang === LANG);
  });
}

function setLang(lang) {
  LANG = lang;
  localStorage.setItem("python_quest_lang", lang);
  applyI18n();
  // Re-render map if visible
  if (DATA && !document.getElementById("home-screen").classList.contains("hidden")) {
    renderMap();
  }
  // Re-render current chapter if visible
  if (DATA && CURRENT_CHAPTER !== null && !document.getElementById("chapter-screen").classList.contains("hidden")) {
    openChapter(CURRENT_CHAPTER);
  }
}

// ── State ────────────────────────────────────────────────────────────────────
let DATA = null;          // chapters.json
let pyodide = null;       // Pyodide instance
let pyodideLoading = false;
const editors = [];       // CodeMirror instances for current chapter
let CURRENT_CHAPTER = null;

const SAVE_KEY = "python_quest_save";

function loadProgress() {
  const raw = localStorage.getItem(SAVE_KEY);
  if (raw) return JSON.parse(raw);
  return { name: "", xp: 0, chapters_done: [], badges: [] };
}

function saveProgress(prog) {
  localStorage.setItem(SAVE_KEY, JSON.stringify(prog));
  // Sync to Firebase if available
  if (typeof syncProgress === "function") syncProgress(prog);
}

let PROG = loadProgress();

// ── Levels ───────────────────────────────────────────────────────────────────
const LEVELS = [
  [0,    "🥚 Egg"],
  [50,   "⚡ Pichu"],
  [150,  "⚡ Pikachu"],
  [300,  "⚡ Raichu"],
  [500,  "🔥 Charizard"],
  [750,  "🐉 Dragonite"],
  [1000, "🌟 Mewtwo"],
  [1500, "🏆 Pokémon Master"],
];

function getLevel(xp) {
  for (let i = LEVELS.length - 1; i >= 0; i--) {
    if (xp >= LEVELS[i][0]) return LEVELS[i][1];
  }
  return LEVELS[0][1];
}

function getXpProgress(xp) {
  let current = 0, next = LEVELS[LEVELS.length - 1][0];
  for (let i = 0; i < LEVELS.length; i++) {
    if (xp >= LEVELS[i][0]) {
      current = LEVELS[i][0];
      next = i + 1 < LEVELS.length ? LEVELS[i + 1][0] : current;
    }
  }
  if (next === current) return { ratio: 1, text: `${xp} XP — MAX!` };
  const ratio = (xp - current) / (next - current);
  return { ratio, text: `${xp} XP` };
}

// ── DOM helpers ──────────────────────────────────────────────────────────────
const $ = (sel) => document.querySelector(sel);
const show = (el) => el.classList.remove("hidden");
const hide = (el) => el.classList.add("hidden");

function showScreen(id) {
  document.querySelectorAll(".screen").forEach(s => hide(s));
  show($(`#${id}-screen`));
}

// ── HUD ──────────────────────────────────────────────────────────────────────
function updateHUD() {
  $("#hud-name").textContent = PROG.name;
  $("#hud-level").textContent = getLevel(PROG.xp);
  const p = getXpProgress(PROG.xp);
  $("#hud-xp-fill").style.width = (p.ratio * 100) + "%";
  $("#hud-xp-text").textContent = p.text;
  $("#hud-badges").textContent = PROG.badges.join(" ");
}

// ── Map rendering ────────────────────────────────────────────────────────────
function renderMap() {
  updateHUD();
  // Sorted nums across ALL chapters for unlock chain (handles decimals like 4.5)
  const allSortedNums = Object.values(DATA.chapters).map(c => c.num).sort((a, b) => a - b);

  for (const s of [1, 2, 3]) {
    const grid = $(`#grid-s${s}`);
    grid.innerHTML = "";
    const chs = Object.values(DATA.chapters).filter(c => c.season === s);
    chs.sort((a, b) => a.num - b.num);

    for (const ch of chs) {
      const done = PROG.chapters_done.includes(ch.num);
      const idx = allSortedNums.indexOf(ch.num);
      const prevNum = idx > 0 ? allSortedNums[idx - 1] : null;
      const prev = prevNum === null || PROG.chapters_done.includes(prevNum);
      const locked = !prev && !done;
      const isCurrent = !done && prev; // next to play

      // Use translated titles if available
      const title = t(`ch${ch.num}_title`) !== `ch${ch.num}_title` ? t(`ch${ch.num}_title`) : ch.title;
      const desc = t(`ch${ch.num}_desc`) !== `ch${ch.num}_desc` ? t(`ch${ch.num}_desc`) : ch.desc;

      const node = document.createElement("div");
      node.className = "chapter-node" +
        (done ? " done" : "") +
        (locked ? " locked" : "") +
        (isCurrent ? " current" : "") +
        (ch.boss ? ` boss s${s}` : "");

      node.innerHTML = `
        <span class="node-num">${ch.num}</span>
        <div class="node-info">
          <div class="node-title">${escapeHtml(title)}</div>
          <div class="node-desc">${escapeHtml(desc)}</div>
        </div>
        <span class="node-status">${done ? "✅" : locked ? "🔒" : "⬜"}</span>
      `;

      if (!locked) {
        node.addEventListener("click", () => openChapter(ch.num));
      }
      grid.appendChild(node);
    }
  }
}

function escapeHtml(s) {
  const d = document.createElement("div");
  d.textContent = s;
  return d.innerHTML;
}

// ── Chapter rendering ────────────────────────────────────────────────────────
function openChapter(num) {
  const ch = DATA.chapters[String(num)];
  if (!ch) return;

  CURRENT_CHAPTER = num;
  editors.length = 0;
  showScreen("chapter");

  // Use translated title if available
  const chTitle = t(`ch${num}_title`) !== `ch${num}_title` ? t(`ch${num}_title`) : ch.title;
  $("#chapter-title").textContent = chTitle;
  $("#chapter-xp-badge").textContent = `${ch.badge} +${ch.xp} XP`;

  const content = $("#chapter-content");
  content.innerHTML = "";
  content.scrollTop = 0;

  let exerciseIndex = 0;

  for (const cell of ch.cells) {
    if (cell.type === "md") {
      const div = document.createElement("div");
      div.className = "cell-md";
      div.innerHTML = marked.parse(cell[LANG === "fr" ? "source_fr" : "source_en"] || cell.source);
      content.appendChild(div);
    }
    else if (cell.type === "code" || cell.type === "exercise") {
      const wrapper = document.createElement("div");
      wrapper.className = "cell-code" + (cell.type === "exercise" ? " exercise" : "");

      const header = document.createElement("div");
      header.className = "cell-code-header";
      header.innerHTML = `<span>${cell.type === "exercise" ? t("exercise_label") : t("example_label")}</span>`;

      const runBtn = document.createElement("button");
      runBtn.className = "btn btn-small btn-run";
      runBtn.textContent = t("run_btn");
      header.appendChild(runBtn);
      wrapper.appendChild(header);

      const editorDiv = document.createElement("div");
      wrapper.appendChild(editorDiv);

      const outputDiv = document.createElement("div");
      outputDiv.className = "cell-output";
      wrapper.appendChild(outputDiv);

      content.appendChild(wrapper);

      // Create CodeMirror editor — restaure le contenu saisi précédemment si dispo
      const cellKey = `pq_cell_${num}_${editors.length}`;
      const cm = CodeMirror(editorDiv, {
        value: localStorage.getItem(cellKey) || cell.source,
        mode: "python",
        theme: "dracula",
        lineNumbers: true,
        indentUnit: 4,
        readOnly: false,
        viewportMargin: Infinity,
      });
      editors.push({ cm, outputDiv, type: cell.type });

      const editorIdx = editors.length - 1;
      cm.on("change", () => localStorage.setItem(cellKey, cm.getValue()));
      runBtn.addEventListener("click", () => runCell(editorIdx));
    }
    else if (cell.type === "verify") {
      const div = document.createElement("div");
      div.className = "verify-section";
      const btn = document.createElement("button");
      btn.className = "btn btn-verify";
      btn.textContent = t("verify_btn");
      btn.addEventListener("click", () => runVerify(num));
      div.appendChild(btn);

      const out = document.createElement("div");
      out.className = "cell-output";
      out.id = "verify-output";
      div.appendChild(out);

      content.appendChild(div);
    }
  }

  // Scroll to top
  window.scrollTo(0, 0);
}

// ── Pyodide ──────────────────────────────────────────────────────────────────
async function ensurePyodide() {
  if (pyodide) return pyodide;
  if (pyodideLoading) {
    // Wait for existing load
    while (!pyodide) await new Promise(r => setTimeout(r, 200));
    return pyodide;
  }

  pyodideLoading = true;
  show($("#loading-overlay"));
  $("#loading-text").textContent = t("loading_pyodide");

  // Dynamically load Pyodide
  const script = document.createElement("script");
  script.src = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js";
  document.head.appendChild(script);

  await new Promise((resolve, reject) => {
    script.onload = resolve;
    script.onerror = reject;
  });

  pyodide = await loadPyodide();

  // Pre-load the verify module
  await pyodide.runPythonAsync(VERIFY_PY_SOURCE);

  hide($("#loading-overlay"));
  pyodideLoading = false;
  return pyodide;
}

// ── Run code ─────────────────────────────────────────────────────────────────
async function runCell(idx) {
  const { cm, outputDiv } = editors[idx];
  const code = cm.getValue();
  outputDiv.textContent = "";
  outputDiv.className = "cell-output";

  try {
    const py = await ensurePyodide();

    // Capture stdout
    py.runPython(`
import sys, io
_capture = io.StringIO()
sys.stdout = _capture
sys.stderr = _capture
`);

    await py.runPythonAsync(code);

    const output = py.runPython("_capture.getvalue()");
    py.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__");

    outputDiv.textContent = output || t("no_output");
    outputDiv.className = "cell-output output-ok";
  } catch (err) {
    outputDiv.textContent = String(err).split("\n").slice(-3).join("\n");
    outputDiv.className = "cell-output output-error";
    // Restore stdout
    try { pyodide.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__"); } catch {}
  }
}

// ── Run verify ───────────────────────────────────────────────────────────────
async function runVerify(chapterNum) {
  const outDiv = document.getElementById("verify-output");
  outDiv.textContent = t("verify_checking");
  outDiv.className = "cell-output";

  try {
    const py = await ensurePyodide();

    // First, run all exercise cells to set variables
    for (const { cm, type } of editors) {
      if (type === "exercise") {
        await py.runPythonAsync(cm.getValue());
      }
    }

    // Run verification
    py.runPython(`
import sys, io
_capture = io.StringIO()
sys.stdout = _capture
sys.stderr = _capture
`);

    await py.runPythonAsync(`_verify_chapter(${chapterNum}, dict(globals()))`);

    const output = py.runPython("_capture.getvalue()");
    py.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__");

    outDiv.textContent = output;

    // Read results
    const ok = py.runPython("_last_ok");
    const total = py.runPython("_last_total");
    const passed = ok === total;

    if (passed) {
      outDiv.className = "cell-output output-ok";
      showVictory(chapterNum, ok, total);
    } else {
      outDiv.className = "cell-output";
    }
  } catch (err) {
    outDiv.textContent = String(err).split("\n").slice(-4).join("\n");
    outDiv.className = "cell-output output-error";
    try { pyodide.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__"); } catch {}
  }
}

// ── Victory ──────────────────────────────────────────────────────────────────
function spawnParticles() {
  const container = $("#victory-particles");
  if (!container) return;
  container.innerHTML = "";
  const emojis = ["✨", "⭐", "💫", "🌟", "⚡", "🎉"];
  for (let i = 0; i < 14; i++) {
    const p = document.createElement("span");
    p.className = "xp-particle";
    p.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    const dur = (0.7 + Math.random() * 0.7).toFixed(2) + "s";
    p.style.cssText = `left:${8 + Math.random() * 84}%;bottom:${15 + Math.random() * 30}%;` +
                      `animation-delay:${(Math.random() * 0.4).toFixed(2)}s;--dur:${dur}`;
    container.appendChild(p);
    setTimeout(() => p.remove(), 1800);
  }
}

function showVictory(chapterNum, ok, total) {
  const ch = DATA.chapters[String(chapterNum)];
  if (!ch) return;

  const oldLevel = getLevel(PROG.xp);
  let isNew = false;
  if (!PROG.chapters_done.includes(chapterNum)) {
    PROG.chapters_done.push(chapterNum);
    PROG.xp += ch.xp;
    PROG.badges.push(ch.badge);
    saveProgress(PROG);
    isNew = true;
  }
  const newLevel = getLevel(PROG.xp);
  const evolved = isNew && oldLevel !== newLevel;

  $("#victory-title").textContent = t("victory_perfect");
  $("#victory-score").textContent = `Score: ${ok}/${total}`;
  $("#victory-xp").textContent = isNew ? `+${ch.xp} XP ✨` : t("victory_already");
  $("#victory-badge").textContent = isNew ? ch.badge : "";

  // Pokémon emoji (Season 1 only)
  const pokemonEl = $("#victory-pokemon");
  if (pokemonEl) {
    const levelEmoji = newLevel.split(" ").slice(0, 1).join("") || "⭐";
    pokemonEl.textContent = levelEmoji;
    pokemonEl.style.display = ch.season === 1 ? "inline-block" : "none";
  }

  // Level-up evolution panel
  const levelupEl = $("#victory-levelup");
  if (levelupEl) {
    if (evolved) {
      show(levelupEl);
      $("#victory-new-level").textContent = newLevel;
    } else {
      hide(levelupEl);
    }
  }

  // Glow + particles on new completion (Season 1)
  if (isNew) {
    const box = $(".modal-box");
    if (box) {
      box.classList.remove("victory-new");
      void box.offsetWidth;
      box.classList.add("victory-new");
    }
    if (ch.season === 1) spawnParticles();
  }

  show($("#victory-modal"));
}

// ── Navigation ───────────────────────────────────────────────────────────────
$("#back-btn").addEventListener("click", () => {
  // Reset Pyodide namespace for fresh chapter
  if (pyodide) {
    try { pyodide.runPython("pass"); } catch {}
  }
  showScreen("home");
  renderMap();
});

$("#victory-btn").addEventListener("click", () => {
  hide($("#victory-modal"));
  const box = $(".modal-box");
  if (box) box.classList.remove("victory-new");
  showScreen("home");
  renderMap();
});

// ── Splash / name entry ──────────────────────────────────────────────────────
async function startGame() {
  const sel = $("#existing-player");
  const selectedName = sel && sel.value ? sel.value : "";

  if (selectedName) {
    // Dresseur existant — charger depuis Firestore
    const data = typeof loadPlayer === "function" ? await loadPlayer(selectedName) : null;
    if (data) {
      PROG = {
        name: data.name,
        xp: data.xp || 0,
        chapters_done: data.chapters_done || [],
        badges: data.badges || [],
        starter_pokemon: data.starter_pokemon || "",
        lang: data.lang || LANG
      };
      if (data.lang) setLang(data.lang);
    } else {
      PROG.name = selectedName;
    }
  } else {
    // Nouveau dresseur
    const nameInput = $("#player-name");
    const name = nameInput.value.trim();
    if (!name) { nameInput.focus(); return; }
    PROG.name = name;
    PROG.lang = LANG;
  }

  saveProgress(PROG);
  showScreen("home");
  renderMap();
}

$("#start-btn").addEventListener("click", startGame);
$("#player-name").addEventListener("keydown", (e) => {
  if (e.key === "Enter") startGame();
});

// Effacer la sélection dropdown si l'utilisateur tape un nouveau nom
$("#player-name").addEventListener("input", () => {
  const sel = $("#existing-player");
  if (sel) sel.value = "";
});

// Effacer le champ texte si un dresseur existant est sélectionné
$("#existing-player")?.addEventListener("change", () => {
  const sel = $("#existing-player");
  if (sel && sel.value) $("#player-name").value = "";
});

// ── Verify module (embedded as string, loaded into Pyodide) ──────────────────
const VERIFY_PY_SOURCE = `
import os as _os

_last_ok = 0
_last_total = 0

def _vc(label, condition, hint, results):
    if condition:
        results.append(True)
        print(f"  ✅ {label}")
    else:
        results.append(False)
        print(f"  ❌ {label} — 💡 {hint}")

def _ch1(ns, r):
    _vc("trainer_name is text", type(ns.get('trainer_name')) is str and len(ns.get('trainer_name',''))>0, 'Use quotes: trainer_name = "Ash"', r)
    _vc("pokemon_name is text", type(ns.get('pokemon_name')) is str and len(ns.get('pokemon_name',''))>0, 'Use quotes: pokemon_name = "Pikachu"', r)
    _vc("pokemon_hp is a number", type(ns.get('pokemon_hp')) is int and 1 <= ns.get('pokemon_hp',0) <= 999, 'No quotes, a whole number: pokemon_hp = 35', r)
    _vc("pokemon_level is 1-100", type(ns.get('pokemon_level')) is int and 1 <= ns.get('pokemon_level',0) <= 100, 'pokemon_level = 5', r)
    pn = ns.get('pokemon_name',''); ph = ns.get('pokemon_hp',''); pi = ns.get('pokemon_info','')
    _vc("pokemon_info contains name & hp", type(pi) is str and str(pn) in pi and str(ph) in pi, 'f-string with name and hp', r)
    if sum(r)==5:
        tn=ns.get('trainer_name','?'); pn2=ns.get('pokemon_name','?')
        print(f"  🎉 PERFECT! Welcome {tn}, your {pn2} is ready!")

def _ch2(ns, r):
    _vc("hp_after_damage = 65", ns.get('hp_after_damage')==65, 'pokemon_hp - damage_taken → 100 - 35', r)
    _vc("total_heal = 60", ns.get('total_heal')==60, 'potions * potion_heal → 3 * 20', r)
    _vc("hp_after_healing = 125", ns.get('hp_after_healing')==125, 'hp_after_damage + total_heal', r)
    _vc("hits_survived = 4", ns.get('hits_survived')==4, '200 // 45 → 4', r)
    _vc("is_boosted is True", ns.get('is_boosted') is True, 'hp_after_healing > 100 → True', r)

def _ch3(ns, r):
    _vc("is_alive is True", ns.get('is_alive') is True, 'hp > 0 → True', r)
    hp=ns.get('health_pct',0)
    _vc("health_pct = 25.0", hp==25.0 or hp==25, '25/100*100 = 25.0', r)
    _vc("status is Injured", ns.get('status')=='Injured', '25 > 20 → Injured (elif branch)', r)
    _vc("can_evolve is False", ns.get('can_evolve') is False, 'is_alive AND level >= 16 → True AND False → False', r)

def _ch4(ns, r):
    _vc("xp = 50", ns.get('xp')==50, 'range(5) × 10 = 50', r)
    _vc("fire_count = 3", ns.get('fire_count')==3, '3 Fire types in the list', r)
    team = ns.get('team', [])
    _vc("team has 4 Pokémon", len(team)==4, 'for pokemon in team', r)

def _ch4b(ns, r):
    _vc("turns = 4", ns.get('turns')==4, 'while enemy_hp > 0: ... 80/25 → 4 turns', r)
    _vc("heals = 4", ns.get('heals')==4, 'while my_hp < 150: ... 90+4×15=150', r)

def _ch5(ns, r):
    _vc("team has 4", ns.get('team_size')==4, '3+2-1=4', r)
    team=ns.get('team',[])
    _vc("Charizard & Mewtwo in team", "Charizard" in team and "Mewtwo" in team, 'team.append(...)', r)
    _vc("Bulbasaur removed", "Bulbasaur" not in team, 'team.remove("Bulbasaur")', r)
    st=ns.get('sorted_team',[])
    _vc("sorted correctly", st==sorted(team), 'sorted(team)', r)
    fa=ns.get('first_alpha','')
    _vc("first_alpha correct", team and fa==sorted(team)[0], 'Index 0', r)

def _ch6(ns, r):
    _vc("charizard_type is Fire", ns.get('charizard_type')=="Fire", 'pokedex[1]["type"]', r)
    _vc("total_hp = 262", ns.get('total_hp')==262, '35+78+45+44+60=262', r)
    _vc("strong_count = 3", ns.get('strong_count')==3, 'HP > 50', r)
    pdex=ns.get('pokedex',[])
    _vc("Mewtwo added", len(pdex)==6 and any(p.get("name")=="Mewtwo" for p in pdex if isinstance(p,dict)), 'pokedex.append({...})', r)

def _ch7(ns, r):
    cd=ns.get('calc_damage'); ia=ns.get('is_alive'); hl=ns.get('heal')
    _vc("calc_damage(60,40,50)=75.0", callable(cd) and cd(60,40,50)==75.0, '(60/40)*50', r)
    _vc("is_alive(10) is True", callable(ia) and ia(10) is True, '10>0', r)
    _vc("is_alive(0) is False", callable(ia) and ia(0) is False, '0>0→False', r)
    _vc("heal(30,100)=50", callable(hl) and hl(30,100)==50, '30+20=50', r)
    _vc("heal(90,100,30)=100", callable(hl) and hl(90,100,30)==100, 'min(120,100)', r)

def _ch8(ns, r):
    _vc("pokemon_count is 3", ns.get('pokemon_count')==3, 'len(loaded["pokemon"])', r)
    _vc("data_matches is True", ns.get('data_matches') is True, 'json.dumps then json.loads', r)
    jt = ns.get('json_text', '')
    _vc("json_text is a string", isinstance(jt, str) and len(jt) > 10, 'json.dumps(my_pokedex, indent=2)', r)

def _boss1(ns, r):
    _vc("Tournament completed", ns.get('tournament_complete') is True, 'Run all cells', r)
    _vc("battle() works", callable(ns.get('battle')), 'Define battle()', r)
    _vc("All steps done", ns.get('tournament_complete') is True and callable(ns.get('battle')), 'Run everything', r)

def _ch10(ns, r):
    grid=ns.get('grid',[])
    try:
        _vc("grid has 10 rows", len(grid)==10, 'range(10)', r)
        _vc("Pole = Verstappen", grid[0][0]=='Verstappen', 'grid[0][0]', r)
        _vc("Last = Pérez", grid[9][1]=='Pérez', 'grid[9][1]', r)
        _vc("2 cars per row", len(grid[0])==2, '2 per row', r)
    except:
        while len(r)<4: r.append(False)

def _ch11(ns, r):
    ranking=ns.get('ranking',[])
    try:
        _vc("Leader is Ferrari", ranking[0]['team']=='Ferrari', 'Sum per team', r)
        _vc("Leader has 500 pts", ranking[0]['points']==500, '280+220', r)
        _vc("5 teams", len(ranking)==5, '5 unique teams', r)
    except:
        while len(r)<3: r.append(False)

def _ch12(ns, r):
    t=ns.get('totals',{})
    _vc("5 drivers", len(t)==5, 'Loop all drivers', r)
    try: _vc("Valid range", all(80*50<=v<=85*50 for v in t.values()), '50 laps × 80..85', r)
    except: r.append(False)
    _vc("Is dict", isinstance(t,dict), 'Use {}', r)

def _ch13(ns, r):
    lt=ns.get('lap_times',[])
    try:
        _vc("20 laps", len(lt)==20, 'n_laps=20', r)
        _vc(">=79.0s", round(min(lt),1)>=79.0, 'uniform(79,82)', r)
        _vc("<=82.0s", round(max(lt),1)<=82.0, 'uniform(79,82)', r)
    except:
        while len(r)<3: r.append(False)

def _ch14(ns, r):
    _vc("Leader = Verstappen", ns.get('leader')=='Verstappen', '25+25+18=68', r)
    _vc("68 pts", ns.get('leader_pts')==68, 'Sum races', r)
    _vc("5 drivers", len(ns.get('totals',{}))==5, '5 in CSV', r)

def _ch15(ns, r):
    _vc("Ferrari has 2", ns.get('n_ferrari')==2, 'Leclerc+Sainz', r)
    _vc("Wins = 4", ns.get('ferrari_wins')==4, '3+1', r)
    _vc("Pts = 500", ns.get('ferrari_points')==500, '280+220', r)

def _ch16(ns, r):
    _vc("2 subplots", ns.get('n_subplots')==2, 'subplots(1,2,...)', r)
    me=ns.get('max_evo',[0]); le=ns.get('lec_evo',[0])
    _vc("Verstappen leads", me[-1]>le[-1], '243>205', r)

def _boss2(ns, r):
    _vc("10 races", len(ns.get('season',{}))==10, 'Run Step 3', r)
    _vc("Dashboard", ns.get('dashboard_done') is True, 'Run Step 5', r)
    ch=ns.get('champion','?')
    _vc("Complete", ns.get('dashboard_done') is True, 'All steps', r)
    if sum(r)==3: print(f"  🏆 Champion: {ch}!")

def _ch18(ns, r):
    _vc("Team 3+", ns.get('team_size',0)>=3, 'Add 3+', r)
    _vc("First=Pikachu", ns.get('first_name')=='Pikachu', 'team[0]', r)
    team=ns.get('team',[])
    _vc("battle_cry()", team and hasattr(team[0],'battle_cry'), 'def battle_cry(self,...)', r)
    _vc("__str__", team and hasattr(team[0],'__str__'), 'def __str__(self)', r)

def _ch19(ns, r):
    _vc("10 dots", ns.get('n_dots')==10, 'Create 10', r)
    _vc("Bounces > 0", ns.get('total_bounces',0)>0, 'self.bounces += 1', r)
    _vc("All inside", ns.get('total_bounces',0)>0, 'Bounce logic', r)

def _ch20(ns, r):
    _vc("20 dots", ns.get('n_dots')==20, 'N=20', r)
    _vc("All inside", ns.get('all_inside') is True, '% SIZE', r)
    pos=ns.get('pos')
    _vc("Shape (20,2)", hasattr(pos,'shape') and pos.shape==(20,2), '2D array', r)

def _ch21(ns, r):
    _vc("Animation created", ns.get('bounce_anim_created') is True, 'Run animation', r)
    _vc("25 dots", ns.get('n_dots_anim')==25, 'N=25', r)

def _ch22(ns, r):
    _vc("30 boids", ns.get('n_boids')==30, 'range(30)', r)
    _vc("All inside", ns.get('all_inside') is True, 'Bounce', r)

def _ch23(ns, r):
    _vc("Flocking ran", ns.get('flocking_works') is True, 'Run 3-rule cell', r)
    _vc("Separation seen", ns.get('obs_separation','???')!='???', 'Your observation', r)
    _vc("Cohesion seen", ns.get('obs_cohesion','???')!='???', 'Your observation', r)

def _ch24(ns, r):
    _vc("hunt() exists", ns.get('has_hunt') is True, 'def hunt(self,flock)', r)
    _vc("Faster", ns.get('pred_fast') is True, 'max_speed>4', r)
    _vc("Inherits Boid", ns.get('pred') is not None, 'class Predator(Boid)', r)

def _ch25(ns, r):
    _vc("Interactive done", ns.get('interactive_done') is True, 'Run animation', r)
    _vc("Slider exists", ns.get('slider_exists') is True, 'radius_slider', r)

def _boss3(ns, r):
    _vc("Sim running", ns.get('simulation_running') is True, 'Run Step 3', r)
    _vc("50 boids", len(ns.get('flock',[]))==50, 'N=50', r)
    _vc("Predator exists", ns.get('pred') is not None, 'pred=Predator(...)', r)

_CHECKS = {
    1:_ch1, 2:_ch2, 3:_ch3, 4:_ch4, 4.5:_ch4b, 5:_ch5, 6:_ch6, 7:_ch7, 8:_ch8, 9:_boss1,
    10:_ch10, 11:_ch11, 12:_ch12, 13:_ch13, 14:_ch14, 15:_ch15, 16:_ch16, 17:_boss2,
    18:_ch18, 19:_ch19, 20:_ch20, 21:_ch21, 22:_ch22, 23:_ch23, 24:_ch24, 25:_ch25, 26:_boss3,
}

def _verify_chapter(chapter, ns):
    global _last_ok, _last_total
    fn = _CHECKS.get(chapter)
    if not fn:
        print(f"  ⚠️ No checks for chapter {chapter}")
        _last_ok = 0; _last_total = 0
        return
    print(f"  ✅ VERIFICATION — Chapter {chapter}")
    print()
    results = []
    try:
        fn(ns, results)
    except Exception as e:
        print(f"  💥 Error: {e}")
    _last_ok = sum(results)
    _last_total = len(results)
    print(f"\\n  Score: {_last_ok}/{_last_total}")
`;


// ── Boot ─────────────────────────────────────────────────────────────────────
// Language toggle (splash + map header)
document.getElementById("lang-en").addEventListener("click", () => setLang("en"));
document.getElementById("lang-fr").addEventListener("click", () => setLang("fr"));
document.getElementById("lang-en2").addEventListener("click", () => setLang("en"));
document.getElementById("lang-fr2").addEventListener("click", () => setLang("fr"));

async function boot() {
  // Load chapter data
  const res = await fetch("chapters.json");
  DATA = await res.json();

  // Init Firebase
  if (typeof initFirebase === "function") {
    const ok = await initFirebase();
    if (ok) {
      // Peupler le dropdown des dresseurs existants
      const players = await listAllPlayers();
      if (players.length > 0) {
        const sel = $("#existing-player");
        players.forEach(p => {
          const opt = document.createElement("option");
          opt.value = p.name;
          opt.textContent = `${p.name} (${p.xp} XP)`;
          sel.appendChild(opt);
        });
        show($("#existing-section"));
      }
      if (PROG.name) syncProgress(PROG);
    }
  }

  applyI18n();

  if (PROG.name) {
    showScreen("home");
    renderMap();
  } else {
    showScreen("splash");
  }
}

boot();
