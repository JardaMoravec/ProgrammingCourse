---
id: 05-aritmeticke-operatory
rocnik: 1
nazev: Aritmetické operátory a konzole
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [04-promenne-a-pamet]
cile:
  - Použijete aritmetické operátory v Pythonu
  - Rozlišíte dělení, celočíselné dělení a modulo
  - Využijete konzoli jako kalkulačku
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/02 - Proměnné, datové typy a operátory v Pythonu.pptx"
---

# Aritmetické operátory a konzole

## Cíle lekce

- Ovládnete základní matematické operace v Pythonu
- Pochopíte rozdíl mezi `/`, `//` a `%`
- Umíte psát jednoduché výpočty

## Konzole jako kalkulačka

Python konzole zvládne běžné výpočty:

```python
>>> 5 + 3
8
>>> 5 * 3
15
```

## Aritmetické operátory

| Operace | Zápis | Příklad | Výsledek |
|---------|-------|---------|----------|
| Sčítání | `+` | `5 + 3` | `8` |
| Odčítání | `-` | `5 - 3` | `2` |
| Násobení | `*` | `5 * 3` | `15` |
| Dělení | `/` | `5 / 3` | `1.666…` (float) |
| Celočíselné dělení | `//` | `5 // 3` | `1` |
| Umocnění | `**` | `5 ** 3` | `125` |
| Modulo (zbytek) | `%` | `10 % 3` | `1` |

→ viz `priklady/operatory.py`

### Dělení vs. celočíselné dělení

```python
print(7 / 2)    # 3.5  — vždy desetinné číslo (Python 3)
print(7 // 2)   # 3    — celá část
print(7 % 2)    # 1    — zbytek po dělení
```

### Modulo — praktické využití

- zjištění, zda je číslo **sudé** (`n % 2 == 0`),
- cyklické opakování (hodiny, dny),
- kontrola dělitelnosti.

### Pořadí operací

Platí standardní matematická pravidla. Závorky `()` mění pořadí:

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

## Zkrácené operátory přiřazení

Kombinace operace s přiřazením:

| Zápis | Ekvivalent |
|-------|------------|
| `x += 5` | `x = x + 5` |
| `x -= 3` | `x = x - 3` |
| `x *= 2` | `x = x * 2` |
| `x /= 4` | `x = x / 4` |

```python
skore = 100
skore += 10   # bonus
print(skore)  # 110
```

## Shrnutí

| Operátor | Význam |
|----------|--------|
| `/` | Dělení (výsledek float) |
| `//` | Celé dělení |
| `%` | Zbytek |
| `**` | Mocnina |

## Co dál

→ [Lekce 06: Vstup a výstup](../06-vstup-a-vystup/lekce.md)
