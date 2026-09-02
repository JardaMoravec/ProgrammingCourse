# Používá generate_tasks.py — placeholdery nahradí generátor.
from __future__ import annotations

import json

STUDENT_FILE = "__STUDENT_FILE__"
TESTS = json.loads(r"""__TESTS__""")

import importlib.util
import os
import re
import sqlite3
import sys
import traceback
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse


def comment(text: str) -> None:
    print(f"Comment :=>> {text}")


def section(ok: bool, name: str) -> None:
    znacka = "OK" if ok else "CHYBA"
    print(f"Comment :=>>-{znacka}: {name}")


def count_tag(html: str, tag: str) -> int:
    return len(re.findall(rf"<{re.escape(tag)}\b", html, flags=re.I))


def norm_path(path: str) -> str:
    p = (path or "").strip()
    if not p:
        return ""
    if re.match(r"^(https?:|#|mailto:)", p, flags=re.I):
        return p
    if not p.startswith("/"):
        p = "/" + p
    if p != "/":
        p = p.rstrip("/")
    return p


def find_hrefs(html: str) -> list[str]:
    found = re.findall(r"""href\s*=\s*['"]([^'"]+)['"]""", html, flags=re.I)
    return [norm_path(h) for h in found]


def load_app(path: Path):
    try:
        from flask import Flask
    except ImportError:
        comment(
            "Ve výpočetním prostředí VPL chybí Flask. "
            "Učitel: nainstalujte balíček flask do jailu automatického hodnocení."
        )
        raise

    spec = importlib.util.spec_from_file_location("student_hw", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Soubor {path.name} nejde načíst.")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["student_hw"] = mod
    spec.loader.exec_module(mod)

    apps = [
        getattr(mod, name)
        for name in dir(mod)
        if isinstance(getattr(mod, name, None), Flask)
    ]
    if not apps:
        raise RuntimeError(
            "V souboru není instance Flask — očekává se např. app = Flask(__name__)."
        )
    app = apps[0]
    root = path.resolve().parent
    app.template_folder = str(root / "templates")
    app.static_folder = str(root / "static")
    return app


def find_in_dir(root: Path, folder: str, rel: str) -> Path | None:
    nested = root / folder / rel
    if nested.is_file():
        return nested
    flat = root / rel
    if flat.is_file():
        return flat
    return None


def find_template(root: Path, rel: str) -> Path | None:
    return find_in_dir(root, "templates", rel)


def location_path(header: str) -> str:
    h = (header or "").strip()
    if not h:
        return ""
    parsed = urlparse(h)
    path = parsed.path or "/"
    return norm_path(path)


def post_payload(spec: dict) -> dict:
    raw = spec.get("data") or {}
    data = {str(k): "" if v is None else str(v) for k, v in raw.items()}
    for field, item in (spec.get("upload") or {}).items():
        if item is None:
            continue
        if isinstance(item, str):
            filename, content, ctype = item, b"x", None
        else:
            filename = str(item.get("filename") or "")
            raw_content = item.get("content", "x")
            if raw_content is None:
                content = b""
            elif isinstance(raw_content, str):
                content = raw_content.encode("utf-8")
            else:
                content = bytes(raw_content)
            ctype = item.get("content_type")
        payload = BytesIO(content)
        if ctype:
            data[str(field)] = (payload, filename, str(ctype))
        else:
            data[str(field)] = (payload, filename)
    return data


def send_http(client, spec: dict):
    follow = bool(spec.get("follow_redirects"))
    if "post" in spec:
        path = spec.get("post") or "/"
        try:
            response = client.post(
                path, data=post_payload(spec), follow_redirects=follow
            )
        except Exception as exc:
            return "POST", path, None, [f"Požadavek POST {path} selhal: {exc}"]
        return "POST", path, response, []
    path = spec.get("get") or "/"
    try:
        response = client.get(path, follow_redirects=follow)
    except Exception as exc:
        return "GET", path, None, [f"Požadavek GET {path} selhal: {exc}"]
    return "GET", path, response, []


def check_response(response, spec: dict, method: str, path: str, root: Path) -> list[str]:
    errors: list[str] = []
    expected_status = int(spec.get("status", 200))
    if response.status_code != expected_status:
        errors.append(
            f"{method} {path}: stav {response.status_code}, očekáváno {expected_status}."
        )
        if response.status_code == 404:
            errors.append("Routa v aplikaci chybí, nebo má jinou cestu.")
        if response.status_code == 405:
            errors.append(
                f"Tato cesta metodu {method} nepřijímá "
                "(u POST doplňte methods=['GET', 'POST'])."
            )
        if expected_status == 302 and response.status_code == 200:
            errors.append("Očekáváno přesměrování — vraťte redirect(...), ne šablonu.")
        return errors

    if "location" in spec:
        wanted = norm_path(str(spec.get("location") or "/"))
        got = location_path(response.headers.get("Location") or "")
        if got != wanted:
            errors.append(
                f"{method} {path}: Location {got or '(chybí)'}, očekáváno {wanted}."
            )

    html = response.get_data(as_text=True) or ""
    where = f"{method} {path}"
    for tag in spec.get("tags") or []:
        if count_tag(html, tag) < 1:
            errors.append(f"Na {where} chybí značka <{tag}>.")

    min_tags = spec.get("min_tags") or {}
    for tag, minimum in min_tags.items():
        n = count_tag(html, tag)
        if n < int(minimum):
            errors.append(
                f"Na {where} je <{tag}> {n}×, potřeba aspoň {minimum}×."
            )

    hrefs = find_hrefs(html)
    for target in spec.get("href") or []:
        wanted = norm_path(target)
        if wanted not in hrefs:
            errors.append(
                f"Na {where} chybí odkaz na {wanted} (atribut href)."
            )

    for needle in spec.get("contains") or []:
        if needle not in html:
            errors.append(f"Na {where} chybí `{needle}`.")

    for needle in spec.get("not_contains") or []:
        if needle in html:
            errors.append(
                f"Na {where} se nesmí objevit `{needle}` "
                f"(šablona se pravděpodobně nevykreslila)."
            )

    for rel in spec.get("saved") or []:
        if not (root / str(rel)).is_file():
            errors.append(
                f"Po odeslání chybí soubor {rel} "
                "(uložte nahrávku do static/uploads/)."
            )

    errors.extend(check_sqlite(root, spec))
    return errors


def check_sqlite(root: Path, spec: dict) -> list[str]:
    db_rel = spec.get("db")
    if not db_rel:
        return []
    errors: list[str] = []
    path = root / str(db_rel)
    if not path.is_file():
        errors.append(
            f"Chybí databáze {db_rel} "
            "(při požadavku ji vytvořte přes sqlite3.connect)."
        )
        return errors
    try:
        conn = sqlite3.connect(path)
    except Exception as exc:
        errors.append(f"Soubor {db_rel} nejde otevřít jako SQLite: {exc}")
        return errors
    try:
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        }
        for name in spec.get("db_tables") or []:
            if name not in tables:
                errors.append(f"V {db_rel} chybí tabulka `{name}`.")
        for name, minimum in (spec.get("db_min_rows") or {}).items():
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", str(name)):
                continue
            if name not in tables:
                continue
            n = conn.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
            if n < int(minimum):
                errors.append(
                    f"Tabulka `{name}` má {n} řádků, potřeba aspoň {minimum}."
                )
    finally:
        conn.close()
    return errors


