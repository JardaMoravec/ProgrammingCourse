# Cvičení — Cykly nad kolekcemi

## Úkol 1 — Filtr kladných (★★☆)

Ze seznamu čísel vytvořte seznam jen kladných.

@reseni
```python
a = [-1, 3, 0, 5, -2]
kladne = [x for x in a if x > 0]
print(kladne)
```
@end

---

## Úkol 2 — Nejprodávanější měsíc (★★☆)

Ve slovníku prodejů najděte měsíc s nejvyšší hodnotou.

@reseni
```python
prodeje = {"leden": 10, "únor": 25, "březen": 15}
nejvic = max(prodeje, key=prodeje.get)
print(nejvic, prodeje[nejvic])
```
@end

---

## Úkol 3 — Délky slov (★★☆)

Seznam slov → seznam délek slov (comprehension).

@reseni
```python
slova = ["Python", "je", "super"]
delky = [len(s) for s in slova]
print(delky)
```
@end

---

## Úkol 4 — Součet sloupce (★★★)

Matice 3×3 — sečtěte každý sloupec do seznamu.

@reseni
```python
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soucty = []
for col in range(3):
    s = 0
    for row in range(3):
        s += m[row][col]
    soucty.append(s)
print(soucty)
```
@end
