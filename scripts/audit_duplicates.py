#!/usr/bin/env python3
"""Audit shod mezi cviceni.md a ukol.yaml."""

from __future__ import annotations

import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent / "lekce" / "1-rocnik"


def norm(s: str) -> str:
    s = re.sub(r"\s+", " ", s.lower().strip())
    return re.sub(r"[^\w\s]", "", s, flags=re.UNICODE)


def sim(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def strip_reseni(text: str) -> str:
    return re.sub(r"@reseni.*?@end", "", text, flags=re.S)


def parse_cviceni(path: Path) -> list[dict]:
    text = strip_reseni(path.read_text(encoding="utf-8"))
    items: list[dict] = []
    pattern = re.compile(
        r"^##\s+Cvičení\s+\d+\s+—\s+(.+?)\s+\(([^)]+)\)\s*\n(.*?)(?=^##\s+Cvičení|\Z)",
        re.S | re.M,
    )
    for m in pattern.finditer(text):
        title = m.group(1).strip()
        body = re.sub(r"^>.*$", "", m.group(3), flags=re.M).strip()
        body = re.sub(r"\n+", " ", body)
        items.append({"title": title, "desc": body, "norm_title": norm(title)})
    return items


def load_ukoly(lesson_dir: Path) -> list[dict]:
    items: list[dict] = []
    ukoly = lesson_dir / "ukoly"
    if not ukoly.is_dir():
        return items
    for d in sorted(ukoly.iterdir()):
        yf = d / "ukol.yaml"
        if not yf.exists():
            continue
        raw = yaml.safe_load(yf.read_text(encoding="utf-8"))
        desc = re.sub(r"\n+", " ", str(raw.get("description", "")).strip())
        items.append(
            {
                "id": d.name,
                "title": raw["title"],
                "desc": desc,
                "norm_title": norm(raw["title"]),
                "cases": raw.get("cases", []),
            }
        )
    return items


def lesson_dirs() -> list[Path]:
    return sorted(
        (d for d in ROOT.iterdir() if d.is_dir() and re.match(r"\d{2}-", d.name)),
        key=lambda p: p.name,
    )


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    same_lesson_title: list[tuple] = []
    all_ukoly: list[dict] = []
    all_cviceni: list[dict] = []

    for lesson in lesson_dirs():
        cv_path = lesson / "cviceni.md"
        cv = parse_cviceni(cv_path) if cv_path.exists() else []
        uk = load_ukoly(lesson)
        for c in cv:
            c["lesson"] = lesson.name
            all_cviceni.append(c)
        for u in uk:
            u["lesson"] = lesson.name
            all_ukoly.append(u)
        for c in cv:
            for u in uk:
                if c["norm_title"] == u["norm_title"]:
                    same_lesson_title.append((lesson.name, c, u))

    print("=" * 72)
    print("1. STEJNÁ LEKCE — shodný název cvičení a úkolu")
    print("=" * 72)
    for lesson, c, u in same_lesson_title:
        print(f"\n{lesson} — {c['title']}")
        print(f"  Cvičení: {c['desc'][:140]}")
        print(f"  Úkol:    {u['desc'][:140]}")
        if u["cases"]:
            print(f"  VPL:     {u['cases'][0].get('output', '')[:80]}")

    print("\n" + "=" * 72)
    print("2. RŮZNÉ LEKCE — úkoly se stejným / velmi podobným názvem")
    print("=" * 72)
    for i, a in enumerate(all_ukoly):
        for b in all_ukoly[i + 1 :]:
            s = sim(a["norm_title"], b["norm_title"])
            if a["norm_title"] == b["norm_title"] or s >= 0.9:
                print(f"  {a['title']}")
                print(f"    {a['lesson']}/{a['id']}")
                print(f"    {b['lesson']}/{b['id']}")
                print()

    print("=" * 72)
    print("3. RŮZNÉ LEKCE — úkol vs cvičení (podobný název)")
    print("=" * 72)
    for u in all_ukoly:
        for c in all_cviceni:
            if u["lesson"] == c["lesson"]:
                continue
            s = sim(u["norm_title"], c["norm_title"])
            if u["norm_title"] == c["norm_title"] or s >= 0.88:
                print(f"  Úkol {u['lesson']}/{u['id']} ({u['title']})")
                print(f"    ~ cvičení {c['lesson']}: {c['title']}  (sim={s:.2f})")
                print()

    print("=" * 72)
    print("4. CVIČENÍ bez odpovídajícího úkolu (stejná lekce)")
    print("=" * 72)
    for lesson in lesson_dirs():
        cv_path = lesson / "cviceni.md"
        if not cv_path.exists():
            continue
        cv = parse_cviceni(cv_path)
        uk = load_ukoly(lesson)
        uk_norm = [u["norm_title"] for u in uk]
        for c in cv:
            if c["norm_title"] in uk_norm:
                continue
            if any(sim(c["norm_title"], ut) >= 0.85 for ut in uk_norm):
                continue
            print(f"  {lesson}: {c['title']}")

    print("\n" + "=" * 72)
    print("5. ÚKOLY bez odpovídajícího cvičení (stejná lekce)")
    print("=" * 72)
    for lesson in lesson_dirs():
        cv_path = lesson / "cviceni.md"
        if not cv_path.exists():
            continue
        cv = parse_cviceni(cv_path)
        uk = load_ukoly(lesson)
        cv_norm = [c["norm_title"] for c in cv]
        for u in uk:
            if u["norm_title"] in cv_norm:
                continue
            if any(sim(u["norm_title"], ct) >= 0.85 for ct in cv_norm):
                continue
            print(f"  {lesson}: {u['title']} ({u['id']})")

    print("\n" + "=" * 72)
    print(f"Souhrn: {len(same_lesson_title)} shodných párů cvičení↔úkol ve stejné lekci")
    print("=" * 72)


if __name__ == "__main__":
    main()