def apply_db_seed(root: Path, spec: dict) -> list[str]:
    seed = spec.get("db_seed")
    if not seed:
        return []
    db_rel = seed.get("db") or spec.get("db")
    table = str(seed.get("table") or "")
    columns = [str(c) for c in (seed.get("columns") or [])]
    rows = seed.get("rows") or []
    ident = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
    if not db_rel or not ident.fullmatch(table) or not columns:
        return ["db_seed: chybí db, table nebo columns."]
    if any(not ident.fullmatch(c) for c in columns):
        return ["db_seed: neplatný název sloupce."]
    path = root / str(db_rel)
    if not path.is_file():
        return [
            f"Chybí databáze {db_rel} — nejdřív ji založte v init_db "
            "(CREATE TABLE)."
        ]
    placeholders = ", ".join("?" for _ in columns)
    colsql = ", ".join(columns)
    conn = None
    try:
        conn = sqlite3.connect(path)
        conn.execute(f"DELETE FROM {table}")
        conn.executemany(
            f"INSERT INTO {table} ({colsql}) VALUES ({placeholders})",
            [tuple(row) for row in rows],
        )
        conn.commit()
    except Exception as exc:
        return [f"Nelze naplnit tabulku `{table}` v {db_rel}: {exc}"]
    finally:
        if conn is not None:
            conn.close()
    return []


