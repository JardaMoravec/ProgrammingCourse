# Cvičení — Cyklus while

## Cvičení 1 — Hádání čísla (★★★)

> Zdroj: `úkol 15 - hádání čísla.docx`

@reseni
→ viz `priklady/hadani_cisla.py`

```python
import random

tajne = random.randint(1, 100)
pokusy = 0

while pokusy < 10:
    pokusy += 1
    try:
        tip = int(input("Hádejte 1–100: "))
    except ValueError:
        print("Zadejte celé číslo.")
        continue
    if tip == tajne:
        print(f"Výhra! Pokusů: {pokusy}")
        break
    print("Větší." if tip < tajne else "Menší.")
else:
    print(f"Prohra. Bylo to {tajne}.")
```
@end

---

## Cvičení 2 — Součet do N (★★☆)

Načtěte N a while cyklem sečtěte 1 + 2 + … + N.

@reseni
```python
n = int(input("Zadejte N: "))
soucet = 0
i = 1
while i <= n:
    soucet += i
    i += 1
print(f"Součet 1..{n} = {soucet}")
```
@end

---

## Cvičení 3 — Menu (★★☆)

Jednoduché menu v `while True`.

@reseni
```python
while True:
    volba = input("Menu [1=pozdrav, 2=součet, k=konec]: ")
    if volba == "1":
        print("Ahoj!")
    elif volba == "2":
        a = float(input("a: "))
        b = float(input("b: "))
        print("Součet:", a + b)
    elif volba == "k":
        break
    else:
        print("Neznámá volba.")
```
@end

---

## Cvičení 4 — Faktoriál (★★★)

Načtěte n ≥ 0. While cyklem vypočítejte n!

@reseni
```python
n = int(input("n: "))
vysledek = 1
i = 2
while i <= n:
    vysledek *= i
    i += 1
print(f"{n}! = {vysledek}")
```
@end
