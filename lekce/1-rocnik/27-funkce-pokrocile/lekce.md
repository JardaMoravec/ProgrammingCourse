---
id: 27-funkce-pokrocile
rocnik: 1
nazev: Funkce — lokální a globální proměnné
hodiny: 3
obtiznost: pokrocily
prerekvizity: [26-soubory-zapis]
cile:
  - Rozlišíte lokální a globální proměnnou
  - Pochopíte, kdy nepoužívat global
  - Předáte parametry a vrátíte hodnotu místo úpravy globálu
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Funkce — lokální a globální proměnné

## Cíle lekce

- Pochopíte **rozsah platnosti** proměnné
- Naučíte se psát funkce bez skrytých vedlejších efektů
- Znáte rozdíl mezi `global` a návratovou hodnotou

## Lokální proměnná

Proměnná vytvořená **uvnitř funkce** existuje jen tam:

```python
def f():
    x = 10
    print(x)

f()
# print(x)  # NameError
```

→ viz `priklady/lokalni_globalni.py`

## Globální proměnná

Proměnná mimo funkci — viditelná v celém modulu:

```python
pocitadlo = 0

def pridej():
    global pocitadlo
    pocitadlo += 1
```

**Lepší styl** — vracet hodnotu:

```python
def pridej(hodnota):
    return hodnota + 1

pocitadlo = pridej(pocitadlo)
```

## Parametr vs. globál

| Globál | Parametr + return |
|--------|-------------------|
| těžko sledovatelný | jasné vstupy/výstupy |
| riziko chyb | snadnější testování |

## Stínění (shadowing)

```python
x = 1

def g():
    x = 2      # lokální x, globální se nemění
    print(x)

g()
print(x)  # 1
```

## Shrnutí

Preferujte **parametry a return** před `global`. Globální proměnné jen výjimečně.

## Co dál

Závěr 1. ročníku — doplňte **úkoly v Moodle** (VPL), které vám chybí. V 2. ročníku navážete objektovým programováním.
