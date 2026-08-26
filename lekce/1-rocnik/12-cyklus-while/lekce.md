---
id: 12-cyklus-while
rocnik: 1
nazev: Cyklus while
hodiny: 3
obtiznost: stredni
prerekvizity: [11-chyby-a-vyjimky]
cile:
  - Použijete cyklus while s podmínkou
  - Použijete break a else u while
  - Napíšete opakující se logiku (hádání čísla)
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/Úkoly 1/úkol 15 - hádání čísla.docx"
---

# Cyklus while

## Cíle lekce

- Opakujete kód dokud platí podmínka
- Ovládáte `break` pro předčasné ukončení
- Spojíte cyklus s podmínkami a vstupem

## Syntaxe

```python
while podminka:
    telo_cyklu
```

Tělo cyklu se opakuje **dokud podmínka platí**.

## Výpis čísel 1–10

→ viz `priklady/while_cyklus.py`

```python
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    print("Hotovo")
```

## break — ukončení cyklu

```python
while True:
    print(x)
    x += 1
    if x > 10:
        break
else:
    print("Toto se neprovede po break")
```

`break` ukončí cyklus včetně větve `else`.

## Nekonečná smyčka s break

Typický vzor pro menu nebo opakovaný vstup:

```python
while True:
    prikaz = input("Příkaz (konec=k): ")
    if prikaz == "k":
        break
    print("Provádím:", prikaz)
```

## Praktický příklad — hádání čísla

> Zdroj: `úkol 15 - hádání čísla.docx`

```python
import random

tajne = random.randint(1, 100)
pokusy = 0
max_pokusu = 10

while pokusy < max_pokusu:
    pokusy += 1
    try:
        tip = int(input("Hádejte číslo 1–100: "))
    except ValueError:
        print("Zadejte celé číslo.")
        continue

    if tip == tajne:
        print(f"Výhra! Počet pokusů: {pokusy}")
        break
    elif tip < tajne:
        print("Větší.")
    else:
        print("Menší.")
else:
    print(f"Prohra. Číslo bylo {tajne}.")
```

## Kdy while?

| Situace | Příklad |
|---------|---------|
| neznáte počet opakování | hádání, menu |
| čekání na platný vstup | opakovat do správného zadání |
| podmínka na začátku | dokud `x < 100` |

## Shrnutí

| Příkaz | Účel |
|--------|------|
| `while` | opakování za podmínky |
| `break` | okamžité ukončení cyklu |
| `continue` | přeskočí zbytek iterace |
| `else` u while | provede se, pokud cyklus neskončil break |

## Co dál

→ [Lekce 13: Cyklus for a range](../13-cyklus-for/lekce.md)
