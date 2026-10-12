# Používá generate_tasks.py — placeholdery nahradí generátor.
"""Hodnotitel OOP úkolu: struktura tříd a zároveň výstup programu."""

from __future__ import annotations

import ast
import io
import json
import re
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path

STUDENT_FILE = "__STUDENT_FILE__"
DATA = json.loads(r"""__TESTS__""")


def comment(text: str) -> None:
    print(f"Comment :=>> {text}")


def section(ok: bool, name: str) -> None:
    znacka = "OK" if ok else "CHYBA"
    print(f"Comment :=>>-{znacka}: {name}")


def _tridy(tree: ast.AST) -> list[ast.ClassDef]:
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def _metody(cls: ast.ClassDef) -> list[ast.FunctionDef]:
    return [
        node
        for node in cls.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]


def _parametry(init: ast.FunctionDef) -> list[str]:
    names = [arg.arg for arg in init.args.posonlyargs]
    names += [arg.arg for arg in init.args.args]
    names += [arg.arg for arg in init.args.kwonlyargs]
    return [name for name in names if name != "self"]


def _zakladni(cls: ast.ClassDef) -> list[str]:
    names: list[str] = []
    for base in cls.bases:
        if isinstance(base, ast.Name):
            names.append(base.id)
        elif isinstance(base, ast.Attribute):
            names.append(base.attr)
    return names


def _sbirej_atributy(target: ast.AST, found: set[str]) -> None:
    if (
        isinstance(target, ast.Attribute)
        and isinstance(target.value, ast.Name)
        and target.value.id == "self"
    ):
        found.add(target.attr)
        return
    if isinstance(target, (ast.Tuple, ast.List)):
        for item in target.elts:
            _sbirej_atributy(item, found)


def _prirazene_atributy(init: ast.FunctionDef) -> set[str]:
    found: set[str] = set()
    for node in ast.walk(init):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets = [node.target]
        for target in targets:
            _sbirej_atributy(target, found)
    return found


def _je_kontejner(node: ast.AST) -> bool:
    if isinstance(node, (ast.List, ast.Dict, ast.Set)):
        return True
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"list", "dict", "set"}
        and not node.args
        and not node.keywords
    )


def _ma_kontejner_vychozi(init: ast.FunctionDef) -> bool:
    defaults = list(init.args.defaults)
    defaults += [item for item in init.args.kw_defaults if item is not None]
    return any(item is not None and _je_kontejner(item) for item in defaults)


def _spec_tridy() -> list[dict]:
    return list(DATA["struktura"].get("tridy") or [])


def _atributy(spec: dict) -> list[str]:
    names: list[str] = []
    for attr in spec.get("atributy") or []:
        if isinstance(attr, str):
            names.append(attr)
        else:
            names.append(str(attr["jmeno"]))
    return names


def _seznam_pravidlo(trida: str, atribut: str) -> dict | None:
    spec = next((item for item in _spec_tridy() if item.get("jmeno") == trida), None)
    if spec is None:
        return None
    for rule in spec.get("seznamy") or []:
        if rule.get("atribut") == atribut:
            return rule
    return None


