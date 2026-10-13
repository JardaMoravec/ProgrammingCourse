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
REZIM = __REZIM__
MIN_POVINNE = __MIN_POVINNE__
MIN_VOLITELNE = __MIN_VOLITELNE__
PROFIL_VNITRNI = __PROFIL_VNITRNI__
PROFIL_VNEJSI = __PROFIL_VNEJSI__
SLOZENI = __SLOZENI__


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
    chyby.extend(_zkontroluj_parametry(tridy))
    return chyby


def _slovo(pocet: int, jeden: str, dva: str, pet: str) -> str:
    if pocet == 1:
        return jeden
    if 2 <= pocet <= 4:
        return dva
    return pet


def _text_poctu(povinne: int, volitelne: int) -> str:
    return (
        f"{povinne} {_slovo(povinne, 'povinný', 'povinné', 'povinných')} a "
        f"{volitelne} {_slovo(volitelne, 'nepovinný', 'nepovinné', 'nepovinných')}"
    )


def _pocty_trid(tridy: list[ast.ClassDef]) -> list[tuple[str, int, int]]:
    pocty: list[tuple[str, int, int]] = []
    for cls in tridy:
        inity = [method for method in _metody(cls) if method.name == "__init__"]
        if len(inity) != 1:
            continue
        povinne, volitelne = _pocty(inity[0])
        pocty.append((cls.name, povinne, volitelne))
    return pocty


def _sedi_profil(povinne: int, volitelne: int, profil: list[int]) -> bool:
    return povinne >= profil[0] and volitelne >= profil[1]


def _zkontroluj_parametry(tridy: list[ast.ClassDef]) -> list[str]:
    pocty = _pocty_trid(tridy)
    if REZIM == "role":
        if len(pocty) < 2:
            return []
        for i, (_, p1, v1) in enumerate(pocty):
            for j, (_, p2, v2) in enumerate(pocty):
                if i == j:
                    continue
                if _sedi_profil(p1, v1, PROFIL_VNITRNI) and _sedi_profil(
                    p2, v2, PROFIL_VNEJSI
                ):
                    return []
        vypis = ", ".join(
            f"{jmeno} {_text_poctu(povinne, volitelne)}"
            for jmeno, povinne, volitelne in pocty
        )
        return [
            "Vnitřní třída má mít aspoň "
            f"{_text_poctu(PROFIL_VNITRNI[0], PROFIL_VNITRNI[1])}, "
            "vnější aspoň "
            f"{_text_poctu(PROFIL_VNEJSI[0], PROFIL_VNEJSI[1])}. "
            "Nepovinný parametr má v hlavičce výchozí hodnotu. self se nepočítá. "
            f"Teď je: {vypis}."
        ]
    povinne = sum(p for _, p, _ in pocty)
    volitelne = sum(v for _, _, v in pocty)
    if povinne < MIN_POVINNE or volitelne < MIN_VOLITELNE:
        return [
            "Konstruktory obou tříd mají dohromady "
            f"{povinne} povinných a {volitelne} nepovinných parametrů. "
            f"Potřeba je aspoň {MIN_POVINNE} povinné a {MIN_VOLITELNE} nepovinné. "
            "Nepovinný parametr má v hlavičce výchozí hodnotu. self se nepočítá."
        ]
    return []


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


def _je_vnitrni(hodnota: object, tridy: set[type], obj: object) -> bool:
    return type(hodnota) in tridy and type(hodnota) is not type(obj)


def _ulozeno(obj: object, hledane: object, *, povolit_seznam: bool) -> bool:
    for attr in vars(obj):
        ulozene = getattr(obj, attr, None)
        if ulozene is hledane:
            return True
        if povolit_seznam and isinstance(ulozene, (list, tuple)):
            if any(polozka is hledane for polozka in ulozene):
                return True
    return False


def _dvojice(
    zaznamy: list[tuple[object, dict]],
    tridy: set[type],
    *,
    povolit_seznam: bool = False,
) -> list[tuple[object, object]]:
    dvojice: list[tuple[object, object]] = []
    for obj, parametry in zaznamy:
        for hodnota in parametry.values():
            kandidati: list[object] = []
            if _je_vnitrni(hodnota, tridy, obj):
                kandidati.append(hodnota)
            elif povolit_seznam and isinstance(hodnota, (list, tuple)):
                kandidati.extend(
                    polozka
                    for polozka in hodnota
                    if _je_vnitrni(polozka, tridy, obj)
                )
            for kandidat in kandidati:
                if _ulozeno(obj, kandidat, povolit_seznam=povolit_seznam):
                    dvojice.append((obj, kandidat))
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
    dvojice = _dvojice(
        zaznamy, tridy, povolit_seznam=SLOZENI == "dve_v_jedne"
    )
    if SLOZENI == "dve_v_jedne":
        chyby.extend(_zkontroluj_dve_v_jedne(zaznamy, dvojice))
    else:
        vnejsi = {id(obj) for obj, _ in dvojice}
        vnitrni = {id(obj) for _, obj in dvojice}
        if len(vnejsi) < 2 or len(vnitrni) < 2:
            chyby.append(
                "Vytvořte aspoň dvě instance od každé třídy. "
                "Do každé instance vnější třídy vložte přes parametr jiný objekt té druhé."
            )
    chyby.extend(_zkontroluj_orientaci(tree, dvojice))
    return not chyby, chyby


