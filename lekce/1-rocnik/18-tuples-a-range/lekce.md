---
id: 18-tuples-a-range
rocnik: 1
nazev: Tuples a range
hodiny: 3
obtiznost: stredni
prerekvizity: [17-metody-seznamu]
cile:
  - Rozlišíte tuple a seznam
  - Použijete tuple pro souřadnice a vracení více hodnot
  - Zopakujete range a převod na seznam
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Tuples a range

## Cíle lekce

- Pochopíte **tuple** jako neměnnou sekvenci
- Vrátíte z funkce více hodnot najednou
- Zopakujete `range()` a jeho vztah ke kolekcím

## Tuple (ntice)

Tuple vypadá jako seznam, ale **nelze měnit** po vytvoření:

```python
bod = (10, 20)
barva = (255, 128, 0)
jednoprvkove = (42,)   # čárka nutná!

print(bod[0], bod[1])
# bod[0] = 5   # TypeError!
```

→ viz `priklady/tuples.py`

## Tuple vs. seznam

| | Seznam | Tuple |
|---|--------|-------|
| Zápis | `[1, 2]` | `(1, 2)` |
| Změna | ano | ne |
| Použití | dynamická data | pevné záznamy |

## Více návratových hodnot

```python
def min_max(cisla):
    return min(cisla), max(cisla)

nejnizsi, nejvyssi = min_max([3, 1, 4, 1, 5])
```

## Range znovu

`range` není seznam — je to **iterátor**. Převod:

```python
r = range(5)
print(list(r))        # [0, 1, 2, 3, 4]
print(tuple(r))       # (0, 1, 2, 3, 4)
```

## Enumerate a zip

```python
jmena = ["Anna", "Petr"]
for i, jmeno in enumerate(jmena):
    print(i, jmeno)

a = [1, 2, 3]
b = ["x", "y", "z"]
for x, y in zip(a, b):
    print(x, y)
```

## Shrnutí

| Typ | Měnitelný | Příklad |
|-----|-----------|---------|
| list | ano | `[1, 2]` |
| tuple | ne | `(1, 2)` |
| range | — | `range(10)` |

## Co dál

→ [Lekce 19: Slovníky](../19-slovniky/lekce.md)