def _zkontroluj_ast(tree: ast.AST) -> list[str]:
    chyby: list[str] = []
    tridy = _tridy(tree)
    jen_init = bool(DATA["struktura"].get("jen_init"))
    for cls in tridy:
        metody = _metody(cls)
        if jen_init and any(method.name != "__init__" for method in metody):
            chyby.append(
                f"Třída {cls.name} smí mít jen __init__, žádnou další metodu."
            )
        for method in metody:
            if method.name == "__init__" and _ma_kontejner_vychozi(method):
                chyby.append(
                    f"V __init__ třídy {cls.name} nesmí být výchozí seznam, "
                    "slovník ani množina (třeba exponaty=[]). "
                    "Seznam založte v těle konstruktoru."
                )
    for spec in _spec_tridy():
        jmeno = str(spec["jmeno"])
        nalezene = [cls for cls in tridy if cls.name == jmeno]
        if len(nalezene) != 1:
            chyby.append(f"V souboru musí být právě jedna třída {jmeno}.")
            continue
        cls = nalezene[0]
        zakazane = {str(name) for name in spec.get("neni_potomek") or []}
        for base in _zakladni(cls):
            if base in zakazane:
                chyby.append(
                    f"Třída {jmeno} nesmí dědit z {base}. "
                    "Objekt vložte atributem."
                )
        inity = [method for method in _metody(cls) if method.name == "__init__"]
        if len(inity) != 1:
            chyby.append(f"Třída {jmeno} musí mít právě jeden __init__.")
            continue
        init = inity[0]
        hlavicka = [arg.arg for arg in init.args.posonlyargs]
        hlavicka += [arg.arg for arg in init.args.args]
        if not hlavicka or hlavicka[0] != "self":
            chyby.append(f"__init__ třídy {jmeno} musí začínat parametrem self.")
        chybi = [
            name for name in _atributy(spec) if name not in _prirazene_atributy(init)
        ]
        if chybi:
            cile = ", ".join(f"self.{name}" for name in chybi)
            chyby.append(
                f"V __init__ třídy {jmeno} chybí přiřazení: {cile}. "
                "Atribut nastavte v konstruktoru, ne až po vytvoření objektu."
            )
    return chyby


def _instrumentuj(tree: ast.AST) -> None:
    for cls in _tridy(tree):
        for method in _metody(cls):
            if method.name != "__init__":
                continue
            names = _parametry(method)
            start = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="_vpl_zacatek", ctx=ast.Load()),
                    args=[
                        ast.Name(id="self", ctx=ast.Load()),
                        ast.Dict(
                            keys=[ast.Constant(value=name) for name in names],
                            values=[ast.Name(id=name, ctx=ast.Load()) for name in names],
                        ),
                    ],
                    keywords=[],
                )
            )
            end = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="_vpl_konec", ctx=ast.Load()),
                    args=[ast.Name(id="self", ctx=ast.Load())],
                    keywords=[],
                )
            )
            method.body.insert(0, start)
            method.body.append(end)
    ast.fix_missing_locations(tree)


def _vystup_sedi(actual: str, expected: str) -> bool:
    actual_n = actual.replace("\r\n", "\n")
    expected_n = str(expected).replace("\r\n", "\n").rstrip("\n")
    if not DATA.get("ignoruj_vyzvu"):
        return actual_n.strip() == expected_n.strip()
    body = re.escape(expected_n)
    pattern = (
        r"\A(?:[^\n]*[^\W\d_][^\n]*\n)*(?:[^\n]*[^\w])?"
        + body
        + r"\s*\Z"
    )
    return re.search(pattern, actual_n) is not None


def _jedna_radka(text: str) -> str:
    flat = text.replace("\r\n", "\n").strip().replace("\n", " | ")
    if not flat:
        return "(prázdný výstup)"
    if len(flat) > 240:
        return flat[:240] + "…"
    return flat


def _polozek(count: int) -> str:
    if count == 1:
        return "1 položku"
    if 2 <= count <= 4:
        return f"{count} položky"
    return f"{count} položek"


def _porovnej(snap: dict, spec: dict) -> str | None:
    ocekavana = str(spec.get("trida") or "")
    if snap.get("cls") != ocekavana:
        return f"Očekávána třída {ocekavana}, nalezeno {snap.get('cls')}."
    for key, expected in spec.items():
        if key == "trida":
            continue
        if key not in snap.get("attrs", {}):
            return (
                f"Objekt {ocekavana} nemá atribut {key} nastavený v __init__."
            )
        actual = snap["attrs"][key]
        if isinstance(expected, list):
            chyba = _porovnej_seznam(snap, key, actual, expected)
            if chyba:
                return chyba
            continue
        if actual != expected or isinstance(actual, bool) != isinstance(expected, bool):
            doplnek = ""
            if isinstance(expected, int) and not isinstance(expected, bool):
                doplnek = " Má to být celé číslo."
            return (
                f"Atribut {key} je na konci __init__ {actual!r}, "
                f"očekáváno {expected!r}.{doplnek}"
            )
    return None


