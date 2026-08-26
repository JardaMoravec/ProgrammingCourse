---
id: 04-vstup-a-vystup
rocnik: 1
nazev: Vstup a výstup (input, print)
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [03-bloky-kodu]
cile:
  - Načtete vstup od uživatele pomocí input()
  - Vypíšete výstup pomocí print() a f-stringu
  - Převedete text z input() na číslo pomocí int() a float()
migrovano_z:
  - "zdroje/Programování 1.docx"
---

# Vstup a výstup (input, print)

## Cíle lekce

- Vytvoříte **interaktivní** konzolový program
- Pochopíte, že `input()` vrací vždy text
- Naučíte se formátovat výstup pomocí f-stringu

> Od této lekce **úkoly v Moodle (VPL)** očekávají program se vstupem a výstupem — stejně jako v zadání.

## Výstup — print()

```python
print("Ahoj")                    # jeden text
print("Ahoj", jmeno, "!")        # více hodnot
print(f"Věk: {vek} let")         # f-string (doporučeno)
```

### f-string

```python
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
```

→ viz `priklady/vstup_vystup.py`

## Vstup — input()

`input()` načte řádek od uživatele a vrací **vždy řetězec** (`str`):

```python
jmeno = input("Zadejte své jméno: ")
print("Ahoj", jmeno, "!")
```

Text v uvozovkách u `input()` je **výzva** pro uživatele — v testech VPL se posílá jen samotná data (bez výzev).

## Vstup jako číslo

Pro výpočty musíte text převést na číslo:

```python
vek = int(input("Zadejte věk: "))
print("Za 5 let vám bude", vek + 5)
```

Desetinné číslo: `float(input())`.

Podrobněji o typech a přetypování v [lekci 07](../07-datove-typy/lekce.md).

## Kompletní příklad

```python
a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
print(f"Součet: {a + b}")
```

## Shrnutí

| Funkce | Účel |
|--------|------|
| `input()` | Načtení textu od uživatele |
| `print()` | Výpis na obrazovku |
| `int(...)` | Text → celé číslo |
| `float(...)` | Text → desetinné číslo |
| `f"{x}"` | Formátovaný výstup |

## Co dál

→ [Lekce 05: Aritmetické operátory](../05-aritmeticke-operatory/lekce.md)