def run_http(client, spec: dict, root: Path) -> list[str]:
    method, path, response, errors = send_http(client, spec)
    if errors or response is None:
        return errors
    return check_response(response, spec, method, path, root)


def run_test(app, student: Path, test: dict) -> list[str]:
    errors: list[str] = []
    root = student.parent

    for rel in test.get("templates") or []:
        if find_template(root, rel) is None:
            errors.append(
                f"Chybí šablona templates/{rel} "
                f"(nahrajte ji ve složce templates/ vedle {student.name})."
            )

    for rel in test.get("static") or []:
        if find_in_dir(root, "static", rel) is None:
            errors.append(
                f"Chybí soubor static/{rel} "
                f"(nahrajte ho ve složce static/ vedle {student.name})."
            )

    src = None
    if test.get("source_contains") or test.get("source_not_contains"):
        src = student.read_text(encoding="utf-8", errors="replace")
    for needle in test.get("source_contains") or []:
        if needle not in src:
            errors.append(f"V {student.name} se nenašlo `{needle}`.")
    for needle in test.get("source_not_contains") or []:
        if needle in src:
            errors.append(f"V {student.name} se nesmí objevit `{needle}`.")

    for rel, needles in (test.get("template_contains") or {}).items():
        found = find_template(root, rel)
        if found is None:
            continue
        text = found.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                errors.append(f"V templates/{rel} se nenašlo `{needle}`.")

    if "get" not in test and "post" not in test:
        return errors

    if app is None:
        errors.append("Požadavek nelze spustit — aplikace se nenačetla.")
        return errors

    client = app.test_client()
    errors.extend(apply_db_seed(root, test))
    errors.extend(run_http(client, test, root))
    for extra in test.get("then") or []:
        if isinstance(extra, dict):
            errors.extend(run_http(client, extra, root))

    other_path = test.get("other_get")
    if other_path is not None:
        other = app.test_client()
        try:
            other_resp = other.get(other_path or "/")
        except Exception as exc:
            errors.append(f"Požadavek GET {other_path} (jiný klient) selhal: {exc}")
            return errors
        other_html = other_resp.get_data(as_text=True) or ""
        for needle in test.get("other_not_contains") or []:
            if needle in other_html:
                errors.append(
                    f"Jiný klient na GET {other_path} vidí `{needle}`. "
                    "Použijte session, ne globální proměnnou."
                )

    return errors


def grade_limits() -> tuple[float, float]:
    gmin = float(os.environ.get("VPL_GRADEMIN", "0"))
    gmax = float(os.environ.get("VPL_GRADEMAX", "100"))
    return gmin, gmax


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

    student = Path(STUDENT_FILE)
    if not student.is_file():
        comment(f"Chybí soubor {STUDENT_FILE}. Nahrajte ho pod přesně tímto názvem.")
        gmin, _ = grade_limits()
        print(f"Grade :=>> {gmin}")
        return 0

    app = None
    try:
        app = load_app(student)
        app.config["TESTING"] = True
    except Exception as exc:
        section(False, "Načtení aplikace")
        comment(str(exc))
        tb = traceback.format_exc().strip().splitlines()
        for line in tb[-8:]:
            comment(line)

    passed = 0
    total = len(TESTS)
    for test in TESTS:
        name = str(test.get("name") or test.get("get") or test.get("post") or "test")
        errors = run_test(app, student, test)
        ok = not errors
        section(ok, name)
        if ok:
            comment("Splněno.")
            passed += 1
        else:
            for err in errors:
                comment(err)

    gmin, gmax = grade_limits()
    if total == 0:
        grade = gmin
    else:
        grade = gmin + (gmax - gmin) * (passed / total)
    comment(f"Výsledek: {passed}/{total} testů.")
    print(f"Grade :=>> {grade:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
