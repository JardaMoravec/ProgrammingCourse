# Cvičení — Chyby a výjimky

## Cvičení 1 — Procvičení výjimek (★★★)

> Zdroj: `úkol 12 - procvičení výjimek.docx`

Postupně ověřte vstup uživatele s konkrétní chybovou hláškou. Každý program má **jeden pokus** — při chybě vypište hlášku a skončete. Cyklus `while` ještě nepoužívejte.

1. celé číslo v rozsahu −100 až 100
2. desetinné číslo (`float`)
3. sudé číslo (`x % 2 != 0` je chyba)
4. dělení `10 / x` (`ZeroDivisionError`)

@reseni
Celé číslo v intervalu:

```python
try:
    x = int(input("Celé číslo od -100 do 100: "))
    if not -100 <= x <= 100:
        raise ValueError("mimo interval")
    print(f"Číslo je {x}.")
except ValueError:
    print("Chyba: zadejte celé číslo v rozsahu -100 až 100.")
```

Desetinné číslo:

```python
try:
    x = float(input("Desetinné číslo: "))
    print(f"Číslo je {x}.")
except ValueError:
    print("Chyba: zadejte desetinné číslo.")
```

Sudé číslo:

```python
try:
    x = int(input("Sudé číslo: "))
    if x % 2 != 0:
        raise ValueError("liché")
    print(f"Číslo {x} je sudé.")
except ValueError:
    print("Chyba: zadejte sudé celé číslo.")
```

Dělení:

```python
try:
    x = int(input("Dělitel: "))
    print(f"10 / {x} = {10 / x}")
except ValueError:
    print("Chyba: zadejte celé číslo.")
except ZeroDivisionError:
    print("Chyba: nulou dělit nelze.")
```
@end

---

## Cvičení 2 — Bezpečný input (★★☆)

Načtěte **jedno** kladné celé číslo. Při chybě (text, nula, záporné) vypište `Neplatný vstup.` a skončete.

Po úspěchu: `Děkuji, zadali jste: X`

@reseni
```python
try:
    n = int(input("Zadejte kladné celé číslo: "))
    if n <= 0:
        raise ValueError("není kladné")
    print("Děkuji, zadali jste:", n)
except ValueError:
    print("Neplatný vstup.")
```
@end

---

## Cvičení 3 — Co spadne? (★★☆)

Predikujte výjimku, pak ověřte.

@reseni
| Kód | Výjimka |
|-----|---------|
| `int("12.5")` | `ValueError` |
| `10 / 0` | `ZeroDivisionError` |
| `"text" + 5` | `TypeError` |
@end
