---
id: 10-vnorene-podminky
rocnik: 1
nazev: Vnořené podmínky
hodiny: 3
obtiznost: stredni
prerekvizity: [09-vetveni-podminek]
cile:
  - Použijete vnořené if bloky
  - Zvolíte mezi vnořením a elif
  - Refaktorujete podmínky pro čitelnost
migrovano_z:
  - "zdroje/Programování 1.docx"
---

# Vnořené podmínky

## Cíle lekce

- Umíte psát podmínky uvnitř podmínek
- Víte, kdy vnořit a kdy použít `and` / `elif`
- Udržíte přehlednou strukturu kódu

## Vnořená podmínka

Jedna podmínka uvnitř druhé — druhá se vyhodnotí jen pokud první platí:

```python
vek = int(input("Věk: "))
if vek >= 18:
    if vek < 65:
        print("Jste v produktivním věku.")
    else:
        print("Jste v důchodovém věku.")
else:
    print("Nejste plnoletí.")
```

→ viz `priklady/vnorene.py`

## Vnoření vs. složená podmínka

Často lze vnoření nahradit **`and`**:

```python
# Vnořené
if vek >= 18:
    if vek < 65:
        print("Produktivní věk")

# Ekvivalent — čitelnější
if vek >= 18 and vek < 65:
    print("Produktivní věk")

# Nebo řetězením
if 18 <= vek < 65:
    print("Produktivní věk")
```

**Pravidlo:** preferujte **méně vnoření** — kód je čitelnější.

## Vnoření vs. elif

`elif` řeší **vzájemně se vylučující** větve na stejné úrovni:

```python
if bmi < 18.5:
    print("Podváha")
elif bmi < 25:
    print("Normální váha")
elif bmi < 30:
    print("Nadváha")
else:
    print("Obezita")
```

Vnoření použijte, když **druhá podmínka závisí** na výsledku první.

## Příklad — validace vstupu

```python
cislo = int(input("Zadejte číslo 1–100: "))
if 1 <= cislo <= 100:
    if cislo % 2 == 0:
        print("Sudé číslo v rozsahu.")
    else:
        print("Liché číslo v rozsahu.")
else:
    print("Číslo mimo rozsah!")
```

## Shrnutí

| Situace | Doporučení |
|---------|------------|
| oba testy musí platit | `and` nebo řetězení |
| výlučné větve | `elif` |
| závislá rozhodnutí | vnořené `if` |

## Co dál

→ [Lekce 11: Chyby a výjimky](../11-chyby-a-vyjimky/lekce.md)
