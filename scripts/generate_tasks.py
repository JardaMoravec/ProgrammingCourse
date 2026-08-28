#!/usr/bin/env python3
"""Generuje ukoly.md a VPL testy (cases / Flask hodnotitel) z lekce/**/ukoly/*/ukol.yaml."""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LEKCE_ROOT = ROOT / "lekce"
SABLONY = ROOT / "sablony"

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
        "cases": raw.get("cases") or [],
        "typ": raw.get("typ", "vpl"),
    }
    if raw.get("io"):
        task["io"] = raw["io"]
    if raw.get("moodle"):
        task["moodle"] = raw["moodle"]
    if raw.get("files"):
        task["files"] = raw["files"]
    if raw.get("odevzdani"):
        task["odevzdani"] = raw["odevzdani"]
    if raw.get("soubor"):
        task["soubor"] = raw["soubor"]
    if raw.get("evaluate"):
        task["evaluate"] = raw["evaluate"]
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


def build_ukoly_md(
    lesson_id: str, lesson_name: str, tasks: list[dict], rocnik: str
) -> str:
    num = lesson_id[:2]
    types = {(t.get("typ") or "vpl") for t in tasks}
    has_vpl = "vpl" in types and any(t.get("cases") for t in tasks)
    has_flask = "flask" in types
    parts = [
        f"# Úkoly — {lesson_name}",
        "",
        "> **Samostatná práce** k odevzdání v Moodle.",
        "> U cvičení v hodině máte k dispozici řešení — u těchto úkolů ne.",
        "",
    ]
    if has_vpl:
        parts += [
            "> V Moodle spusťte **Evaluate** — automatický test ověří výstup programu.",
            "",
            "**Odevzdání:** soubor `main.py` (nebo název / způsob uvedený u úkolu).",
            "",
        ]
    elif has_flask:
        parts += [
            "> V Moodle spusťte **Evaluate** — test ověří routy a HTML značky",
            "> (text na stránce může být vlastní).",
            "",
        ]
    for t in tasks:
        moodle = t.get("moodle", f"PRG-{rocnik}-{num}-{t['id']}")
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
        if t.get("odevzdani"):
            parts += ["**Odevzdání:**", "", str(t["odevzdani"]).strip(), ""]
    return "\n".join(parts)


def write_lesson_ukoly(lesson_dir: Path, tasks: list[dict]) -> None:
    meta = parse_meta(lesson_dir / "meta.yaml")
    nazev = meta.get("nazev", lesson_dir.name)
    rocnik = meta.get("rocnik", "1")
    (lesson_dir / "ukoly.md").write_text(
        build_ukoly_md(lesson_dir.name, nazev, tasks, rocnik), encoding="utf-8"
    )

    ukoly_root = lesson_dir / "ukoly"
    ukoly_root.mkdir(parents=True, exist_ok=True)
    cleanup_stale_ukoly(ukoly_root, tasks)

    for t in tasks:
        task_dir = ukoly_root / task_dir_name(t)
        task_dir.mkdir(parents=True, exist_ok=True)
        cases_path = task_dir / "vpl_evaluate.cases"
        if t["cases"]:
            cases_path.write_text(format_vpl_cases(t["cases"]), encoding="utf-8")
        elif cases_path.exists():
            cases_path.unlink()
        write_flask_vpl(task_dir, t)
        for fname, content in t.get("files", {}).items():
            (task_dir / fname).write_text(content, encoding="utf-8")


def format_flask_evaluator(soubor: str, tests: list) -> str:
    template = (SABLONY / "vpl_evaluate_flask.py").read_text(encoding="utf-8")
    if "__STUDENT_FILE__" not in template or "__TESTS__" not in template:
        raise ValueError("sablony/vpl_evaluate_flask.py: chybí placeholdery")
    return template.replace("__STUDENT_FILE__", soubor, 1).replace(
        "__TESTS__",
        json.dumps(tests, ensure_ascii=True, indent=2),
        1,
    )


def write_flask_vpl(task_dir: Path, task: dict) -> None:
    py_path = task_dir / "vpl_evaluate.py"
    sh_path = task_dir / "vpl_evaluate.sh"
    if task.get("typ") != "flask":
        if py_path.exists():
            py_path.unlink()
        if sh_path.exists():
            sh_path.unlink()
        return
    soubor = task.get("soubor")
    tests = task.get("evaluate") or []
    if not soubor or not tests:
        raise ValueError(
            f"{task_dir / 'ukol.yaml'}: typ flask vyžaduje soubor: a evaluate:"
        )
    py_path.write_text(format_flask_evaluator(soubor, tests), encoding="utf-8")
    sh_text = (SABLONY / "vpl_evaluate_flask.sh").read_text(encoding="utf-8")
    sh_text = sh_text.replace("\r\n", "\n")
    if not sh_text.endswith("\n"):
        sh_text += "\n"
    sh_path.write_bytes(sh_text.encode("utf-8"))


def lesson_dirs() -> list[Path]:
    dirs: list[Path] = []
    if not LEKCE_ROOT.is_dir():
        return dirs
    for rocnik_dir in sorted(LEKCE_ROOT.iterdir()):
        if not rocnik_dir.is_dir() or not rocnik_dir.name.endswith("-rocnik"):
            continue
        dirs.extend(
            d
            for d in rocnik_dir.iterdir()
            if d.is_dir() and re.match(r"\d{2}-", d.name)
        )
    return dirs


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
        print(f"  OK {lesson_dir.parent.name}/{lesson_dir.name} ({len(tasks)} ukolu)")
    print(f"Hotovo ({total} ukolu).")


if __name__ == "__main__":
    main()
