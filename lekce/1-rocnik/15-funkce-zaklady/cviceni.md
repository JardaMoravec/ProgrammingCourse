# Cvičení — Funkce (základy)

## Cvičení 1 — Obsah a obvod (★★☆)

Napište funkce `obsah(a, b)` a `obvod(a, b)` pro obdélník.

@reseni
```python
def obsah(a, b):
    return a * b

def obvod(a, b):
    return 2 * (a + b)

print(obsah(5, 3), obvod(5, 3))  # 15 16
```
@end

---

## Cvičení 2 — Maximum ze tří (★★☆)

Funkce `maximum(a, b, c)` vrátí největší ze tří čísel (bez vestavěého max).

@reseni
```python
def maximum(a, b, c):
    nejvetsi = a
    if b > nejvetsi:
        nejvetsi = b
    if c > nejvetsi:
        nejvetsi = c
    return nejvetsi
```
@end

---

## Cvičení 3 — Faktoriál (★★★)

Funkce `faktorial(n)` pro n ≥ 0.

@reseni
```python
def faktorial(n):
    vysledek = 1
    for i in range(2, n + 1):
        vysledek *= i
    return vysledek
```
@end

---

## Cvičení 4 — Je prvočíslo? (★★★)

Funkce vrátí True/False; v hlavním programu načtěte číslo a vypište výsledek.

@reseni
```python
def je_prvocislo(n):
    if n <= 1:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

n = int(input("Číslo: "))
print("Prvočíslo" if je_prvocislo(n) else "Není prvočíslo")
```
@end
