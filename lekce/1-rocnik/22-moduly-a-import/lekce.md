---
id: 22-moduly-a-import
rocnik: 1
nazev: Moduly, import a knihovna math
hodiny: 3
obtiznost: stredni
prerekvizity: [21-kolekce-procviceni]
cile:
  - Importujete vestavěný modul math
  - Pochopíte rozdíl mezi import a from-import
  - Rozdělíte kód do více souborů
migrovano_z:
  - kurikulum/1-rocnik.yaml
---

# Moduly, import a knihovna math

## Cíle lekce

- Pochopíte modul jako soubor s funkcemi
- Použijete knihovnu `math` pro matematické výpočty
- Naimportujete vlastní pomocný modul

## Import modulu

```python
import math

print(math.sqrt(16))    # 4.0
print(math.pi)
print(math.floor(3.7))  # 3
```

→ viz `priklady/import_math.py`

## Různé formy importu

```python
import math
from math import sqrt, pi
import math as m

print(sqrt(25))
print(m.cos(0))
```

## Vlastní modul

Soubor `pomocne.py`:
```python
def pozdrav(jmeno):
    return f"Ahoj, {jmeno}!"
```

Hlavní program:
```python
import pomocne
print(pomocne.pozdrav("Anna"))
```

## Co je `if __name__ == "__main__"`?

Kód pod touto podmínkou se spustí jen při přímém spuštění souboru, ne při importu.

```python
def main():
    print("Běžím jako hlavní program")

if __name__ == "__main__":
    main()
```

## Užitečné z math

| Funkce | Význam |
|--------|--------|
| `sqrt(x)` | odmocnina |
| `ceil(x)` | zaokrouhlení nahoru |
| `floor(x)` | zaokrouhlení dolů |
| `pow(x, y)` | mocnina |

## Shrnutí

Moduly = organizace kódu a knihovny. Python má bohatou standardní knihovnu.

## Co dál

→ [Lekce 23: Znaky a řetězce — operátory](../23-retezce-zaklady/lekce.md)
