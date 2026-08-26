---
id: 11-chyby-a-vyjimky
rocnik: 1
nazev: Chyby a výjimky (try, except)
hodiny: 3
obtiznost: stredni
prerekvizity: [10-vnorene-podminky]
cile:
  - Rozlišíte syntaktickou chybu a výjimku za běhu
  - Odchytíte výjimku pomocí try/except
  - Ošetříte neplatný vstup od uživatele
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/Úkoly 1/úkol 12 - procvičení výjimek.docx"
---

# Chyby a výjimky (try, except)

## Cíle lekce

- Pochopíte, proč program „spadne“
- Naučíte se odchytávat předvídatelné chyby
- Napišete robustnější vstupní formulář

## Typy problémů

| Typ | Kdy se projeví | Příklad |
|-----|----------------|---------|
| **SyntaxError** | před spuštěním | chybějící dvojtečka |
| **Výjimka (Exception)** | za běhu | `int("abc")` |

V interpretovaném Pythonu se mnoho chyb projeví **až při spuštění** na konkrétním řádku.

## try / except

```python
try:
    x = int(input("Zadejte číslo: "))
    print("Zadali jste:", x)
except ValueError:
    print("To není platné celé číslo!")
```

- `try` — kód, který může selhat,
- `except` — co udělat při konkrétní chybě.

## Více typů výjimek

```python
while True:
    try:
        x = int(input("Číslo: "))
        y = 10 / x
        break
    except ValueError:
        print("Zadejte celé číslo.")
    except ZeroDivisionError:
        print("Nulou dělit nelze.")
```

## as — detail výjimky

```python
try:
    x = int(input("Číslo: "))
except ValueError as e:
    print("Chyba:", e)
```

## raise — vyvolání výjimky

```python
try:
    raise NameError("Test")
except NameError:
    print("Výjimka odchycena.")
```

Vlastní validace bez knihovny:

```python
text = input("Muž nebo žena? ")
if text not in ("muž", "žena"):
    raise ValueError("Povoleny jsou pouze hodnoty muž nebo žena.")
```

→ viz `priklady/vyjimky.py`

## Běžné výjimky

| Výjimka | Příčina |
|---------|---------|
| `ValueError` | neplatná hodnota (`int("a")`) |
| `ZeroDivisionError` | dělení nulou |
| `TypeError` | špatný typ operace |
| `IndexError` | neplatný index seznamu |

Kompletní seznam: [docs.python.org — Exceptions](https://docs.python.org/3/library/exceptions.html)

## Shrnutí

| Konstrukce | Účel |
|------------|------|
| `try` | rizikový kód |
| `except` | reakce na chybu |
| `raise` | vyvolání výjimky |

## Co dál

→ [Lekce 12: Cyklus while](../12-cyklus-while/lekce.md)
