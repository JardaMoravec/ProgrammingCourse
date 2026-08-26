---
id: 09-vetveni-podminek
rocnik: 1
nazev: Větvení programu (if, elif, else)
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [08-porovnaci-operatory]
cile:
  - Použijete if, elif a else
  - Napíšete program s více větvemi
  - Ošetříte základní vstupní podmínky
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/Úkoly 1/úkol 3, 6, 9"
---

# Větvení programu (if, elif, else)

## Cíle lekce

- Ovládnete základní řídicí strukturu podmínky
- Napíšete program reagující na různé situace
- Spojíte vstup, operátory a větvení

## Proč větvení?

Program se v různých situacích chová jinak — podle hodnot proměnných, vstupu uživatele nebo výsledku výpočtu.

```python
if podminka:
    # kód, pokud podmínka platí
else:
    # kód, pokud neplatí
```

## Syntaxe

```python
if podminka:
    prikaz1
    prikaz2
elif jina_podminka:
    prikaz3
else:
    prikaz4
```

- za `if` / `elif` / `else` vždy **dvojtečka**,
- tělo bloku je **odsazené** (4 mezery),
- `elif` a `else` jsou volitelné.

## Příklad — bohatá a šťastná

→ viz `priklady/vetveni.py`

```python
bohata = True
stastna = False

if bohata and stastna:
    print("Gratuluji!")
elif bohata:
    print("Zkus se víc usmívat.")
elif stastna:
    print("Zkus míň utrácet.")
else:
    print("To je mi líto.")
```

## Praktický příklad — výpočet zisku

> Zdroj: `úkol 3 - výpočet zisku.docx`

```python
nakupni = float(input("Nákupní cena (Kč): "))
prodejni = float(input("Prodejní cena (Kč): "))
rozdil = prodejni - nakupni

if rozdil >= 0:
    print(f"Vydělali jste: {rozdil} Kč")
else:
    print(f"Prodělali jste: {abs(rozdil)} Kč")
```

## Vnořené podmínky — náhled

Podmínku lze vnořit do další podmínky — detailně v [lekci 10](../10-vnorene-podminky/lekce.md).

```python
if x > 0:
    if x < 100:
        print("x je mezi 0 a 100")
```

## Shrnutí

| Konstrukce | Kdy |
|------------|-----|
| `if` | první podmínka |
| `elif` | další větev |
| `else` | vše ostatní |

## Co dál

→ [Lekce 10: Vnořené podmínky](../10-vnorene-podminky/lekce.md)
