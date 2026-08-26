# Cvičení — Datové typy

## Úkol 1 — type() (★☆☆)

Pro každou hodnotu určete typ pomocí `type()`:

`42`, `3.0`, `"3"`, `True`, `False`, `0`

@reseni
```python
print(type(42))      # <class 'int'>
print(type(3.0))     # <class 'float'>
print(type("3"))     # <class 'str'>
print(type(True))    # <class 'bool'>
print(type(False))   # <class 'bool'>
print(type(0))       # <class 'int'>  — nula je int, ne bool
```
@end

---

## Úkol 2 — Co spadne? (★★☆)

Které výrazy projdou a které vyvolají chybu? Ověřte v Pythonu.

```python
10 + 5
"10" + 5
"10" + "5"
True + 1
```

@reseni
| Výraz | Výsledek |
|-------|----------|
| `10 + 5` | `15` OK |
| `"10" + 5` | **TypeError** — str + int |
| `"10" + "5"` | `"105"` OK |
| `True + 1` | `2` OK (True = 1) |
@end

---

## Úkol 3 — Bool v praxi (★☆☆)

Uložte do proměnných, zda je student plnoletý (věk ≥ 18) a zda má známku prospěl (True/False). Zatím natvrdo, bez `input`.

@reseni
```python
vek = 17
prospel = True

je_plnolety = vek >= 18
print("Plnoletý:", je_plnolety)   # False
print("Prospěl:", prospel)         # True
```
@end
