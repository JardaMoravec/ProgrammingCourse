# Cvičení — Moduly a třídy ve více souborech

## Cvičení 1 — Jídelní lístek ve dvou modulech (★☆☆)

Rozdělte program do souborů `jidlo.py` a `main.py`. Třída `Jidlo` patří
do `jidlo.py`; její konstruktor uloží název jídla. V `main.py`
importujte třídu, vytvořte `Jidlo("Kulajda")` a vypište její název.

@reseni
`jidlo.py`:

```python
class Jidlo:
    def __init__(self, nazev):
        self.nazev = nazev
```

`main.py`:

```python
from jidlo import Jidlo

jidlo = Jidlo("Kulajda")
print(jidlo.nazev)
```
@end

---

## Cvičení 2 — Sportovní klub a jednosměrné importy (★★☆)

Máte soubory `hrac.py`, `tym.py` a `main.py`. Třída `Tym` uchovává
hráče a hlavní program vytváří tým i hráče. Určete, které soubory mají
co importovat.

@reseni
- `hrac.py` definuje `Hrac`; nic z dalších souborů nepotřebuje.
- `tym.py` importuje `Hrac`, pokud ji ve svých metodách potřebuje.
- `main.py` importuje `Hrac` i `Tym` a propojí je.

Importy jdou jedním směrem: `main.py` → `tym.py` → `hrac.py`.
`hrac.py` nesmí importovat `tym.py`.
@end
