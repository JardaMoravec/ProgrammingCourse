---
id: 08-porovnaci-operatory
rocnik: 1
nazev: Porovnávací a logické operátory
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [07-datove-typy]
cile:
  - Použijete porovnávací operátory
  - Složíte podmínky pomocí and, or, not
  - Pochopíte, že porovnání vrací bool
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/02 - Proměnné, datové typy a operátory v Pythonu.pptx"
---

# Porovnávací a logické operátory

## Cíle lekce

- Znáte operátory pro porovnání hodnot
- Umíte kombinovat podmínky logicky
- Připravíte se na větvení `if`

## Porovnávací operátory

Výsledek je vždy `True` nebo `False`:

| Operátor | Význam | Příklad |
|----------|--------|---------|
| `==` | rovno | `a == 10` |
| `!=` | nerovno | `a != 0` |
| `>` | větší | `a > 10` |
| `<` | menší | `a < 10` |
| `>=` | větší nebo rovno | `a >= 10` |
| `<=` | menší nebo rovno | `a <= 10` |

Speciální operátory:

| Operátor | Význam | Příklad |
|----------|--------|---------|
| `is` | identita objektu | `a is None` |
| `in` | obsažení | `'a' in 'ahoj'` |

## Logické operátory

| Operátor | Význam | Příklad |
|----------|--------|---------|
| `and` | obě podmínky musí platit | `x > 0 and x < 100` |
| `or` | alespoň jedna platí | `a == 5 or b == 5` |
| `not` | negace | `not je_plnolety` |

### Pravdivostní tabulka (and / or)

| Výraz | Výsledek |
|-------|----------|
| `True and True` | `True` |
| `True and False` | `False` |
| `True or False` | `True` |
| `False or False` | `False` |
| `not True` | `False` |

→ viz `priklady/logicke.py`

## Praktické příklady

```python
vek = 17
plnolety = vek >= 18          # False
v_rozsahu = 0 <= vek <= 120    # True — řetězení porovnání

text = "ahoj"
print("a" in text)            # True
```

## Co dál s výsledkem?

Porovnání samo o sobě jen vrátí `True`/`False`. V další lekci použijeme výsledek v **`if`** pro větvení programu.

## Shrnutí

| Operátor | Typ |
|----------|-----|
| `==`, `!=`, `<`, `>` | porovnání |
| `and`, `or`, `not` | logika |
| `in` | membership |

## Co dál

→ [Lekce 09: Větvení programu](../09-vetveni-podminek/lekce.md)
