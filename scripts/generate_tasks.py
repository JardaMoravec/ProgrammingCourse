#!/usr/bin/env python3
"""Generuje ukoly.md a VPL testy (cases / Flask hodnotitel) z lekce/**/ukoly/*/ukol.yaml.

U tajných známkovaných úkolů (složka zNN-) vznikne i zadani.html pro vložení do Moodlu.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
LEKCE_ROOT = ROOT / "lekce"
SABLONY = ROOT / "sablony"

TASK_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9-]+)$")
SECRET_DIR_RE = re.compile(r"^z(\d{2})-([a-z0-9-]+)$")


def is_lesson_group(name: str) -> bool:
    return name.endswith("-rocnik") or name == "bonus"


def moodle_rocnik_code(rocnik: str) -> str:
    if rocnik == "bonus":
        return "B"
    return rocnik


def stars(n: int) -> str:
    return "★" * int(n) + "☆" * (3 - int(n))


_POSIX_ERE_SPECIAL = re.compile(r"([.^$*+?()\[\]{}|\\/])")
_NUMBER_AT_END = re.compile(r"(-?\d+(?:\.\d+)?)$")


def escape_posix_ere(text: str) -> str:
    return _POSIX_ERE_SPECIAL.sub(r"\\\1", text)


PROMPT_NOTE = (
    "**Výzva u `input()`:** libovolný text, nebo prázdné `input()`. Test výzvu ignoruje."
)


def case_reads_stdin(cases: list[dict]) -> bool:
    return any(str(c.get("input") or "").strip() for c in cases)


def _flexible_number(number: str) -> str:
    if "." not in number:
        return rf"{number}(\.0+)?"
    whole, frac = number.split(".", 1)
    significant = frac.rstrip("0")
    if significant:
        return rf"{whole}\.{significant}0*"
    return rf"{whole}(\.0+)?"


def prompt_tolerant_output(out: str, *, numeric: bool) -> str:
    """Výstup VPL, který ignoruje text vypsaný funkcí input().

    Očekávaný text musí být na konci. Před ním smí být výzva na stejném řádku
    i celé řádky s písmenem (typická výzva). Řádky jen z číslic navíc neprojdou,
    takže delší výpis není automaticky správný. U numeric se u posledního čísla
    povolí 16 i 16.0 i 16.00.
    """
    text = str(out).rstrip("\r\n")
    body = escape_posix_ere(text)
    if numeric:
        match = _NUMBER_AT_END.search(text)
        if match:
            body = escape_posix_ere(text[: match.start()]) + _flexible_number(
                match.group(1)
            )
    return (
        r"/^([^\n]*[[:alpha:]][^\n]*\n)*"
        r"([^\n]*[^[:alnum:]_])?"
        + body
        + r"[[:space:]]*$/"
    )


def ignore_prompts(task: dict, rocnik: str) -> bool:
    """Výzvu u input() ignorují testy v 1. a 2. ročníku."""
    if task.get("ignore_input_prompt"):
        return True
    return str(rocnik) in {"1", "2"} and case_reads_stdin(task.get("cases") or [])


def format_vpl_cases(cases: list[dict], *, ignore_input_prompt: bool = False) -> str:
    lines: list[str] = []
    tolerate = ignore_input_prompt
    for c in cases:
        lines.append(f"Case = {c['name']}")
        if c.get("input") is not None:
            lines.append(f"Input = {str(c['input']).rstrip()}")
        out = c.get("output")
        if out is not None:
            if tolerate:
                pattern = prompt_tolerant_output(
                    str(out), numeric=bool(c.get("numeric"))
                )
                lines.append(f"Output = {pattern}")
            elif c.get("numeric"):
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


def load_task(task_dir: Path, *, secret: bool = False) -> dict | None:
    match = (SECRET_DIR_RE if secret else TASK_DIR_RE).match(task_dir.name)
    yaml_path = task_dir / "ukol.yaml"
    if not match or not yaml_path.exists():
        return None
    raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{yaml_path}: ocekavan slovnik")
    task = {
        "id": f"z{match.group(1)}" if secret else match.group(1),
        "slug": match.group(2),
        "title": raw["title"],
        "stars": raw["stars"],
        "description": raw["description"],
        "cases": raw.get("cases") or [],
        "typ": raw.get("typ", "vpl"),
    }
    if raw.get("io"):
        task["io"] = raw["io"]
    if raw.get("ignore_input_prompt"):
        task["ignore_input_prompt"] = True
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
    if raw.get("seed") is not None:
        task["seed"] = raw["seed"]
    if raw.get("zakazane"):
        task["zakazane"] = list(raw["zakazane"])
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


def discover_secret_tasks(lesson_dir: Path) -> list[dict]:
    ukoly_root = lesson_dir / "ukoly"
    if not ukoly_root.is_dir():
        return []
    tasks: list[dict] = []
    for task_dir in sorted(ukoly_root.iterdir()):
        if not task_dir.is_dir():
            continue
        task = load_task(task_dir, secret=True)
        if task:
            tasks.append(task)
    return tasks


def cleanup_stale_ukoly(ukoly_root: Path, tasks: list[dict]) -> None:
    expected_dirs = {task_dir_name(t) for t in tasks}
    for child in ukoly_root.iterdir():
        if not child.is_dir():
            continue
        if child.name == "reseni" or SECRET_DIR_RE.match(child.name):
            continue
        if child.name not in expected_dirs:
            shutil.rmtree(child)


def assignment_markdown(task: dict, rocnik: str) -> str:
    """Zadání úkolu v Markdownu: popis, formát vstupu a výstupu, odevzdání."""
    description = strip_format_from_description(task["description"])
    parts = [f"# {task['title']}", "", description, ""]
    io = str(task["io"]).strip() if task.get("io") else ""
    if (
        str(rocnik) in {"1", "2"}
        and case_reads_stdin(task.get("cases") or [])
        and "Výzva u `input()`" not in io
    ):
        io = f"{io}\n{PROMPT_NOTE}".strip()
    if io:
        parts += ["**Formát:**", "", io, ""]
    if task.get("odevzdani"):
        parts += ["**Odevzdání:**", "", str(task["odevzdani"]).strip(), ""]
    return "\n".join(parts).rstrip() + "\n"


_CODE_LINE = re.compile(r"^\s*`[^`]+`\s*$")
_IO_LABEL = re.compile(r"^\*\*(Vstup|Výstup|Výzva)\b")


def prepare_assignment_markdown(text: str) -> str:
    """Ukázkový výstup a řádky Vstup/Výstup nechá jako samostatné odstavce."""
    out: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if _CODE_LINE.match(line) or _IO_LABEL.match(stripped):
            if out and out[-1] != "":
                out.append("")
            out.append(stripped)
            if _CODE_LINE.match(line):
                out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def format_secret_zadani_html(task: dict, rocnik: str) -> str:
    """Samostatná HTML stránka. Moodle Markdown nebere, text se vloží z prohlížeče."""
    body = markdown.markdown(
        prepare_assignment_markdown(assignment_markdown(task, rocnik)),
        extensions=["tables", "fenced_code", "attr_list"],
    )
    title = html.escape(str(task["title"]))
    return (
        "<!DOCTYPE html>\n"
        '<html lang="cs">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        f"<title>{title}</title>\n"
        "</head>\n"
        "<body>\n"
        "<!-- Otevřete v prohlížeči, označte zadání a vložte ho do Moodlu. -->\n"
        f"{body}\n"
        "</body>\n"
        "</html>\n"
    )


def write_secret_zadani_html(task_dir: Path, task: dict, rocnik: str) -> None:
    (task_dir / "zadani.html").write_text(
        format_secret_zadani_html(task, rocnik),
        encoding="utf-8",
    )


def strip_format_from_description(description: str) -> str:
    """Odstraní řádky „Formát:“ z popisu — formát patří do pole io."""
    lines = str(description).strip().splitlines()
    kept = [line for line in lines if not re.match(r"^\s*Formát\s*:", line, re.I)]
    return "\n".join(kept).strip()


def is_truthy_meta(value: str) -> bool:
    return value.strip().lower() in ("true", "ano", "1", "yes")


def build_ukoly_md(
    lesson_id: str,
    lesson_name: str,
    tasks: list[dict],
    rocnik: str,
    *,
    has_cviceni: bool = True,
    tajny_znamkovany: bool = False,
) -> str:
    num = lesson_id[:2]
    types = {(t.get("typ") or "vpl") for t in tasks}
    has_vpl = "vpl" in types and any(t.get("cases") for t in tasks)
    has_flask = "flask" in types
    has_sql = "sql" in types
    parts = [
        f"# Úkoly — {lesson_name}",
        "",
        "> **Samostatná práce** k odevzdání v AMOS.",
    ]
    if has_cviceni:
        parts += [
            "> U cvičení v hodině máte k dispozici řešení — u těchto úkolů ne.",
            "",
        ]
    else:
        parts.append("")
    if has_vpl:
        parts += [
            "> V AMOS spusťte **Evaluate** — automatický test ověří výstup programu.",
            "",
            "**Odevzdání:** soubor `main.py` (nebo název / způsob uvedený u úkolu).",
            "",
        ]
    elif has_flask:
        parts += [
            "> V AMOS spusťte **Evaluate** — test ověří routy a HTML značky",
            "> (text na stránce může být vlastní).",
            "",
        ]
    elif has_sql:
        parts += [
            "> V AMOS spusťte **Evaluate** — test spustí SQL ve SQLite a ověří tabulky.",
            "",
            "**Odevzdání:** soubor `reseni.sql`.",
            "",
        ]
    for t in tasks:
        moodle = t.get("moodle", f"PRG-{moodle_rocnik_code(rocnik)}-{num}-{t['id']}")
        description = strip_format_from_description(t["description"])
        parts += [
            "---",
            "",
            f"## Úkol {t['id']} — {t['title']} ({stars(t['stars'])}) {{#ukol-{t['id']}}}",
            "",
            f"**AMOS:** `{moodle}`",
            "",
            description,
            "",
        ]
        io = str(t["io"]).strip() if t.get("io") else ""
        if str(rocnik) in {"1", "2"} and case_reads_stdin(t.get("cases") or []) and "Výzva u `input()`" not in io:
            io = f"{io}\n{PROMPT_NOTE}".strip()
        if io:
            parts += ["**Formát:**", "", io, ""]
        if t.get("odevzdani"):
            parts += ["**Odevzdání:**", "", str(t["odevzdani"]).strip(), ""]
    if tajny_znamkovany:
        parts += [
            "---",
            "",
            "## Známkovaný úkol {#ukol-znamkovany}",
            "",
            "Lekce končí **známkovaným úkolem**. Zadání je **tajné** — dostanete ho",
            "od učitele. V těchto materiálech ani v AMOS předem není.",
            "",
        ]
    return "\n".join(parts)


def write_lesson_ukoly(lesson_dir: Path, tasks: list[dict]) -> None:
    meta = parse_meta(lesson_dir / "meta.yaml")
    nazev = meta.get("nazev", lesson_dir.name)
    rocnik = meta.get("rocnik", "1")
    (lesson_dir / "ukoly.md").write_text(
        build_ukoly_md(
            lesson_dir.name,
            nazev,
            tasks,
            rocnik,
            has_cviceni=(lesson_dir / "cviceni.md").is_file(),
            tajny_znamkovany=is_truthy_meta(meta.get("znamkovany_tajny", "")),
        ),
        encoding="utf-8",
    )

    ukoly_root = lesson_dir / "ukoly"
    ukoly_root.mkdir(parents=True, exist_ok=True)
    cleanup_stale_ukoly(ukoly_root, tasks)

    bundled_path = ukoly_root / "vpl_evaluate.cases"
    runner_path = ukoly_root / "vpl_run_ukol.sh"
    if bundled_path.exists():
        bundled_path.unlink()
    if runner_path.exists():
        runner_path.unlink()

    for t in tasks + discover_secret_tasks(lesson_dir):
        task_dir = ukoly_root / task_dir_name(t)
        task_dir.mkdir(parents=True, exist_ok=True)
        cases_path = task_dir / "vpl_evaluate.cases"
        if t["cases"]:
            cases_path.write_text(
                format_vpl_cases(
                    t["cases"],
                    ignore_input_prompt=ignore_prompts(t, rocnik),
                ),
                encoding="utf-8",
            )
        elif cases_path.exists():
            cases_path.unlink()
        write_custom_vpl(task_dir, t)
        if str(t["id"]).startswith("z"):
            write_secret_zadani_html(task_dir, t, rocnik)
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


def format_sql_evaluator(soubor: str, seed: str, tests: list) -> str:
    template = (SABLONY / "vpl_evaluate_sql.py").read_text(encoding="utf-8")
    for placeholder in ("__STUDENT_FILE__", "__SEED_PY__", "__TESTS__"):
        if placeholder not in template:
            raise ValueError(f"sablony/vpl_evaluate_sql.py: chybí {placeholder}")
    return (
        template.replace("__STUDENT_FILE__", soubor, 1)
        .replace("__SEED_PY__", json.dumps(seed or ""), 1)
        .replace("__TESTS__", json.dumps(tests, ensure_ascii=False, indent=2), 1)
    )


def write_run_sh(path: Path) -> None:
    sh_text = (SABLONY / "vpl_evaluate_flask.sh").read_text(encoding="utf-8")
    sh_text = sh_text.replace("\r\n", "\n")
    if not sh_text.endswith("\n"):
        sh_text += "\n"
    path.write_bytes(sh_text.encode("utf-8"))


def write_sql_run_sh(path: Path, soubor: str) -> None:
    sh_text = (SABLONY / "vpl_run_sql.sh").read_text(encoding="utf-8")
    sh_text = sh_text.replace("__STUDENT_FILE__", soubor, 1)
    sh_text = sh_text.replace("\r\n", "\n")
    if not sh_text.endswith("\n"):
        sh_text += "\n"
    path.write_bytes(sh_text.encode("utf-8"))


def format_slozeni_evaluator(soubor: str, zakazane: list) -> str:
    template = (SABLONY / "vpl_evaluate_slozeni.py").read_text(encoding="utf-8")
    for placeholder in ("__STUDENT_FILE__", "__ZAKAZANE__"):
        if placeholder not in template:
            raise ValueError(f"sablony/vpl_evaluate_slozeni.py: chybí {placeholder}")
    klice = sorted(
        {
            "".join(ch for ch in str(name).lower() if ch.isalnum())
            for name in zakazane
        }
    )
    return template.replace("__STUDENT_FILE__", soubor, 1).replace(
        "__ZAKAZANE__",
        json.dumps(klice, ensure_ascii=True),
        1,
    )


def write_custom_vpl(task_dir: Path, task: dict) -> None:
    py_path = task_dir / "vpl_evaluate.py"
    sh_path = task_dir / "vpl_evaluate.sh"
    run_path = task_dir / "vpl_run.sh"
    typ = task.get("typ")
    if typ == "slozeni":
        py_path.write_text(
            format_slozeni_evaluator(
                str(task.get("soubor") or "main.py"),
                list(task.get("zakazane") or []),
            ),
            encoding="utf-8",
        )
        write_run_sh(sh_path)
        if run_path.exists():
            run_path.unlink()
        return
    if typ not in ("flask", "sql"):
        if py_path.exists():
            py_path.unlink()
        if sh_path.exists():
            sh_path.unlink()
        if run_path.exists():
            run_path.unlink()
        return
    soubor = task.get("soubor")
    tests = task.get("evaluate") or []
    if not soubor or not tests:
        raise ValueError(
            f"{task_dir / 'ukol.yaml'}: typ {typ} vyžaduje soubor: a evaluate:"
        )
    if typ == "flask":
        py_path.write_text(format_flask_evaluator(soubor, tests), encoding="utf-8")
        if run_path.exists():
            run_path.unlink()
    else:
        py_path.write_text(
            format_sql_evaluator(soubor, str(task.get("seed") or ""), tests),
            encoding="utf-8",
        )
        write_sql_run_sh(run_path, soubor)
    write_run_sh(sh_path)


def lesson_dirs() -> list[Path]:
    dirs: list[Path] = []
    if not LEKCE_ROOT.is_dir():
        return dirs
    for group_dir in sorted(LEKCE_ROOT.iterdir()):
        if not group_dir.is_dir() or not is_lesson_group(group_dir.name):
            continue
        dirs.extend(
            d
            for d in group_dir.iterdir()
            if d.is_dir() and re.match(r"\d{2}-", d.name)
        )
    return dirs


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print("Generuji ukoly.md + VPL testy z lekce/**/ukoly/*/ukol.yaml ...")
    total = 0
    for lesson_dir in lesson_dirs():
        tasks = discover_tasks(lesson_dir)
        secrets = discover_secret_tasks(lesson_dir)
        if not tasks and not secrets:
            continue
        if tasks:
            write_lesson_ukoly(lesson_dir, tasks)
        elif secrets:
            ukoly_root = lesson_dir / "ukoly"
            rocnik = parse_meta(lesson_dir / "meta.yaml").get("rocnik", "1")
            for t in secrets:
                task_dir = ukoly_root / task_dir_name(t)
                task_dir.mkdir(parents=True, exist_ok=True)
                cases_path = task_dir / "vpl_evaluate.cases"
                if t["cases"]:
                    cases_path.write_text(
                        format_vpl_cases(
                            t["cases"],
                            ignore_input_prompt=ignore_prompts(t, rocnik),
                        ),
                        encoding="utf-8",
                    )
                write_secret_zadani_html(task_dir, t, rocnik)
        total += len(tasks)
        extra = f", {len(secrets)} tajnych" if secrets else ""
        print(
            f"  OK {lesson_dir.parent.name}/{lesson_dir.name} "
            f"({len(tasks)} ukolu{extra})"
        )
    print(f"Hotovo ({total} ukolu).")


if __name__ == "__main__":
    main()
