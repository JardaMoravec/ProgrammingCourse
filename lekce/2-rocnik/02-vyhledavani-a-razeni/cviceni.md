# Cvičení — Vyhledávání a řazení — základ

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání (věty, vstup z konzole).

## Cvičení 1 — Je v seznamu? (★☆☆)

Funkce `je_v(pole, x)` vrátí `True` / `False`. Napište ji **cyklem**. Nepoužívejte `x in pole`.

Ověření: `je_v([3, 8, 1], 8)` je `True`, `je_v([3, 8, 1], 5)` je `False`.

@reseni
```python
def je_v(pole, x):
    for prvek in pole:
        if prvek == x:
            return True
    return False


print(je_v([3, 8, 1], 8))  # True
print(je_v([3, 8, 1], 5))  # False
```
@end

---

## Cvičení 2 — Index rekurzí (★★☆)

Funkce `index_rek(pole, x, i=0)` vrátí **index od nuly**, nebo `-1`, když prvek chybí. Jen rekurze, ne cyklus.

Ověření: `index_rek([10, 20, 30], 20)` je `1`.

@reseni
```python
def index_rek(pole, x, i=0):
    if i >= len(pole):
        return -1
    if pole[i] == x:
        return i
    return index_rek(pole, x, i + 1)


print(index_rek([10, 20, 30], 20))  # 1
print(index_rek([10, 20, 30], 99))  # -1
```
@end

---

## Cvičení 3 — Počet výskytů cyklem (★★☆)

Funkce `pocet(pole, x)` vrátí, kolikrát se `x` v seznamu vyskytuje. Cyklus, ne `pole.count`.

Ověření: `pocet([2, 5, 2, 2, 7], 2)` je `3`.

@reseni
```python
def pocet(pole, x):
    kolik = 0
    for prvek in pole:
        if prvek == x:
            kolik += 1
    return kolik


print(pocet([2, 5, 2, 2, 7], 2))  # 3
```
@end

---

## Cvičení 4 — Binární hledání (★★☆)

Seznam je **seřazený**. Funkce `binarni(pole, x)` vrátí **pozici od jedné**, nebo `None`. Rekurze: seznam vždy **rozdělte na poloviny** (`pole[:stred]` a `pole[stred + 1:]`).

Ověření: `binarni([1, 4, 9, 16, 25], 16)` je `4`.

@reseni
```python
def binarni(pole, x):
    if not pole:
        return None
    stred = len(pole) // 2  # celočíselné dělení: 5 // 2 je 2, ne 2.5
    if pole[stred] == x:
        return stred + 1
    if pole[stred] > x:
        return binarni(pole[:stred], x)
    nalez = binarni(pole[stred + 1:], x)
    if nalez is None:
        return None
    return stred + 1 + nalez


print(binarni([1, 4, 9, 16, 25], 16))  # 4
print(binarni([1, 4, 9, 16, 25], 10))  # None
```
@end

---

## Cvičení 5 — Bublinkové řazení (★★★)

Funkce `serad(pole)` seřadí seznam vzestupně **bublinkovým řazením**. Nesmíte použít `sort` ani `sorted`. Funkce může měnit seznam na místě a vrátit ho.

Ověření: `serad([5, 1, 4, 2])` je `[1, 2, 4, 5]`.

@reseni
```python
def serad(pole):
    n = len(pole)
    for i in range(n):
        for j in range(n - 1 - i):
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    return pole


print(serad([5, 1, 4, 2]))  # [1, 2, 4, 5]
```
@end