def _zkontroluj_dve_v_jedne(
    zaznamy: list[tuple[object, dict]],
    dvojice: list[tuple[object, object]],
) -> list[str]:
    po_vnejsich: dict[int, tuple[object, list[object]]] = {}
    for vnejsi, vnitrni in dvojice:
        zaznam = po_vnejsich.setdefault(id(vnejsi), (vnejsi, []))
        zaznam[1].append(vnitrni)
    kandidati: list[tuple[object, type]] = []
    for vnejsi, vlozene in po_vnejsich.values():
        podle_typu: dict[type, set[int]] = {}
        for obj in vlozene:
            podle_typu.setdefault(type(obj), set()).add(id(obj))
        for typ, identifikatory in podle_typu.items():
            if len(identifikatory) >= 2:
                kandidati.append((vnejsi, typ))
                break
    if len(kandidati) != 1:
        return [
            "Vytvořte jednu instanci vnější třídy a dvě různé instance té první. "
            "Obě předejte vnější třídě přes parametry a uložte je. "
            "Mohou být ve dvou atributech, nebo v jednom seznamu."
        ]
    vnejsi, _typ = kandidati[0]
    pocet = sum(1 for obj, _parametry in zaznamy if type(obj) is type(vnejsi))
    if pocet != 1:
        return [
            "Vnější třídu vytvořte jen jednou. "
            "Ta jediná instance má držet dvě různé instance té první."
        ]
    return []


def _pocty_jmena(tree: ast.AST, jmeno: str) -> tuple[int, int] | None:
    for cls_name, povinne, volitelne in _pocty_trid(_tridy(tree)):
        if cls_name == jmeno:
            return povinne, volitelne
    return None


def _zkontroluj_orientaci(
    tree: ast.AST, dvojice: list[tuple[object, object]]
) -> list[str]:
    if REZIM != "role":
        return []
    chyby: list[str] = []
    videno: set[tuple[str, str]] = set()
    for vnejsi, vnitrni in dvojice:
        klic = (type(vnejsi).__name__, type(vnitrni).__name__)
        if klic in videno:
            continue
        videno.add(klic)
        pocty_v = _pocty_jmena(tree, klic[0])
        pocty_i = _pocty_jmena(tree, klic[1])
        if pocty_v is None or pocty_i is None:
            continue
        povinne_i, volitelne_i = pocty_i
        povinne_v, volitelne_v = pocty_v
        if not _sedi_profil(povinne_i, volitelne_i, PROFIL_VNITRNI):
            chyby.append(
                f"Vnitřní třída {klic[1]} má {_text_poctu(povinne_i, volitelne_i)}. "
                "Potřeba je aspoň "
                f"{_text_poctu(PROFIL_VNITRNI[0], PROFIL_VNITRNI[1])}."
            )
        if not _sedi_profil(povinne_v, volitelne_v, PROFIL_VNEJSI):
            chyby.append(
                f"Vnější třída {klic[0]} má {_text_poctu(povinne_v, volitelne_v)}. "
                "Potřeba je aspoň "
                f"{_text_poctu(PROFIL_VNEJSI[0], PROFIL_VNEJSI[1])}."
            )
    return chyby


def _uspech() -> str:
    if REZIM == "role":
        return (
            "Dvě třídy, vnitřní "
            f"{_text_poctu(PROFIL_VNITRNI[0], PROFIL_VNITRNI[1])}, vnější "
            f"{_text_poctu(PROFIL_VNEJSI[0], PROFIL_VNEJSI[1])}, "
            "vložení, dvě instance"
        )
    if SLOZENI == "dve_v_jedne":
        return (
            "Dvě třídy, "
            f"{MIN_POVINNE} povinné a {MIN_VOLITELNE} nepovinné parametry, "
            "jedna vnější instance se dvěma vnitřními"
        )
    return (
        "Dvě třídy, "
        f"{MIN_POVINNE} povinné a {MIN_VOLITELNE} nepovinné parametry, "
        "vložení, dvě instance"
    )


def main() -> None:
    student = Path(STUDENT_FILE)
    if not student.is_file():
        comment(f"Chybí soubor {STUDENT_FILE}.")
        print("Grade :=>> 0")
        return
    ok, chyby = _ohodnot(student.read_text(encoding="utf-8"))
    if ok:
        section(True, _uspech())
        print("Grade :=>> 100")
        return
    for text in chyby:
        section(False, text)
    print("Grade :=>> 0")


if __name__ == "__main__":
    main()
