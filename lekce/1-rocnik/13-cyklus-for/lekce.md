---
id: 13-cyklus-for
rocnik: 1
nazev: Cyklus for a funkce range
hodiny: 3
obtiznost: stredni
prerekvizity: [12-cyklus-while]
cile:
  - Použijete for s funkcí range()
  - Pochopíte intervaly range(start, stop, step)
  - Sečtete sudá a lichá čísla v intervalu
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/Úkoly 1/úkol 16 - sudá a lichá čísla.docx"
---

# Cyklus for a funkce range

## Cíle lekce

- Použijete `for` pro opakování s known počtem kroků
- Ovládnete `range()` pro generování číselných řad
- Připravíte se na práci se seznamy (lekce 16+)

## Cyklus for

```python
for prvek in sekvence:
    telo
```

`for` projde **každý prvek** sekvence. Zatím použijeme hlavně `range()`.

## Funkce range()

`range(n)` generuje čísla **0, 1, …, n-1** (konec **není** součástí):

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4
```

### Formy range

| Zápis | Význam |
|-------|--------|
| `range(5)` | 0 až 4 |
| `range(3, 7)` | 3, 4, 5, 6 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |

→ viz `priklady/for_range.py`

```python
for x in range(0, 10, 2):
    print(x)   # sudá čísla 0–8
```

## for vs. while

| for | while |
|-----|-------|
| známý počet opakování | podmínka |
| `for i in range(10)` | `while i < 10` |
| přehlednější pro indexy | vhodné pro nejistý konec |

## Součet sudých a lichých

> Adaptace `úkol 16` — bez seznamu, jen `range`:

```python
suda = 0
licha = 0

for n in range(1, 31):
    if n % 2 == 0:
        suda += n
    else:
        licha += n

print("Součet sudých:", suda)
print("Součet lichých:", licha)
```

Procházení **seznamů a slovníků** přidáme v lekcích 16–20.

## Vnořené cykly for

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
```

## break a continue

Fungují stejně jako u `while`:

```python
for i in range(100):
    if i == 5:
        break
    print(i)
```

## Shrnutí

| Konstrukce | Účel |
|------------|------|
| `for x in range(n)` | n opakování |
| `range(a, b)` | od a do b-1 |
| `range(a, b, k)` | krokování |

## Co dál

→ [Lekce 14: Řídicí struktury — procvičení](../14-ridici-struktury-procviceni/lekce.md)

→ [Lekce 15: Funkce — definice, parametry, návratová hodnota](../15-funkce-zaklady/lekce.md)
