# Cvičení — Slovníky

## Cvičení 1 — Telefonní seznam (★★☆)

Slovník jméno → telefon; načtěte jméno a vypište číslo nebo „nenalezeno“.

@reseni
```python
kontakty = {"Anna": "111", "Petr": "222"}
jmeno = input("Jméno: ")
print(kontakty.get(jmeno, "nenalezeno"))
```
@end

---

## Cvičení 2 — Počítání slov (★★★)

Na vstupu věta — slovník kolikrát se každé slovo vyskytuje (malá písmena).

@reseni
```python
veta = input("Věta: ").lower().split()
pocet = {}
for slovo in veta:
    pocet[slovo] = pocet.get(slovo, 0) + 1
print(pocet)
```
@end

---

## Cvičení 3 — Známky (★★☆)

Slovník předmět → známka; vypište průměr (1= nejlepší, 5= nejhorší).

@reseni
```python
znamky = {"mat": 2, "cj": 1, "prg": 1}
soucet = sum(znamky.values())
print("Průměr:", soucet / len(znamky))
```
@end

---

## Cvičení 4 — Sloučení (★★☆)

Dva slovníky sloučte do třetího (druhý přepíše shodné klíče).

@reseni
```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
c = a.copy()
c.update(b)
print(c)
```
@end
