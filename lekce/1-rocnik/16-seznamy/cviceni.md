# Cvičení — Seznamy (základy)

## Cvičení 1 — První a poslední (★☆☆)

Vytvořte seznam 5 jmen a vypište první, poslední a prostřední prvek.

@reseni
```python
jmena = ["Anna", "Petr", "Eva", "Tom", "Lucie"]
print(jmena[0], jmena[-1], jmena[len(jmena) // 2])
```
@end

---

## Cvičení 2 — Součet seznamu (★★☆)

Načtěte N čísel do seznamu a vypište součet a průměr.

@reseni
```python
n = int(input("Kolik čísel: "))
cisla = []
for _ in range(n):
    cisla.append(float(input("Číslo: ")))
if cisla:
    print("Součet:", sum(cisla), "Průměr:", sum(cisla) / len(cisla))
```
@end

---

## Cvičení 3 — Maximum v seznamu (★★☆)

Bez vestavěné funkce `max()` najděte největší prvek.

@reseni
```python
cisla = [3, 7, 2, 9, 4]
nejvetsi = cisla[0]
for x in cisla:
    if x > nejvetsi:
        nejvetsi = x
print(nejvetsi)
```
@end

---

## Cvičení 4 — Sudá čísla (★★☆)

Z seznamu `[1..20]` vytvořte nový seznam jen se sudými čísly.

@reseni
```python
suda = []
for n in range(1, 21):
    if n % 2 == 0:
        suda.append(n)
print(suda)
```
@end
