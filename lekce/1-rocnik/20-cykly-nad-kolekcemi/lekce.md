---
id: 20-cykly-nad-kolekcemi
rocnik: 1
nazev: Cykly nad seznamy a slovníky
hodiny: 3
obtiznost: stredni
prerekvizity: [19-slovniky]
cile:
  - Filtrujete a transformujete seznam pomocí cyklu
  - Projdete slovník a agregujete data
  - Použijete list comprehension (úvod)
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Cykly nad seznamy a slovníky

## Cíle lekce

- Spojíte cykly `for` s kolekcemi
- Vytvoříte nový seznam z existujícího (filtr, mapování)
- Sečtete nebo spočítáte data ve slovníku

## for nad seznamem

```python
cisla = [1, 2, 3, 4, 5]
suda = []
for n in cisla:
    if n % 2 == 0:
        suda.append(n)
```

→ viz `priklady/cykly_kolekce.py`

## for nad slovníkem

```python
prodeje = {"leden": 10, "únor": 15, "březen": 12}
celkem = 0
for mesic, ks in prodeje.items():
    print(mesic, ks)
    celkem += ks
print("Celkem:", celkem)
```

## List comprehension (úvod)

Zkrácený zápis pro vytvoření seznamu:

```python
cisla = [1, 2, 3, 4, 5]
suda = [n for n in cisla if n % 2 == 0]
ctverce = [n ** 2 for n in range(1, 6)]
```

Ekvivalent delšího cyklu — používejte, až rozumíte oběma formám.

## Vnořené cykly nad maticí

```python
matice = [[1, 2], [3, 4], [5, 6]]
for radek in matice:
    for prvek in radek:
        print(prvek, end=" ")
    print()
```

## Shrnutí

| Úloha | Postup |
|-------|--------|
| filtr | cyklus + podmínka + append |
| součet slovníku | `for` přes `.values()` |
| nový seznam | comprehension nebo cyklus |

## Co dál

→ [Lekce 21: Kolekce — souhrnné procvičení](../21-kolekce-procviceni/lekce.md)
