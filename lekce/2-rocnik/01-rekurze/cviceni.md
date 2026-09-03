# Cvičení — Rekurze — základ

Ve cvičeních řešte **rekurzí**. Cyklus `for` / `while` nepoužívejte (kromě výpisu hotového výsledku).

## Cvičení 1 — Součet 1 až n (★☆☆)

Napište funkci `soucet_do(n)`, která vrátí `1 + 2 + … + n`. Pro `n <= 0` vraťte `0`.

Ověření: `soucet_do(4)` je `10`.

@reseni
```python
def soucet_do(n):
    if n <= 0:
        return 0
    return n + soucet_do(n - 1)


print(soucet_do(4))  # 10
```
@end

---

## Cvičení 2 — Počet číslic (★★☆)

Funkce `pocet_cislic(n)` vrátí, kolik číslic má nezáporné celé číslo `n`. Nulu berte jako jednu číslici.

Ověření: `pocet_cislic(502)` je `3`, `pocet_cislic(0)` je `1`.

@reseni
```python
def pocet_cislic(n):
    if n < 10:
        return 1
    return 1 + pocet_cislic(n // 10)


print(pocet_cislic(502))  # 3
print(pocet_cislic(0))    # 1
```
@end

---

## Cvičení 3 — Součin seznamu (★★☆)

Funkce `soucin(polozky, index=0)` vrátí součin všech čísel v seznamu. Prázdný seznam: `1` (neutrální prvek násobení).

Ověření: `soucin([2, 3, 4])` je `24`.

@reseni
```python
def soucin(polozky, index=0):
    if index >= len(polozky):
        return 1
    return polozky[index] * soucin(polozky, index + 1)


print(soucin([2, 3, 4]))  # 24
print(soucin([]))         # 1
```
@end

---

## Cvičení 4 — Obrácený řetězec (★★☆)

Funkce `obrat(text)` vrátí řetězec pozpátku. Nepoužívejte `text[::-1]` ani cyklus.

Ověření: `obrat("ahoj")` je `"joha"`.

@reseni
```python
def obrat(text):
    if text == "":
        return ""
    return obrat(text[1:]) + text[0]


print(obrat("ahoj"))  # joha
```
@end

---

## Cvičení 5 — Fibonacci (★★★)

Funkce `fib(n)` vrátí n-tý člen posloupnosti: `fib(0) = 0`, `fib(1) = 1`, dále součet dvou předchozích.

Zkuste jen **malá** `n` (do 10). Tahle naivní rekurze volá sama sebe dvakrát — u velkého `n` by běžela dlouho. To teď řešit nemusíte.

Ověření: `fib(6)` je `8`.

@reseni
```python
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(6))  # 8
```
@end
