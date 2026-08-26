---
id: 17-metody-seznamu
rocnik: 1
nazev: Metody pro práci se seznamy
hodiny: 3
obtiznost: stredni
prerekvizity: [16-seznamy]
cile:
  - Použijete sort, reverse, count, index, pop
  - Rozdělíte a spojíte seznamy
  - Vyberete vhodnou metodu pro úlohu
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Metody pro práci se seznamy

## Cíle lekce

- Ovládnete běžné **metody** seznamu
- Seřadíte data a budete hledat prvky
- Spojíte více seznamů do jednoho

## Metody měnící seznam

→ viz `priklady/metody_seznamu.py`

```python
a = [3, 1, 4, 1, 5]
a.sort()           # [1, 1, 3, 4, 5] — setřídí na místě
a.reverse()        # obrátí pořadí
a.pop()            # odebere a vrátí poslední prvek
a.pop(0)           # odebere prvek na indexu 0
```

## Metody vracející informaci

```python
a = [1, 2, 3, 2, 4]
print(a.count(2))   # 2 — kolikrát je 2 v seznamu
print(a.index(3))   # 2 — index prvního výskytu 3
print(5 in a)       # False — membership test
```

## Spojování a dělení

```python
a = [1, 2]
b = [3, 4]
c = a + b           # [1, 2, 3, 4] — nový seznam
a.extend(b)         # přidá prvky b do a
a * 3               # [1, 2, 1, 2, 1, 2] — opakování
```

## Řez seznamu (slice)

```python
a = [0, 1, 2, 3, 4, 5]
print(a[1:4])    # [1, 2, 3]
print(a[:3])     # [0, 1, 2]
print(a[2:])     # [2, 3, 4, 5]
print(a[::2])    # každý druhý prvek
```

## Kopie vs. reference

```python
a = [1, 2, 3]
b = a              # stejný seznam!
b.append(4)        # změní i a

c = a.copy()       # nezávislá kopie
c.append(5)        # a zůstane [1, 2, 3, 4]
```

## Shrnutí

| Metoda | Účel |
|--------|------|
| `sort()` | setřídí |
| `append(x)` | přidá na konec |
| `pop()` | odebere poslední |
| `count(x)` | počet výskytů |
| `s[a:b]` | výřez |

## Co dál

→ [Lekce 18: Tuples a range](../18-tuples-a-range/lekce.md)
