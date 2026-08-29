# Používá generate_tasks.py — placeholdery nahradí generátor.
from __future__ import annotations

STUDENT_FILE = "__STUDENT_FILE__"
TESTS = __TESTS__

import importlib.util
import os
import re
import sys
import traceback
from pathlib import Path


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


def run_test(client, student: Path, test: dict) -> list[str]:
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

    if test.get("source_contains"):
        src = student.read_text(encoding="utf-8", errors="replace")
        for needle in test["source_contains"]:
            if needle not in src:
                errors.append(f"V {student.name} se nenašlo `{needle}`.")

    for rel, needles in (test.get("template_contains") or {}).items():
        found = find_template(root, rel)
        if found is None:
            continue
        text = found.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                errors.append(f"V templates/{rel} se nenašlo `{needle}`.")

    if "get" not in test:
        return errors

    if client is None:
        errors.append("GET nelze spustit — aplikace se nenačetla.")
        return errors

    path = test.get("get") or "/"
    expected_status = int(test.get("status", 200))
    try:
        response = client.get(path)
    except Exception as exc:
        errors.append(f"Požadavek GET {path} selhal: {exc}")
        return errors

    if response.status_code != expected_status:
        errors.append(
            f"GET {path}: stav {response.status_code}, očekáváno {expected_status}."
        )
        if response.status_code == 404:
            errors.append("Routa v aplikaci chybí, nebo má jinou cestu.")
        return errors

    html = response.get_data(as_text=True) or ""
    for tag in test.get("tags") or []:
        if count_tag(html, tag) < 1:
            errors.append(f"Na {path} chybí značka <{tag}>.")

    min_tags = test.get("min_tags") or {}
    for tag, minimum in min_tags.items():
        n = count_tag(html, tag)
        if n < int(minimum):
            errors.append(
                f"Na {path} je <{tag}> {n}×, potřeba aspoň {minimum}×."
            )

    hrefs = find_hrefs(html)
    for target in test.get("href") or []:
        wanted = norm_path(target)
        if wanted not in hrefs:
            errors.append(
                f"Na {path} chybí odkaz na {wanted} (atribut href)."
            )

    for needle in test.get("contains") or []:
        if needle not in html:
            errors.append(f"Na {path} chybí `{needle}`.")

    for needle in test.get("not_contains") or []:
        if needle in html:
            errors.append(
                f"Na {path} se nesmí objevit `{needle}` "
                f"(šablona se pravděpodobně nevykreslila)."
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

    client = None
    try:
        app = load_app(student)
        app.config["TESTING"] = True
        client = app.test_client()
    except Exception as exc:
        section(False, "Načtení aplikace")
        comment(str(exc))
        tb = traceback.format_exc().strip().splitlines()
        for line in tb[-8:]:
            comment(line)

    passed = 0
    total = len(TESTS)
    for test in TESTS:
        name = str(test.get("name") or test.get("get") or "test")
        errors = run_test(client, student, test)
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
