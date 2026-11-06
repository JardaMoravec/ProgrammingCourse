---
id: 11-moduly-a-soubory
rocnik: 2
nazev: Moduly a třídy ve více souborech
hodiny: 3
obtiznost: stredni
prerekvizity: [10-staticke-metody-a-promenne]
cile:
  - Rozdělíte třídy a hlavní program do samostatných modulů
  - Naimportujete třídu z jiného souboru
  - Navrhnete závislosti modulů bez kruhových importů
migrovano_z: []
---

# Moduly a třídy ve více souborech

Lekce má **3 hodiny**. Dosud jste program psali do jednoho souboru. Jakmile
má aplikace více tříd, rozdělíte ji do souborů podle jejich odpovědnosti.
Každý soubor s Python kódem je **modul**.

## Cíle lekce

- Třídy, které spolu souvisejí, uložíte do pojmenovaných modulů
- Importujete třídu pomocí `from modul import Trida`
- Spustíte hlavní program ze správného místa

## Jeden soubor pro jednu odpovědnost

Například jednoduchá půjčovna může mít tuto strukturu:

```text
pujcovna/
    main.py
    kolo.py
    pujcovna.py
```

- `kolo.py` obsahuje definici třídy `Kolo`
- `pujcovna.py` obsahuje třídu `Pujcovna`, která pracuje s koly
- `main.py` vytvoří objekty a spustí program

Modul pojmenujte podle jeho obsahu. Název souboru bez `.py` je název
modulu. Nepojmenovávejte vlastní soubor `random.py`, `datetime.py` ani
jiným názvem standardního modulu — zastínil by knihovnu Pythonu.

## Import třídy

V `kolo.py`:

```python
class Kolo:
    def __init__(self, znacka):
        self.znacka = znacka
```

V `main.py`:

```python
from kolo import Kolo

kolo = Kolo("Author")
print(kolo.znacka)
```

Soubor `main.py` a `kolo.py` jsou ve stejné složce. Spusťte `main.py`
z této složky. Python najde `kolo.py` a připraví z něj modul `kolo`.

Můžete také importovat celý modul:

```python
import kolo

moje_kolo = kolo.Kolo("Author")
```

Zápis `from kolo import Kolo` zpřístupní třídu přímo. Zápis `import kolo`
ponechá viditelné, odkud třída pochází.

## Závislosti jedním směrem

`pujcovna.py` může importovat `Kolo`. Hlavní program pak importuje obě
třídy. Kolo ale nemá importovat půjčovnu:

```text
main.py ──→ pujcovna.py ──→ kolo.py
    └─────────────────────→ kolo.py
```

Když se dva moduly navzájem importují, vzniká **kruhový import**. Jeden
modul ještě není připravený, když ho druhý začne používat. Přesuňte
sdílenou třídu do třetího modulu nebo závislosti uspořádejte jedním směrem.

Do importovaného modulu pište hlavně definice tříd a funkcí. Kód na
nejvyšší úrovni souboru se spustí už při importu. Vytváření objektů,
načítání vstupu a spuštění programu proto patří do `main.py`.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| `from kolo.py import Kolo` | Do importu se nepíše přípona `.py` |
| soubor se jmenuje jako standardní modul | Python může načíst váš soubor místo knihovny |
| vstup a výpis jsou v importovaném modulu | spustí se i při pouhém importu |
| dva moduly importují jeden druhý | kruhový import a neúplně načtená definice |
| spustíte program z jiné složky | Python nemusí najít místní modul |

## Shrnutí

| Pojem | Význam |
|-------|--------|
| modul | Python soubor, například `kolo.py` |
| `import kolo` | zpřístupní modul |
| `from kolo import Kolo` | zpřístupní konkrétní třídu |
| hlavní program | místo, které propojí objekty a spustí aplikaci |

Příště použijete `@property` pro řízený přístup k atributu.

## Co dál

→ [Lekce 12: Vlastnosti a `@property`](../12-vlastnosti/lekce.md)
