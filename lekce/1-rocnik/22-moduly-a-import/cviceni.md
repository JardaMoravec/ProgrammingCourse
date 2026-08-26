# Cvičení — Moduly a import

## Úkol 1 — Hypoténa (★★☆)

Délky odvěsen a, b — hypoténa pomocí math.sqrt.

@reseni
```python
import math

a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt(a**2 + b**2)
print(f"Hypoténa: {c:.2f}")
```
@end

---

## Úkol 2 — Kruh (★★☆)

Poloměr r — obvod a obsah (math.pi).

@reseni
```python
import math

r = float(input("r: "))
print("Obvod:", 2 * math.pi * r)
print("Obsah:", math.pi * r ** 2)
```
@end

---

## Úkol 3 — Vlastní modul (★★★)

V souboru `geo.py` funkce obsah_kruhu(r); v hlavním souboru import a volání.

@reseni
```python
# geo.py
import math

def obsah_kruhu(r):
    return math.pi * r ** 2

# main.py
import geo
print(geo.obsah_kruhu(5))
```
@end

---

## Úkol 4 — Náhodné číslo (★★☆)

Modul random — 5 náhodných celých 1–6 (kostka).

@reseni
```python
import random

for _ in range(5):
    print(random.randint(1, 6))
```
@end
