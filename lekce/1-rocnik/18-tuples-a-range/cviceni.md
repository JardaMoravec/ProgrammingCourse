# Cvičení — Tuples a range

## Úkol 1 — Souřadnice (★☆☆)

Uložte bod (x, y) do tuple a vypište obě souřadnice.

@reseni
```python
bod = (12, 7)
x, y = bod
print(f"Bod ({x}, {y})")
```
@end

---

## Úkol 2 — min_max (★★☆)

Funkce vrátí tuple (minimum, maximum) ze seznamu.

@reseni
```python
def min_max(cisla):
    return min(cisla), max(cisla)

print(min_max([5, 2, 8, 1]))
```
@end

---

## Úkol 3 — Seznam z range (★★☆)

Vytvořte seznam sudých čísel 0–20 pomocí range a list().

@reseni
```python
suda = list(range(0, 21, 2))
print(suda)
```
@end

---

## Úkol 4 — zip (★★☆)

Dva seznamy — jména a známky — spojte a vypište „Jméno: známka“.

@reseni
```python
jmena = ["Anna", "Petr", "Eva"]
znamky = [1, 2, 3]
for j, z in zip(jmena, znamky):
    print(f"{j}: {z}")
```
@end
