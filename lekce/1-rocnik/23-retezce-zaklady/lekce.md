---
id: 23-retezce-zaklady
rocnik: 1
nazev: Znaky a řetězce — operátory
hodiny: 3
obtiznost: stredni
prerekvizity: [22-moduly-a-import]
cile:
  - Pracujete s indexováním a řezy řetězců
  - Spojíte řetězce a použijete f-string
  - Porovnáte řetězce a testujete příslušnost
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Znaky a řetězce — operátory

## Cíle lekce

- Ovládnete řetězec jako sekvenci znaků
- Použijete `+`, `*`, indexy a řezy
- Formátujete výstup pomocí f-stringů

## Řetězec jako sekvence

```python
s = "Python"
print(s[0])      # P
print(s[-1])     # n
print(s[1:4])    # yth
print(len(s))    # 6
```

→ viz `priklady/retezce.py`

## Spojování a opakování

```python
a = "Ahoj"
b = " světe"
print(a + b)
print("-" * 20)
```

## f-string

```python
jmeno = "Anna"
vek = 16
print(f"{jmeno} je {vek} let.")
print(f"Za rok: {vek + 1}")
```

## Porovnání a testy

```python
print("abc" < "abd")      # True (lexikograficky)
print("a" in "banán")     # True
print("x" not in "ahoj")  # True
```

## Escapování a uvozovky

```python
print('Řekl: "Ahoj!"')
print("Cesta: C:\\Users")
```

## Shrnutí

| Operace | Příklad |
|---------|---------|
| index | `s[i]` |
| řez | `s[a:b]` |
| spojení | `a + b` |
| opakování | `"*" * 10` |
| formát | `f"{x}"` |

## Co dál

→ [Lekce 24: Metody řetězců](../24-retezce-metody/lekce.md)
