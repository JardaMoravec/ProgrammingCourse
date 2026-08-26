#!/usr/bin/env python3
"""Generuje ukoly.md a VPL testy z lekce/**/ukoly/*/ukol.yaml."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LEKCE = ROOT / "lekce" / "1-rocnik"

TASK_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9-]+)$")


def stars(n: int) -> str:
    return "★" * int(n) + "☆" * (3 - int(n))


def format_vpl_cases(cases: list[dict]) -> str:
    lines: list[str] = []
    for c in cases:
        lines.append(f"Case = {c['name']}")
        if c.get("input") is not None:
            lines.append(f"Input = {str(c['input']).rstrip()}")
        out = c.get("output")
        if out is not None:
            if c.get("numeric"):
                lines.append(f"Output = {out}")
            else:
                lines.append(f'Output = "{out}"')
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def task_dir_name(task: dict) -> str:
    return f"{task['id']}-{task['slug']}"


def parse_meta(meta_path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not meta_path.exists():
        return data
    for line in meta_path.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.strip().startswith("#"):
            key, _, val = line.partition(":")
            data[key.strip()] = val.strip()
    return data


def load_task(task_dir: Path) -> dict | None:
    match = TASK_DIR_RE.match(task_dir.name)
    yaml_path = task_dir / "ukol.yaml"
    if not match or not yaml_path.exists():
        return None
    raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{yaml_path}: ocekavan slovnik")
    task = {
        "id": match.group(1),
        "slug": match.group(2),
        "title": raw["title"],
        "stars": raw["stars"],
        "description": raw["description"],
        "cases": raw["cases"],
    }
    if raw.get("io"):
        task["io"] = raw["io"]
    if raw.get("moodle"):
        task["moodle"] = raw["moodle"]
    if raw.get("files"):
        task["files"] = raw["files"]
    return task


def discover_tasks(lesson_dir: Path) -> list[dict]:
    ukoly_root = lesson_dir / "ukoly"
    if not ukoly_root.is_dir():
        return []
    tasks: list[dict] = []
    for task_dir in sorted(ukoly_root.iterdir()):
        if not task_dir.is_dir():
            continue
        task = load_task(task_dir)
        if task:
            tasks.append(task)
    return tasks


def cleanup_stale_ukoly(ukoly_root: Path, tasks: list[dict]) -> None:
    expected_dirs = {task_dir_name(t) for t in tasks}
    for child in ukoly_root.iterdir():
        if not child.is_dir():
            continue
        if child.name == "reseni":
            shutil.rmtree(child, ignore_errors=True)
            continue
        if child.name not in expected_dirs:
            shutil.rmtree(child)


def strip_format_from_description(description: str) -> str:
    """Odstraní řádky „Formát:“ z popisu — formát patří do pole io."""
    lines = str(description).strip().splitlines()
    kept = [line for line in lines if not re.match(r"^\s*Formát\s*:", line, re.I)]
    return "\n".join(kept).strip()


def build_ukoly_md(lesson_id: str, lesson_name: str, tasks: list[dict]) -> str:
    num = lesson_id[:2]
    parts = [
        f"# Úkoly — {lesson_name}",
        "",
        "> **Samostatná práce** k odevzdání v Moodle (Virtual Programming Lab).",
        "> U cvičení v hodině máte k dispozici řešení — u těchto úkolů ne.",
        "> V Moodle spusťte **Evaluate** — automatický test ověří výstup programu.",
        "",
        "**Odevzdání:** soubor `main.py` (nebo název uvedený v Moodle).",
        "",
    ]
    for t in tasks:
        moodle = t.get("moodle", f"PRG-1-{num}-{t['id']}")
        description = strip_format_from_description(t["description"])
        parts += [
            "---",
            "",
            f"## Úkol {t['id']} — {t['title']} ({stars(t['stars'])})",
            "",
            f"**Moodle:** `{moodle}`",
            "",
            description,
            "",
        ]
        if t.get("io"):
            parts += ["**Formát:**", "", str(t["io"]).strip(), ""]
    return "\n".join(parts)


def write_lesson_ukoly(lesson_dir: Path, tasks: list[dict]) -> None:
    meta = parse_meta(lesson_dir / "meta.yaml")
    nazev = meta.get("nazev", lesson_dir.name)
    (lesson_dir / "ukoly.md").write_text(
        build_ukoly_md(lesson_dir.name, nazev, tasks), encoding="utf-8"
    )

    ukoly_root = lesson_dir / "ukoly"
    ukoly_root.mkdir(parents=True, exist_ok=True)
    cleanup_stale_ukoly(ukoly_root, tasks)

    for t in tasks:
        task_dir = ukoly_root / task_dir_name(t)
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / "vpl_evaluate.cases").write_text(
            format_vpl_cases(t["cases"]), encoding="utf-8"
        )
        for fname, content in t.get("files", {}).items():
            (task_dir / fname).write_text(content, encoding="utf-8")


def lesson_dirs() -> list[Path]:
    dirs = [d for d in LEKCE.iterdir() if d.is_dir() and re.match(r"\d{2}-", d.name)]
    return sorted(dirs, key=lambda p: p.name)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print("Generuji ukoly.md + VPL testy z lekce/**/ukoly/*/ukol.yaml ...")
    total = 0
    for lesson_dir in lesson_dirs():
        tasks = discover_tasks(lesson_dir)
        if not tasks:
            continue
        write_lesson_ukoly(lesson_dir, tasks)
        total += len(tasks)
        print(f"  OK {lesson_dir.name} ({len(tasks)} ukolu)")
    print(f"Hotovo ({total} ukolu).")


if __name__ == "__main__":
    main()