def _porovnej_seznam(snap: dict, key: str, actual: object, expected: list) -> str | None:
    if not isinstance(actual, dict) or "__list__" not in actual:
        return f"Atribut {key} má být seznam."
    pravidlo = _seznam_pravidlo(str(snap.get("cls")), key)
    if pravidlo and pravidlo.get("novy") and actual.get("__z_parametru__"):
        return (
            f"Seznam {key} nesmí být hotový seznam z parametru. "
            "Vytvořte ho v těle konstruktoru z jednotlivých objektů."
        )
    items = list(actual["__list__"])
    if pravidlo and pravidlo.get("pocet") is not None and len(items) != int(pravidlo["pocet"]):
        return (
            f"Seznam {key} má mít {_polozek(int(pravidlo['pocet']))}, "
            f"má {len(items)}."
        )
    if len(items) != len(expected):
        return (
            f"Seznam {key} má mít {_polozek(len(expected))}, má {len(items)}."
        )
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        return f"V seznamu {key} je stejný objekt víckrát."
    povolene = snap.get("param_id") or set()
    for index, (item, exp) in enumerate(zip(items, expected), start=1):
        if not isinstance(exp, dict):
            return f"Položka {index} v seznamu {key} nesedí."
        if pravidlo and item.get("cls") != pravidlo.get("trida"):
            return (
                f"Položka {index} v seznamu {key} má být {pravidlo.get('trida')}, "
                f"je {item.get('cls')}."
            )
        if pravidlo and pravidlo.get("novy"):
            vlastni = bool(item.get("vznik_uvnitr")) or item.get("id") in povolene
            if not vlastni:
                return (
                    f"Položka {index} v seznamu {key} musí přijít parametrem "
                    f"konstruktoru, nebo ji třída vytvoří uvnitř __init__. "
                    "Hotový seznam zvenku nestačí."
                )
        chyba = _porovnej(item, exp)
        if chyba:
            return chyba
    return None


def _najdi_instanci(registry: dict, spec: dict) -> str | None:
    candidates = [
        snap for snap in registry.values() if snap.get("cls") == spec.get("trida")
    ]
    if not candidates:
        return f"Program nevytvořil objekt třídy {spec.get('trida')}."
    chyby = []
    for snap in candidates:
        chyba = _porovnej(snap, spec)
        if chyba is None:
            return None
        chyby.append(chyba)
    if len(candidates) == 1:
        return chyby[0]
    return f"Žádný objekt třídy {spec.get('trida')} nesedí. {chyby[0]}"


