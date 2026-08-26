# Cvičení — Řídicí struktury (souhrn)

## Úkol 1 — Kalkulačka s menu (★★☆)

Napište program s menu: součet, rozdíl, součin, konec. Opakujte, dokud uživatel nezvolí konec.

@reseni
→ viz `priklady/menu.py`
@end

---

## Úkol 2 — FizzBuzz (★★☆)

Pro čísla 1–100 vypište `Fizz` (dělitelné 3), `Buzz` (dělitelné 5), `FizzBuzz` (obojí) nebo samotné číslo.

@reseni
```python
for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```
@end

---

## Úkol 3 — Prvočíslo (★★★)

Načtěte n a rozhodněte, zda je prvočíslo (n > 1, dělitelné jen 1 a sebou).

@reseni
```python
n = int(input("Číslo: "))
if n <= 1:
    print("Ne")
else:
    je_prvocislo = True
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            je_prvocislo = False
            break
    print("Ano" if je_prvocislo else "Ne")
```
@end

---

## Úkol 4 — Tabulka násobků (★★☆)

Vypište matici 10×10 násobků (vnořené cykly for).

@reseni
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
```
@end
