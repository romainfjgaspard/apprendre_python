#!/usr/bin/env python3
"""Génère chapters.json depuis chapters/ch*/ (structure markdown + .py).

Structure attendue par chapitre :
  chapters/ch{N:02d}/
    meta.json              — { num, title, desc, badge, xp, season, boss }
    {N}_lesson.en.md       — cellule texte anglaise
    {N}_lesson.fr.md       — cellule texte française (optionnelle)
    {N}_example.py         — cellule code (pas de ???)
    {N}_exercise.py        — cellule exercice (contient ???)

Les cellules md génèrent source_en + source_fr dans le JSON.
source (compat) = source_en pour ne pas casser app.js avant la Tâche 6.
Les cellules code/exercise génèrent source unique.
Une cellule verify est auto-ajoutée en fin de chapitre.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
CHAPTERS_DIR = HERE / "chapters"

SEASONS = {
    "1": {"name": "Pokémon Edition",   "emoji": "⚡",  "color": "#f6d365"},
    "2": {"name": "Formula 1",         "emoji": "🏎️", "color": "#e74c3c"},
    "3": {"name": "Birds Simulation",  "emoji": "🐦",  "color": "#a855f7"},
}

LEVELS = [
    [0,    "🥚 Egg"],
    [50,   "⚡ Pichu"],
    [150,  "⚡ Pikachu"],
    [300,  "⚡ Raichu"],
    [500,  "🔥 Charizard"],
    [750,  "🐉 Dragonite"],
    [1000, "🌟 Mewtwo"],
    [1500, "🏆 Pokémon Master"],
]


def read_chapter(ch_dir: Path) -> dict:
    meta = json.loads((ch_dir / "meta.json").read_text(encoding="utf-8"))
    num = meta["num"]
    cells = []

    files = sorted(f for f in ch_dir.iterdir() if f.name != "meta.json")
    processed_en_stems: set[str] = set()

    for f in files:
        name = f.name

        if name.endswith(".en.md"):
            stem = name[: -len(".en.md")]
            source_en = f.read_text(encoding="utf-8")
            fr_file = ch_dir / f"{stem}.fr.md"
            source_fr = fr_file.read_text(encoding="utf-8") if fr_file.exists() else ""
            cell: dict = {"type": "md", "source_en": source_en, "source": source_en}
            if source_fr:
                cell["source_fr"] = source_fr
            cells.append(cell)
            processed_en_stems.add(stem)

        elif name.endswith(".fr.md"):
            stem = name[: -len(".fr.md")]
            if stem in processed_en_stems:
                continue  # déjà traité avec .en.md
            # .fr.md sans .en.md correspondant (cas rare)
            source_fr = f.read_text(encoding="utf-8")
            cells.append({"type": "md", "source_fr": source_fr, "source": source_fr})

        elif f.suffix == ".py":
            source = f.read_text(encoding="utf-8")
            if "???" in source:
                cells.append({"type": "exercise", "source": source})
            else:
                cells.append({"type": "code", "source": source})

    # Cellule verify auto-générée en fin de chapitre
    cells.append({
        "type": "verify",
        "source": f"from _verify import verify\nverify({num}, locals())",
    })

    return {
        "num": num,
        "title": meta["title"],
        "desc": meta["desc"],
        "badge": meta["badge"],
        "xp": meta["xp"],
        "season": meta["season"],
        "boss": meta.get("boss", False),
        "cells": cells,
    }


def main():
    if not CHAPTERS_DIR.exists():
        print("❌ chapters/ introuvable. Lancez d'abord migrate_to_chapters.py.")
        return

    ch_dirs = sorted(
        d for d in CHAPTERS_DIR.iterdir()
        if d.is_dir() and re.match(r"^ch\d+[a-z]?$", d.name)
    )

    if not ch_dirs:
        print("❌ Aucun répertoire ch{N}/ trouvé dans chapters/.")
        return

    out: dict = {"chapters": {}, "seasons": SEASONS, "levels": LEVELS}

    for ch_dir in ch_dirs:
        try:
            ch = read_chapter(ch_dir)
            out["chapters"][str(ch["num"])] = ch
            boss_tag = " [BOSS]" if ch["boss"] else ""
            print(f"  ✅ Ch {str(ch['num']):>4}{boss_tag}: {len(ch['cells'])} cellules — {ch['title']}")
        except Exception as exc:
            print(f"  ❌ {ch_dir.name}: {exc}")

    out_path = HERE / "chapters.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print(f"\n✨ {len(out['chapters'])} chapitres exportés → {out_path}")


if __name__ == "__main__":
    main()
