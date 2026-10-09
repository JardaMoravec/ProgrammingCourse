# Používá generate_tasks.py — placeholdery nahradí generátor.
"""Hodnotitel známkovaného úkolu: dvě třídy, složení přes parametr __init__."""

from __future__ import annotations

import ast
import io
import traceback
from contextlib import redirect_stdout
from pathlib import Path

STUDENT_FILE = "__STUDENT_FILE__"
ZAKAZANE = __ZAKAZANE__


def comment(text: str) -> None:
    print(f"Comment :=>> {text}")


def section(ok: bool, name: str) -> None:
    znacka = "OK" if ok else "CHYBA"
    print(f"Comment :=>>-{znacka}: {name}")


def _klic(name: str) -> str:
    return "".join(ch for ch in name.lower() if ch.isalnum())


def _tridy(tree: ast.AST) -> list[ast.ClassDef]:
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def _metody(cls: ast.ClassDef) -> list[ast.FunctionDef]:
    return [node for node in cls.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]


def _parametry(init: ast.FunctionDef) -> list[str]:
    names = [arg.arg for arg in init.args.args]
    names += [arg.arg for arg in init.args.kwonlyargs]
    return [name for name in names if name != "self"]


def _instrumentuj(tree: ast.AST) -> None:
    for cls in _tridy(tree):
        for method in _metody(cls):
            if method.name != "__init__":
                continue
            names = _parametry(method)
            call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="_sleduj", ctx=ast.Load()),
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
            method.body.insert(0, call)
    ast.fix_missing_locations(tree)


def _zkontroluj_ast(tree: ast.AST) -> list[str]:
    chyby: list[str] = []
    tridy = _tridy(tree)
    if len(tridy) < 2:
        chyby.append("V souboru musí být aspoň dvě třídy.")
        return chyby
    for cls in tridy:
        if _klic(cls.name) in ZAKAZANE:
            chyby.append(
                f"Třída {cls.name} je z úkolů této lekce. Zvolte jiné téma."
            )
        metody = _metody(cls)
        inity = [method for method in metody if method.name == "__init__"]
        if len(inity) != 1:
            chyby.append(f"Třída {cls.name} musí mít právě jeden __init__.")
            continue
        if any(method.name != "__init__" for method in metody):
            chyby.append(
                f"Třída {cls.name} smí mít jen __init__, žádnou další metodu."
            )
        args = [arg.arg for arg in inity[0].args.args]
        if not args or args[0] != "self":
            chyby.append(f"__init__ třídy {cls.name} musí začínat parametrem self.")
    povinne, volitelne = _soucet_parametru(tridy)
    if povinne < 4 or volitelne < 4:
        chyby.append(
            "Konstruktory obou tříd mají dohromady "
            f"{povinne} povinných a {volitelne} nepovinných parametrů. "
            "Potřeba je aspoň 4 povinné a 4 nepovinné. "
            "Nepovinný parametr má v hlavičce výchozí hodnotu. self se nepočítá."
        )
    return chyby


def _pocty(init: ast.FunctionDef) -> tuple[int, int]:
    args = init.args
    n_pos = len(args.args)
    n_def = len(args.defaults)
    n_required_pos = n_pos - n_def
    self_required = bool(args.args) and args.args[0].arg == "self" and n_required_pos > 0
    povinne = n_required_pos - (1 if self_required else 0)
    volitelne = n_def
    for default in args.kw_defaults:
        if default is None:
            povinne += 1
        else:
            volitelne += 1
    return povinne, volitelne


def _soucet_parametru(tridy: list[ast.ClassDef]) -> tuple[int, int]:
    povinne = 0
    volitelne = 0
    for cls in tridy:
        inity = [method for method in _metody(cls) if method.name == "__init__"]
        if len(inity) != 1:
            continue
        p, v = _pocty(inity[0])
        povinne += p
        volitelne += v
    return povinne, volitelne


def _dvojice(zaznamy: list[tuple[object, dict]], tridy: set[type]) -> list[tuple[object, object]]:
    dvojice: list[tuple[object, object]] = []
    for obj, parametry in zaznamy:
        for hodnota in parametry.values():
            if type(hodnota) not in tridy or type(hodnota) is type(obj):
                continue
            if any(getattr(obj, attr, None) is hodnota for attr in vars(obj)):
                dvojice.append((obj, hodnota))
    return dvojice


def _ohodnot(source: str) -> tuple[bool, list[str]]:
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return False, [f"Soubor nejde spustit: {exc.msg} (řádek {exc.lineno})."]

    chyby = _zkontroluj_ast(tree)
    if chyby:
        return False, chyby

    zaznamy: list[tuple[object, dict]] = []

    def _sleduj(self, parametry: dict) -> None:
        zaznamy.append((self, dict(parametry)))

    _instrumentuj(tree)
    namespace = {"__name__": "student", "_sleduj": _sleduj}
    try:
        with redirect_stdout(io.StringIO()):
            exec(compile(tree, STUDENT_FILE, "exec"), namespace, namespace)
    except Exception as exc:
        last = traceback.format_exception_only(type(exc), exc)[-1].strip()
        return False, [f"Program spadl při spuštění: {last}"]

    tridy = {
        value
        for value in namespace.values()
        if isinstance(value, type) and getattr(value, "__module__", "") == "student"
    }
    dvojice = _dvojice(zaznamy, tridy)
    vnejsi = {id(obj) for obj, _ in dvojice}
    vnitrni = {id(obj) for _, obj in dvojice}
    if len(vnejsi) < 2 or len(vnitrni) < 2:
        chyby.append(
            "Vytvořte aspoň dvě instance od každé třídy. "
            "Do každé instance vnější třídy vložte přes parametr jiný objekt té druhé."
        )
    return not chyby, chyby


def main() -> None:
    student = Path(STUDENT_FILE)
    if not student.is_file():
        comment(f"Chybí soubor {STUDENT_FILE}.")
        print("Grade :=>> 0")
        return
    ok, chyby = _ohodnot(student.read_text(encoding="utf-8"))
    if ok:
        section(True, "Dvě třídy, 4 povinné a 4 nepovinné parametry, vložení, dvě instance")
        print("Grade :=>> 100")
        return
    for text in chyby:
        section(False, text)
    print("Grade :=>> 0")


if __name__ == "__main__":
    main()
