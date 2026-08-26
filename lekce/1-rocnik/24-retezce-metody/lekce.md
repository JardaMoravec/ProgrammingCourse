---
id: 24-retezce-metody
rocnik: 1
nazev: Metody řetězců
hodiny: 3
obtiznost: stredni
prerekvizity: [23-retezce-zaklady]
cile:
  - Použijete split, join, strip, replace
  - Převedete velikost písmen upper/lower/title
  - Vyhledáte podřetězec a ověříte prefix/suffix
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Metody řetězců

## Cíle lekce

- Ovládnete běžné metody pro úpravu textu
- Rozdělíte větu na slova a slova spojíte
- Očistíte vstup od mezer

## Čištění a změna velikosti

```python
s = "  Ahoj světe  "
print(s.strip())        # "Ahoj světe"
print(s.lower())        # malá písmena
print("python".title()) # Python
```

→ viz `priklady/retezce_metody.py`

## split a join

```python
veta = "Python je skvělý"
slova = veta.split()           # ["Python", "je", "skvělý"]
csv = "a,b,c".split(",")       # ["a", "b", "c"]
print("-".join(csv))           # a-b-c
```

## replace a find

```python
s = "banán banán"
print(s.replace("banán", "hruška"))
print(s.find("n"))    # index prvního výskytu, -1 pokud není
print(s.count("a"))
```

## startswith / endswith

```python
soubor = "data.txt"
if soubor.endswith(".txt"):
    print("Textový soubor")
```

## Shrnutí

| Metoda | Účel |
|--------|------|
| `strip()` | odstraní mezery okolo |
| `split()` | rozdělí na slova |
| `join()` | spojí seznam |
| `replace()` | nahradí text |

## Co dál

→ [Lekce 25: IO operace — čtení ze souboru](../25-soubory-cteni/lekce.md)
