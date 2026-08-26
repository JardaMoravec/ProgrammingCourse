# Cvičení — Kolekce (souhrn)

## Úkol 1 — Evidence knih (★★☆)

Seznam slovníků `{název, autor, rok}` — vypište knihy po roce 2000.

@reseni
```python
knihy = [
    {"nazev": "A", "autor": "X", "rok": 1999},
    {"nazev": "B", "autor": "Y", "rok": 2010},
]
for k in knihy:
    if k["rok"] > 2000:
        print(k["nazev"])
```
@end

---

## Úkol 2 — Histogram (★★★)

Seznam známek 1–5 — slovník kolikrát každá známka.

@reseni
```python
znamky = [1, 2, 2, 3, 1, 5, 2]
hist = {}
for z in znamky:
    hist[z] = hist.get(z, 0) + 1
print(hist)
```
@end

---

## Úkol 3 — Seřazení studentů (★★★)

Seznam jmen seřaďte abecedně a vypište s pořadím.

@reseni
```python
jmena = ["Petr", "Anna", "Eva"]
jmena.sort()
for i, j in enumerate(jmena, 1):
    print(i, j)
```
@end

---

## Úkol 4 — Množina unikátních (★★☆)

Ze seznamu čísel vypište unikátní hodnoty (bez set — použijte slovník nebo cyklus).

@reseni
```python
a = [1, 2, 2, 3, 1, 4]
unikatni = list(dict.fromkeys(a))
print(unikatni)
```
@end
