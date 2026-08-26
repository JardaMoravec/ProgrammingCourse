---
id: 16-seznamy
rocnik: 1
nazev: Seznamy (pole) — základy
hodiny: 3
obtiznost: stredni
prerekvizity: [15-funkce-zaklady]
cile:
  - Vytvoříte seznam a přistoupíte k prvkům indexem
  - Projdete seznam cyklem for
  - Použijete základní operace (součet prvků, hledání)
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Seznamy (pole) — základy

## Cíle lekce

- Pochopíte seznam jako **uspořádanou** kolekci prvků
- Ovládnete indexování od 0
- Napíšete program pracující se seznamem čísel

## Co je seznam?

Seznam (`list`) ukládá více hodnot pod jedním názvem. Prvky jsou **uspořádané** a **měnitelné**.

```python
cisla = [10, 20, 30, 40]
jmena = ["Anna", "Petr", "Eva"]
prazdny = []
```

## Indexování

Indexy začínají na **0**:

```python
jmena = ["Anna", "Petr", "Eva"]
print(jmena[0])   # Anna
print(jmena[-1])  # Eva (poslední)
jmena[1] = "Tomáš"
```

| Index | -3 | -2 | -1 |
|-------|----|----|-----|
| Prvek | Anna | Tomáš | Eva |

→ viz `priklady/seznamy.py`

## Délka a procházení

```python
cisla = [3, 1, 4, 1, 5]
print(len(cisla))  # 5

for c in cisla:
    print(c)

for i in range(len(cisla)):
    print(i, cisla[i])
```

## Vytváření a úpravy

```python
a = [1, 2, 3]
a.append(4)       # přidá na konec
a.insert(0, 0)    # vloží na index 0
a.remove(2)       # smaže první výskyt 2
```

## Sečtení prvků

```python
def soucet(seznam):
    s = 0
    for x in seznam:
        s += x
    return s

print(soucet([1, 2, 3, 4]))  # 10
```

## Seznam vs. jedna proměnná

| Jedna proměnná | Seznam |
|----------------|--------|
| jedna hodnota | N hodnot |
| `x = 5` | `x = [1, 2, 3]` |

## Shrnutí

| Operace | Zápis |
|---------|-------|
| vytvoření | `[1, 2, 3]` |
| přístup | `s[i]`, `s[-1]` |
| délka | `len(s)` |
| přidání | `s.append(x)` |

## Co dál

→ [Lekce 17: Metody pro práci se seznamy](../17-metody-seznamu/lekce.md)
