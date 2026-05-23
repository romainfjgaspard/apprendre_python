#!/usr/bin/env python3
"""Migration one-shot : web/chapters.json → chapters/ch{N}/ structure de fichiers.

Source de vérité : chapters.json (plus à jour que les notebooks .ipynb).
Crée un répertoire par chapitre avec :
  meta.json             — métadonnées (titre, XP, badge, saison, boss)
  {N:02d}_lesson.en.md  — cellule texte (markdown, contenu anglais existant)
  {N:02d}_example.py    — cellule code sans ???
  {N:02d}_exercise.py   — cellule exercice (contient ???)

Les cellules verify sont auto-générées par export_web.py — non stockées.
Les fichiers .fr.md seront ajoutés manuellement après.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
SRC_JSON = HERE / "web" / "chapters.json"
OUT_DIR = HERE / "chapters"


def migrate_chapter(num: int, ch: dict, ch_dir: Path) -> int:
    ch_dir.mkdir(parents=True, exist_ok=True)

    meta = {
        "num": ch["num"],
        "title": ch["title"],
        "desc": ch["desc"],
        "badge": ch["badge"],
        "xp": ch["xp"],
        "season": ch["season"],
        "boss": ch.get("boss", False),
    }
    (ch_dir / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    file_idx = 1
    for cell in ch["cells"]:
        ctype = cell["type"]
        source = cell.get("source", "")

        if ctype == "md":
            path = ch_dir / f"{file_idx:02d}_lesson.en.md"
            path.write_text(source, encoding="utf-8")
            file_idx += 1
        elif ctype == "code":
            path = ch_dir / f"{file_idx:02d}_example.py"
            path.write_text(source, encoding="utf-8")
            file_idx += 1
        elif ctype == "exercise":
            path = ch_dir / f"{file_idx:02d}_exercise.py"
            path.write_text(source, encoding="utf-8")
            file_idx += 1
        # verify : skipped, auto-générées par export_web.py

    return file_idx - 1


def main():
    if not SRC_JSON.exists():
        print(f"❌ {SRC_JSON} introuvable.")
        return

    data = json.loads(SRC_JSON.read_text(encoding="utf-8"))
    chapters = data["chapters"]

    total_files = 0
    for num_str, ch in sorted(chapters.items(), key=lambda x: int(x[0])):
        num = int(num_str)
        ch_dir = OUT_DIR / f"ch{num:02d}"
        n = migrate_chapter(num, ch, ch_dir)
        total_files += n
        boss_tag = " [BOSS]" if ch.get("boss") else ""
        print(f"  ✅ ch{num:02d}{boss_tag}: {n} fichiers — {ch['title']}")

    print(f"\n✨ {len(chapters)} chapitres migrés ({total_files} fichiers) → {OUT_DIR}/")


if __name__ == "__main__":
    main()
