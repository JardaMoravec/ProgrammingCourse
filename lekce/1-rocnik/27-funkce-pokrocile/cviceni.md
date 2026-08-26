# Cvičení — Lokální a globální proměnné

## Úkol 1 — Bez global (★★☆)

Funkce `zvys(o)` vrátí hodnotu o 1 větší — bez global.

@reseni
```python
def zvys(o):
    return o + 1

x = 5
x = zvys(x)
print(x)
```
@end

---

## Úkol 2 — Prohození (★★☆)

Funkce vrátí tuple (b, a) — prohoďte dvě hodnoty bez globálu.

@reseni
```python
def prohod(a, b):
    return b, a

x, y = 1, 2
x, y = prohod(x, y)
print(x, y)
```
@end

---

## Úkol 3 — Počítadlo volání (★★★)

Funkce s globálním počítadlem kolikrát byla volána (procvičení global).

@reseni
```python
volani = 0

def akce():
    global volani
    volani += 1

akce()
akce()
print("Volání:", volani)
```
@end

---

## Úkol 4 — Akumulátor (★★★)

Funkce `pridej_do_seznamu(seznam, prvek)` mění seznam (mutace) — proč to funguje bez global?

@reseni
Seznam je **objekt** — parametr odkazuje na stejný objekt v paměti, proto `append` změní původní seznam:

```python
def pridej(seznam, prvek):
    seznam.append(prvek)

a = [1, 2]
pridej(a, 3)
print(a)  # [1, 2, 3]
```
@end
