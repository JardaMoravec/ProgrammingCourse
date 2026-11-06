---
id: 13-dataclasses
rocnik: 2
nazev: Dataclasses
hodiny: 5
obtiznost: stredni
prerekvizity: [12-vlastnosti]
cile:
  - Vytvoříte datovou třídu dekorátorem @dataclass
  - Vysvětlíte, které metody dataclass vytvoří automaticky
  - Nastavíte bezpečnou výchozí hodnotu pro seznam pomocí field
migrovano_z: []
---

# Dataclasses

Lekce má **5 hodin**. Některé třídy hlavně uchovávají data. Jejich
konstruktor, textový výpis a porovnání podle obsahu se často opakují.
Dekorátor `@dataclass` je doplní za vás.

## Cíle lekce

- Zkrátíte datovou třídu pomocí `@dataclass`
- Rozpoznáte automaticky vytvořený `__init__`, `__repr__` a `__eq__`
- Ošetříte výchozí hodnotu seznamu pomocí `field(default_factory=...)`

## Automatický konstruktor a porovnání

```python
from dataclasses import dataclass


@dataclass
class Kniha:
    nazev: str
    rok: int


prvni = Kniha("R.U.R.", 1920)
druha = Kniha("R.U.R.", 1920)
print(prvni)             # Kniha(nazev='R.U.R.', rok=1920)
print(prvni == druha)    # True
```

Anotace `str` a `int` popisují očekávaný tvar dat. Samy o sobě hodnoty
nepřevádějí ani nekontrolují. Dataclass automaticky vytvoří konstruktor,
výpis pro ladění (`__repr__`) a rovnost podle polí (`__eq__`).

V obyčejné třídě byste tyto metody psali ručně. Pokud třída potřebuje
specifické chování, můžete přidat vlastní metody:

```python
@dataclass
class Kniha:
    nazev: str
    rok: int

    def je_starsi_nez(self, rok):
        return self.rok < rok
```

Dataclass se hodí pro záznamy, například knihu, bod nebo výsledek měření.
Třídu s komplikovaným životním cyklem a řadou metod pište jako běžnou
třídu, pokud by automaticky vytvořené metody nedávaly smysl.

## Výchozí hodnoty a seznamy

Pole s výchozí hodnotou musí následovat až za poli bez výchozí hodnoty:

```python
@dataclass
class Ukol:
    nazev: str
    hotovo: bool = False
```

U seznamu nepoužívejte přímo `ukoly: list = []`. Jeden seznam by pak
sdílely všechny instance. Použijte `field(default_factory=list)`:

```python
from dataclasses import dataclass, field


@dataclass
class Projekt:
    nazev: str
    ukoly: list = field(default_factory=list)


prvni = Projekt("Web")
druhy = Projekt("Hra")
prvni.ukoly.append("navrh")
print(prvni.ukoly)  # ['navrh']
print(druhy.ukoly)  # []
```

`default_factory=list` zavolá `list()` pro každý nový objekt zvlášť.
Změna seznamu jednoho projektu tak neovlivní druhý.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| chybí import `dataclass` | dekorátor není znám |
| anotace považujete za převod typu | `Kniha("R.U.R.", "1920")` má rok stále jako text |
| mutable `=[]` jako výchozí hodnota | objekty mohou sdílet stejný seznam |
| pole bez hodnoty je až za polem s výchozí hodnotou | konstruktor má neplatné pořadí parametrů |
| dataclass použijete na každou třídu | automatický výpis nebo rovnost nemusí odpovídat účelu |

## Shrnutí

| Zápis | Význam |
|-------|--------|
| `@dataclass` | automaticky vytvoří běžné metody datové třídy |
| anotace `nazev: str` | dokumentuje očekávaný typ |
| `field(default_factory=list)` | vytvoří nový seznam pro každý objekt |
| vlastní metoda | doplní chování, které třída potřebuje |

Příště propojíte OOP nástroje ve vlastním návrhu a pololetním projektu.

## Co dál

→ [Lekce 14: Vlastní výjimky a iterace](../14-vyjimky-a-iterace/lekce.md)
