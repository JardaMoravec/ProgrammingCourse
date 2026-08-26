---
id: 21-kolekce-procviceni
rocnik: 1
nazev: Kolekce — souhrnné procvičení
hodiny: 3
obtiznost: stredni
prerekvizity: [20-cykly-nad-kolekcemi]
cile:
  - Vyberete správnou kolekci pro úlohu
  - Složíte program kombinující seznamy a slovníky
  - Zopakujete metody, cykly a funkce
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Kolekce — souhrnné procvičení

## Cíle lekce

- Procvičíte seznamy, tuple, slovníky a cykly
- Napíšete větší program rozdělený do funkcí
- Zopakujete rozdíly mezi typy kolekcí

## Kdy co použít?

| Potřebuji… | Typ |
|------------|-----|
| seznam hodnot v pořadí | `list` |
| neměnný záznam | `tuple` |
| vyhledání podle jména | `dict` |
| generování čísel | `range` |

## Vzor: evidence studentů

→ viz `priklady/evidence.py`

```python
def prumer_znamek(student):
    znamky = student["znamky"]
    return sum(znamky) / len(znamky)

studenti = [
    {"jmeno": "Anna", "znamky": [1, 2, 1]},
    {"jmeno": "Petr", "znamky": [3, 2, 4]},
]

for s in studenti:
    print(s["jmeno"], prumer_znamek(s))
```

## Tipy na procvičení

1. Rozdělte úlohu na **malé funkce**
2. Data držte ve **slovnících** u pojmenovaných záznamů
3. Seznam použijte pro **více stejných věcí**

## Shrnutí

Souhrnná lekce — cílem je samostatně napsat program s kolekcemi bez nápovědy teorie.

## Co dál

→ [Lekce 22: Moduly, import a knihovna math](../22-moduly-a-import/lekce.md)
