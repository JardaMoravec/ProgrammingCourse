---
id: 14-ridici-struktury-procviceni
rocnik: 1
nazev: Řídicí struktury — souhrn a procvičení
hodiny: 3
obtiznost: stredni
prerekvizity: [13-cyklus-for]
cile:
  - Zopakujete podmínky, cykly while a for
  - Vyberete správnou řídicí strukturu pro úlohu
  - Složíte větší program z menších bloků
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Řídicí struktury — souhrn a procvičení

## Cíle lekce

- Zopakujete `if` / `elif` / `else`, `while` a `for`
- Naučíte se rozhodnout, **kdy** použít kterou strukturu
- Procvičíte kombinaci vnořených podmínek a cyklů

## Přehled řídicích struktur

| Struktura | Kdy použít |
|-----------|------------|
| `if` / `elif` / `else` | rozhodnutí podle podmínky |
| `while` | opakování, dokud platí podmínka (počet neznámý) |
| `for` | procházení sekvence nebo `range()` (počet známý) |
| `try` / `except` | ošetření chyby za běhu |

## Rozhodovací strom

```
Potřebuji opakovat?
├─ ne → if / elif / else
└─ ano → znám počet kroků?
         ├─ ano → for + range()
         └─ ne → while
```

## Typické vzory

### Menu s opakováním

→ viz `priklady/menu.py`

```python
while True:
    print("1) Součet  2) Konec")
    volba = input("Volba: ")
    if volba == "2":
        break
    elif volba == "1":
        a = float(input("a: "))
        b = float(input("b: "))
        print("Součet:", a + b)
    else:
        print("Neplatná volba.")
```

### Validace vstupu

```python
while True:
    try:
        n = int(input("Zadej kladné celé číslo: "))
        if n > 0:
            break
        print("Musí být kladné.")
    except ValueError:
        print("To není celé číslo.")
```

### Počítání v cyklu

```python
soucet = 0
for i in range(1, 101):
    if i % 2 == 0:
        soucet += i
print("Součet sudých 1–100:", soucet)
```

## Časté chyby

| Chyba | Řešení |
|-------|--------|
| nekonečný `while True` bez `break` | vždy mějte cestu ven |
| `range(10)` místo `range(1, 11)` | pamatujte: konec intervalu **není** součástí |
| zapomenuté odsazení | tělo bloku = 4 mezery |
| `=` místo `==` v podmínce | přiřazení vs. porovnání |

## Shrnutí

Procvičovací lekce — spojujete vše z lekcí 09–13. Před funkcí (lekce 15) byste měli bez problémů napsat program s menu, cyklem a podmínkami.

## Co dál

→ [Lekce 15: Funkce — definice, parametry, návratová hodnota](../15-funkce-zaklady/lekce.md)
