# Používá generate_tasks.py — placeholdery nahradí generátor.
from __future__ import annotations

import json
import os
import sqlite3
import sys
from pathlib import Path

STUDENT_FILE = "__STUDENT_FILE__"
SEED = __SEED_PY__
TESTS = json.loads(r"""__TESTS__""")


def comment(text: str) -> None:
    print(f"Comment :=>> {text}")


def section(ok: bool, name: str) -> None:
    znacka = "OK" if ok else "CHYBA"
    print(f"Comment :=>>-{znacka}: {name}")


def grade_limits() -> tuple[float, float]:
    gmin = float(os.environ.get("VPL_GRADEMIN", "0"))
    gmax = float(os.environ.get("VPL_GRADEMAX", "100"))
    return gmin, gmax


def qi(name: str) -> str:
    return '"' + str(name).replace('"', '""') + '"'


def table_names(con: sqlite3.Connection) -> list[str]:
    rows = con.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    return [r[0] for r in rows]


def find_table(con: sqlite3.Connection, name: str) -> str | None:
    for existing in table_names(con):
        if existing.lower() == name.lower():
            return existing
    return None


def column_rows(con: sqlite3.Connection, table: str) -> list[dict]:
    info = con.execute(f"PRAGMA table_info({qi(table)})").fetchall()
    unique_cols: set[str] = set()
    for idx in con.execute(f"PRAGMA index_list({qi(table)})").fetchall():
        if not idx[2]:
            continue
        for col in con.execute(f"PRAGMA index_info({qi(idx[1])})").fetchall():
            if col[2]:
                unique_cols.add(str(col[2]).lower())
    out = []
    for cid, name, typ, notnull, _default, pk in info:
        out.append(
            {
                "name": name,
                "type": (typ or "").upper(),
                "notnull": int(notnull),
                "pk": int(pk),
                "unique": name.lower() in unique_cols or int(pk) > 0,
            }
        )
    return out


def check_test(con: sqlite3.Connection, test: dict) -> list[str]:
    errors: list[str] = []
    required = test.get("tables") or []
    if test.get("table"):
        required = list(required) + [test["table"]]
    found = {n.lower(): n for n in table_names(con)}
    for name in required:
        if name.lower() not in found:
            have = ", ".join(table_names(con)) or "(žádná)"
            errors.append(f"Chybí tabulka {name}. V databázi je: {have}.")
    if errors:
        return errors

    table = test.get("table")
    if not table:
        return errors
    real = found[table.lower()]
    cols = column_rows(con, real)
    by_name = {c["name"].lower(): c for c in cols}
    for spec in test.get("columns") or []:
        cname = spec["name"]
        col = by_name.get(cname.lower())
        if col is None:
            have = ", ".join(c["name"] for c in cols) or "(žádný)"
            errors.append(f"V tabulce {real} chybí sloupec {cname}. Jsou tam: {have}.")
            continue
        if spec.get("type") and col["type"] != str(spec["type"]).upper():
            errors.append(
                f"Sloupec {real}.{col['name']} má typ {col['type'] or '(prázdný)'}, "
                f"očekávám {str(spec['type']).upper()}."
            )
        if "notnull" in spec and col["notnull"] != int(spec["notnull"]):
            stav = "je" if col["notnull"] else "není"
            errors.append(f"Sloupec {real}.{col['name']} {stav} NOT NULL.")
        if spec.get("pk") and col["pk"] <= 0:
            errors.append(f"Sloupec {real}.{col['name']} není primární klíč.")
        if spec.get("unique") and not col["unique"]:
            errors.append(f"Sloupec {real}.{col['name']} není UNIQUE.")

    for fk in test.get("foreign_keys") or []:
        want_from = str(fk["column"]).lower()
        want_table = str(fk["ref_table"]).lower()
        want_to = str(fk.get("ref_column") or "id").lower()
        listed = con.execute(f"PRAGMA foreign_key_list({qi(real)})").fetchall()
        ok = False
        for row in listed:
            if (
                str(row[3]).lower() == want_from
                and str(row[2]).lower() == want_table
                and str(row[4]).lower() == want_to
            ):
                ok = True
                break
        if not ok:
            errors.append(
                f"V tabulce {real} chybí cizí klíč {fk['column']} → {fk['ref_table']}.{fk.get('ref_column') or 'id'}."
            )
    return errors


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    student = Path(STUDENT_FILE)
    gmin, gmax = grade_limits()
    if not student.is_file():
        comment(f"Chybí soubor {STUDENT_FILE}. Nahrajte ho pod přesně tímto názvem.")
        print(f"Grade :=>> {gmin}")
        return 0

    sql = student.read_text(encoding="utf-8")
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA foreign_keys = ON")
    try:
        if str(SEED).strip():
            con.executescript(str(SEED))
        con.executescript(sql)
    except sqlite3.Error as exc:
        section(False, "Spuštění SQL")
        comment(str(exc))
        print(f"Grade :=>> {gmin}")
        return 0

    passed = 0
    total = len(TESTS)
    for test in TESTS:
        name = str(test.get("name") or test.get("table") or "test")
        errors = check_test(con, test)
        ok = not errors
        section(ok, name)
        if ok:
            comment("Splněno.")
            passed += 1
        else:
            for err in errors:
                comment(err)

    if total == 0:
        grade = gmin
    else:
        grade = gmin + (gmax - gmin) * (passed / total)
    comment(f"Výsledek: {passed}/{total} testů.")
    print(f"Grade :=>> {grade:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
