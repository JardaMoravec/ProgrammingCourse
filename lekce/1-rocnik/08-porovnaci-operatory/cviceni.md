# Cvičení — Porovnávací a logické operátory

## Úkol 1 — Pravdivostní hodnoty (★☆☆)

Bez počítače odhadněte, pak ověřte:

```python
(5 > 3) and (2 == 2)
(10 < 5) or (3 > 1)
not (4 == 4)
(7 >= 7) and (7 <= 6)
```

@reseni
```python
print((5 > 3) and (2 == 2))    # True
print((10 < 5) or (3 > 1))       # True
print(not (4 == 4))              # False
print((7 >= 7) and (7 <= 6))     # False
```
@end

---

## Úkol 2 — Interval (★★☆)

Máte proměnnou `x`. Napište **jednu** podmínku (jako výraz), která je True právě když je x mezi 10 a 20 včetně.

@reseni
```python
x = 15
print(10 <= x <= 20)        # True — doporučený zápis
print(x >= 10 and x <= 20)  # True — ekvivalent
```
@end

---

## Úkol 3 — Dělitelnost (★★☆)

Bez `if` (zatím jen výraz): napište podmínku, která zjistí, zda je číslo `n` dělitelné pěti.

@reseni
```python
n = 25
print(n % 5 == 0)  # True
```
@end
