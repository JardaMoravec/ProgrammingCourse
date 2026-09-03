---
id: 02-vyhledavani-a-razeni
rocnik: 2
nazev: Vyhledávání a řazení — základ
hodiny: 10
obtiznost: stredni
prerekvizity: [01-rekurze]
cile:
  - Najdete prvek lineárním hledáním (cyklus i rekurze)
  - Najdete prvek binárním hledáním v seřazeném seznamu
  - Seřadíte seznam vlastním algoritmem (bez sort)
migrovano_z:
  - "zdroje/Programování 2.docx (kap. Vyhledávací algoritmy)"
  - "zdroje/Programování 2 – Python manuál.docx"
---

# Vyhledávání a řazení — základ

Lekce má **10 hodin** (dva týdny). Navazuje na [rekurzi](../01-rekurze/lekce.md). Bez složitosti algoritmů — jen postup, který umíte napsat.

V 1. ročníku jste v seznamu hledali cyklem a řadili jste `sort()`. Tady uvidíte, **jak** hledání a řazení funguje uvnitř. Vestavěné `sort()` / `sorted()` v úkolech **nejsou** povolené.

## Cíle lekce

- Projdete seznam **lineárně** (od začátku) cyklem i rekurzí
- Použijete **binární hledání**, když je seznam **seřazený**
- Napíšete **bublinkové řazení** — bez `sort()` a `sorted()`

## Kdy který postup

| Potřebujete | Použijte |
|-------------|----------|
| najít prvek, seznam **není** seřazený | lineární hledání |
| najít prvek, seznam **je** seřazený | binární hledání |
| seznam seřadit vlastním kódem | bublinkové řazení (nebo jiný vlastní algoritmus) |

## Lineární hledání

Jdete prvek po prvku, dokud nenajdete hledané číslo, nebo seznam neskončí.

```python
def linearni(pole, x):
    for i in range(len(pole)):
        if pole[i] == x:
            return i + 1
    return None


pole = [4, 8, 10, 45]
print(linearni(pole, 10))  # 3
print(linearni(pole, 7))   # None
```

Pozice v této lekci počítáme **od jedné** (první prvek je 1), stejně jako v úkolech.

![Lineární hledání: kontrola zleva doprava](diagramy/linearni-hledani.svg)

Tohle umíte z 1. ročníku jako cyklus. Teď totéž **rekurzí** — index je další parametr:

```python
def linearni_rek(pole, x, i=0):
    if i >= len(pole):
        return None
    if pole[i] == x:
        return i + 1
    return linearni_rek(pole, x, i + 1)
```

Bazický případ: index je za koncem → prvek tam **není**.

→ viz `priklady/linearni_hledani.py`

## Binární hledání

Funguje jen nad **seřazeným** seznamem (od nejmenšího). Myšlenka: podíváte se **doprostřed**.

- je to hledané číslo? hotovo
- střed je **větší** → hledejte jen v **levé** polovině
- střed je **menší** → hledejte jen v **pravé** polovině

Na osmi číslech stačí pár porovnání místo až osmi.

```python
def binarni(pole, x, levy=0, pravy=None):
    if pravy is None:
        pravy = len(pole) - 1
    if levy > pravy:
        return None
    stred = (levy + pravy) // 2
    if pole[stred] == x:
        return stred + 1
    if pole[stred] > x:
        return binarni(pole, x, levy, stred - 1)
    return binarni(pole, x, stred + 1, pravy)


pole = [4, 8, 10, 45, 48, 49, 51, 100]
print(binarni(pole, 45))  # 4
print(binarni(pole, 7))   # None
```

`levy` a `pravy` jsou indexy úseku, ve kterém ještě má smysl hledat. Až `levy > pravy`, úsek je prázdný.

Hledání 45 v `[4, 8, 10, 45, 48, 49, 51, 100]`:

1. střed je 48 — větší než 45 → berete **levou** polovinu
2. střed je 10 — menší než 45 → berete **pravou** polovinu
3. zbývá 45 — **shoda**, pozice 4

![Binární hledání čísla 45](diagramy/binarni-hledani.svg)

→ viz `priklady/binarni_hledani.py`

Když seznam **není** seřazený, binární hledání může říct „není“, i když číslo v seznamu je. Nejdřív seřadit, nebo použít lineární hledání.

## Bublinkové řazení

Chcete seznam od nejmenšího po největší **vlastním** algoritmem. Vestavěné `seznam.sort()` a `sorted()` v úkolech **nejsou** povolené.

**Bublinkové řazení:** jdete sousední dvojice. Když je levé číslo větší, **prohodíte** je. Větší hodnoty „probublají“ doprava. Celý průchod opakujete, dokud je co prohazovat.

```python
def bublinkove(pole):
    n = len(pole)
    for i in range(n):
        for j in range(n - 1 - i):
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    return pole


print(bublinkove([4, 1, 3, 2]))  # [1, 2, 3, 4]
```

První průchod `[4, 1, 3, 2]`:

1. 4 a 1 → prohodit → `[1, 4, 3, 2]`
2. 4 a 3 → prohodit → `[1, 3, 4, 2]`
3. 4 a 2 → prohodit → `[1, 3, 2, 4]`

Největší číslo je vpravo. Další průchody seřadí zbytek.

![Jeden průchod bublinkového řazení](diagramy/bublinkove-razeni.svg)

`n - 1 - i`: po každém průchodu je na konci o jedno správně umístěné číslo víc, takže příště stačí kratší úsek.

Prohození bez třetí proměnné:

```python
a, b = b, a
```

→ viz `priklady/bublinkove_razeni.py`

Jiný řadící algoritmus (třeba výběrem minima) je taky v pořádku — v známkovaném úkolu stačí **libovolný vlastní**.

## Načtení seznamu z konzole

Úkoly čtou **jeden řádek čísel** a často ještě druhé číslo. `input()` bez textu:

```python
pole = [int(x) for x in input().split()]
x = int(input())
```

`split()` rozdělí řádek podle mezer. `int` každé slovo změní na číslo.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| binární hledání na neseřazeném seznamu | špatná odpověď |
| pozice od nuly, úkol chce od jedné | o jednu vedle |
| `return binarni(...)` zapomenete | funkce vrátí `None` i při nálezu |
| `pole.sort()` v úkolu | nedostatečná |

## Shrnutí

| Pojem | Podmínka | Postup |
|-------|----------|--------|
| lineární hledání | žádná | prvek po prvku |
| binární hledání | seznam je seřazený | půlení úseku |
| bublinkové řazení | — | prohazovat sousedy |

Automatický test v AMOS kontroluje **výstup**. Učitel může zkontrolovat, že v kódu opravdu je rekurze, binární půlení, nebo vlastní řazení (ne `sort`).

## Co dál

Další lekce: **Třídy, objekty a atributy** — začátek objektového programování.
