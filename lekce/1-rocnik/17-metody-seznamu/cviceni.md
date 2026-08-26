# Cvičení — Metody seznamů

## Úkol 1 — Seřazení známek (★★☆)

Seznam známek seřaďte vzestupně a vypište nejhorší a nejlepší.

@reseni
```python
znamky = [2, 4, 1, 3, 2]
znamky.sort()
print("Nejhorší:", znamky[0], "Nejlepší:", znamky[-1])
```
@end

---

## Úkol 2 — Odstranění duplicit (★★★)

Z `[1, 2, 2, 3, 3, 3, 4]` vytvořte seznam bez opakování (postupně procházejte a přidávejte jen nové).

@reseni
```python
puvodni = [1, 2, 2, 3, 3, 3, 4]
bez_duplicit = []
for x in puvodni:
    if x not in bez_duplicit:
        bez_duplicit.append(x)
print(bez_duplicit)
```
@end

---

## Úkol 3 — Druhé největší (★★★)

Najděte druhé největší číslo v seznamu (seřaďte nebo projděte dvakrát).

@reseni
```python
cisla = [5, 1, 9, 3, 9, 2]
serazene = sorted(set(cisla), reverse=True)
print(serazene[1] if len(serazene) >= 2 else "N/A")
```
@end

---

## Úkol 4 — Výřez (★★☆)

Z seznamu 10 čísel vypište první polovinu a druhou polovinu.

@reseni
```python
a = list(range(1, 11))
polovina = len(a) // 2
print(a[:polovina], a[polovina:])
```
@end
