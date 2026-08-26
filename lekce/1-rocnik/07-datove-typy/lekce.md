---
id: 07-datove-typy
rocnik: 1
nazev: Základní datové typy (int, float, str, bool)
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [06-promenne-a-pamet]
cile:
  - Rozlišíte int, float, str a bool
  - Použijete funkci type()
  - Pochopíte jednoduché vs. složené typy
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/02 - Proměnné, datové typy a operátory v Pythonu.pptx"
---

# Základní datové typy

## Cíle lekce

- Znáte čtyři základní datové typy Pythonu
- Umíte zjistit typ proměnné
- Rozumíte rozdílu skalár vs. kolekce (náhled)

## Proč datové typy?

Počítač ukládá různá data různým způsobem. **Datový typ** určuje, jaká operace je smysluplná:

```python
5 + 3       # OK — sčítání čísel
"5" + "3"   # OK — spojení textu → "53"
"5" + 3     # CHYBA — nelze mixovat
```

## Jednoduché typy (skaláry)

### int — celé číslo

```python
a = 10
b = -458
```

### float — desetinné číslo

```python
c = 0.159
d = 10.74
d2 = .17    # = 0.17
```

Desetinná **tečka**, ne čárka. Float není neomezeně přesný.

### str — řetězec (text)

```python
s = 'nějaký text'
t = "jiný text"
```

Jednoduché `' '` nebo dvojité `" "` uvozovky.

### bool — pravdivostní hodnota

```python
schvaleno = True
prospel = False
```

Pouze `True` nebo `False` — **s velkým písmenem na začátku**.

## Zjištění typu

```python
x = 1.56
print(type(x))   # <class 'float'>
```

## Skalár vs. kolekce (náhled)

| Skalár | Kolekce (později) |
|--------|-------------------|
| jedna hodnota | více hodnot |
| `int`, `float`, `bool` | seznam, slovník, tuple |
| věk, teplota | seznam studentů, košík |

→ viz `priklady/datove_typy.py`

## Přetypování (type casting)

Funkce pro převod mezi typy — důležité zejména po `input()`:

```python
text = "10"
cislo = int(text)       # 10 (int)
desetinne = float(text) # 10.0 (float)
zpet = str(cislo)       # "10" (str)
```

→ viz `priklady/pretipovani.py`

### Pozor na neplatný vstup

```python
int("abc")   # ValueError
```

Validaci chyb řešíme v lekci 11 (výjimky).

## Shrnutí

| Typ | Python | Příklad |
|-----|--------|---------|
| Celé číslo | `int` | `42` |
| Desetinné | `float` | `3.14` |
| Text | `str` | `"Ahoj"` |
| Pravda/nepravda | `bool` | `True` |
| Převod typu | `int()`, `float()`, `str()` | `int("5")` |

## Co dál

→ [Lekce 08: Porovnávací a logické operátory](../08-porovnaci-operatory/lekce.md)