def _spust(source: str, stdin_text: str) -> tuple[str | None, dict, str | None]:
    registry: dict[int, dict] = {}
    po_startu: dict[int, dict] = {}
    aktivni: list[str] = []

    def _odkaz(item: object) -> dict:
        found = registry.get(id(item))
        if found is not None:
            return found
        if isinstance(item, (str, int, float, bool)) or item is None:
            return {
                "cls": type(item).__name__,
                "attrs": {},
                "id": id(item),
                "vznik_uvnitr": False,
            }
        attrs = {}
        if hasattr(item, "__dict__"):
            attrs = {
                key: value
                for key, value in vars(item).items()
                if not str(key).startswith("_") and not isinstance(value, list)
            }
        return {
            "cls": type(item).__name__,
            "attrs": attrs,
            "id": id(item),
            "vznik_uvnitr": False,
        }

    def _vpl_zacatek(self, parametry: dict) -> None:
        aktivni.append(type(self).__name__)
        po_startu[id(self)] = {
            "param_id": {id(value) for value in parametry.values()},
            "param_listu": {
                id(value) for value in parametry.values() if isinstance(value, list)
            },
        }

    def _vpl_konec(self) -> None:
        try:
            info = po_startu.get(id(self), {})
            attrs: dict = {}
            for key, value in vars(self).items():
                if str(key).startswith("_"):
                    continue
                if isinstance(value, list):
                    attrs[key] = {
                        "__list__": [_odkaz(item) for item in value],
                        "__z_parametru__": id(value) in info.get("param_listu", ()),
                    }
                else:
                    attrs[key] = value
            registry[id(self)] = {
                "cls": type(self).__name__,
                "id": id(self),
                "vznik_uvnitr": len(aktivni) > 1,
                "param_id": set(info.get("param_id") or ()),
                "attrs": attrs,
            }
        finally:
            if aktivni:
                aktivni.pop()

    tree = ast.parse(source)
    _instrumentuj(tree)
    namespace = {
        "__name__": "__main__",
        "_vpl_zacatek": _vpl_zacatek,
        "_vpl_konec": _vpl_konec,
    }
    data = stdin_text or ""
    if data and not data.endswith("\n"):
        data += "\n"
    buffer = io.StringIO()
    old_stdin = sys.stdin
    try:
        sys.stdin = io.StringIO(data)
        with redirect_stdout(buffer):
            exec(compile(tree, STUDENT_FILE, "exec"), namespace, namespace)
    except KeyboardInterrupt:
        raise
    except BaseException as exc:
        last = traceback.format_exception_only(type(exc), exc)[-1].strip()
        return None, {}, f"Program spadl při spuštění: {last}"
    finally:
        sys.stdin = old_stdin
    return buffer.getvalue(), registry, None


def _ohodnot_pripad(source: str, case: dict) -> list[str]:
    stdout, registry, chyba = _spust(source, str(case.get("input") or ""))
    if chyba:
        return [chyba]
    problemy: list[str] = []
    if not _vystup_sedi(stdout or "", str(case.get("output") or "")):
        problemy.append(
            "Výstup nesedí. "
            f"Očekáváno: {_jedna_radka(str(case.get('output') or ''))}. "
            f"Program vypsal: {_jedna_radka(stdout or '')}."
        )
    instance = case.get("instance")
    if isinstance(instance, dict):
        objekt = _najdi_instanci(registry, instance)
        if objekt:
            problemy.append(objekt)
    return problemy


def main() -> None:
    student = Path(STUDENT_FILE)
    if not student.is_file():
        comment(f"Chybí soubor {STUDENT_FILE}.")
        print("Grade :=>> 0")
        return
    try:
        source = student.read_text(encoding="utf-8-sig")
    except UnicodeError:
        comment("Soubor main.py musí být v kódování UTF-8.")
        print("Grade :=>> 0")
        return
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        comment(f"Soubor nejde spustit: {exc.msg} (řádek {exc.lineno}).")
        print("Grade :=>> 0")
        return

    chyby = _zkontroluj_ast(tree)
    if chyby:
        for text in chyby:
            section(False, text)
        comment("Dokud struktura nesedí, výstup se nehodnotí.")
        print("Grade :=>> 0")
        return

    section(True, "Třídy, konstruktory a složení")
    cases = list(DATA.get("cases") or [])
    proslo = 0
    for case in cases:
        name = str(case.get("name") or "test")
        problemy = _ohodnot_pripad(source, case)
        if problemy:
            for text in problemy:
                section(False, f"{name} — {text}")
        else:
            section(True, name)
            proslo += 1
    if not cases:
        print("Grade :=>> 0")
        return
    grade = int(round(100 * proslo / len(cases)))
    print(f"Grade :=>> {grade}")


if __name__ == "__main__":
    main()
