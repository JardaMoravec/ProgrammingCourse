# Cvičení — Cyklus for a range

## Cvičení 1 — Sudá a lichá čísla (★★☆)

> Adaptace: `úkol 16 - sudá a lichá čísla.docx`

Projděte `range(1, 31)`, sečtěte sudá a lichá zvlášť.

@reseni
```python
suda = 0
licha = 0

for n in range(1, 31):
    if n % 2 == 0:
        suda += n
    else:
        licha += n

print("Součet sudých:", suda)
print("Součet lichých:", licha)
```
@end

---

## Cvičení 2 — Násobilková tabulka (★★☆)

Načtěte n a vypište násobky 1–10.

@reseni
```python
n = int(input("Číslo: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
@end

---

## Cvičení 3 — Dělitelné třemi (★★☆)

Vypište čísla 1–100 dělitelná 3.

@reseni
```python
for x in range(1, 101):
    if x % 3 == 0:
        print(x, end=" ")
```
@end

---

## Cvičení 4 — Pyramida hvězdiček (★★★)

@reseni
```python
for i in range(1, 6):
    print("*" * i)
```
@end

---

## Cvičení 5 — Průměr N čísel (★★★)

Načtěte N, pak N× číslo a vypište průměr.

@reseni
```python
n = int(input("Kolik čísel: "))
soucet = 0
for _ in range(n):
    soucet += float(input("Číslo: "))
if n > 0:
    print("Průměr:", soucet / n)
else:
    print("Není co průměrovat.")
```
@end
