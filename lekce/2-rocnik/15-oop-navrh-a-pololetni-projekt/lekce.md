---
id: 15-oop-navrh-a-pololetni-projekt
rocnik: 2
nazev: OOP — návrh a pololetní projekt
hodiny: 18
obtiznost: stredni
prerekvizity: [14-vyjimky-a-iterace]
cile:
  - Navrhnete třídy ze zadání (je vs má) dřív, než začnete kód
  - Složíte jednu aplikaci z lekcí 03–14
  - Odevzdáte známkovaný pololetní projekt
migrovano_z:
  - "zdroje/Programování 2.docx (kap. Objektově orientovaná analýza a návrh)"
  - "zdroje/Úkoly 2/úkol 14, 15, 18"
---

# OOP — návrh a pololetní projekt

Lekce má **18 hodin**. Je to prostor na návrh, implementaci, testování
a prezentaci samostatné aplikace.

Nová syntaxe **nepřibývá**. Projekt uzavírá OOP před začátkem SQL
v druhém pololetí. Závěrečný projekt ročníku (SQL, lekce 32–33) tohle
**není**.

## Cíle lekce

- Ze zadání vypíšete třídy **než** napíšete `class`
- Odlišíte vztah **„je“** (dědičnost) a **„má“** (složení)
- Složíte jednu konzolovou aplikaci z lekcí 03–14

## Rozvrh 18 hodin

| Hodiny | Co dělat |
|--------|----------|
| 1–2 | návrh tříd, vztah je / má, rozdělení modulů; učitel schválí téma |
| 3–13 | implementace tříd a hlavního programu ve více souborech |
| 14–15 | testování a opravy; kontrola `property` a dataclass |
| 16–17 | dokončení, příprava ukázky a dokumentace |
| 18 | odevzdání do AMOS a krátká prezentace učiteli |

Bez schváleného tématu v první hodině kód nepište.

## Mapa lekcí 03–14

| Lekce | V projektu musíte ukázat |
|-------|--------------------------|
| [03](../03-tridy-a-objekty/lekce.md) | víc objektů, každý má svá data |
| [04](../04-konstruktor/lekce.md) | konstruktor, `self` |
| [05](../05-metody/lekce.md) | metody, které vrací nebo mění stav |
| [06](../06-specialni-metody/lekce.md) | `__str__`, `__eq__` a `__len__` |
| [07](../07-tridy-procviceni/lekce.md) | opakování 03–06, v projektu nic navíc |
| [08](../08-dedicnost/lekce.md) | rodič a potomek, `super()` |
| [09](../09-polymorfismus/lekce.md) | stejná metoda, jiné tělo, cyklus přes seznam |
| [10](../10-staticke-metody-a-promenne/lekce.md) | statické členy jsou volitelné, v projektu je nemusíte použít |
| [11](../11-moduly-a-soubory/lekce.md) | třídy oddělené do souborů, jednosměrné importy |
| [12](../12-vlastnosti/lekce.md) | vhodné použití `@property` |
| [13](../13-dataclasses/lekce.md) | dataclass pro datový záznam |
| [14](../14-vyjimky-a-iterace/lekce.md) | vlastní výjimka + `for` přes váš objekt |

Projekt musí být rozdělen do více souborů s jasnými odpovědnostmi. Použijte
`@property` pro vhodnou odvozenou nebo ověřovanou hodnotu a dataclass pro
jednoduchý datový záznam; v návrhu zdůvodněte, proč se tyto nástroje hodí.

## Nejdřív návrh

Ze zadání podtrhejte podstatná jména. U každého se zeptejte:

| Otázka | Vztah | V kódu |
|--------|--------|--------|
| A **je** B? (pes je zvíře) | dědičnost | `class Pes(Zvire)` |
| A **má** B? (auto má motor) | složení | `self.motor = Motor(...)` |
| Mají A i B totéž? | společné k rodiči | metoda / atribut u rodiče |

Až máte seznam tříd, atributů a metod na papíře, teprve pište kód.

Opakující se způsoby, jak třídy poskládat, mají jména — **návrhové vzory**. Základ (iterátor, strategie, továrna) je volitelně v [bonusu](../../bonus/07-navrhove-vzory/lekce.md). Do projektu je **nemusíte** znát.

![Od zadání přes návrh ke třídám](diagramy/navrh.svg)

Připomínka z lekce 08 — auto motor **má**, není jím:

```python
class Motor:
    def __init__(self, vykon):
        self.vykon = vykon


class Vozidlo:
    def __init__(self, znacka):
        self.znacka = znacka

    def hlaska(self):
        return "jedeme"


class Auto(Vozidlo):
    def __init__(self, znacka, vykon):
        super().__init__(znacka)
        self.motor = Motor(vykon)

    def hlaska(self):
        return "brum"
```

`Auto(Vozidlo)` je **je**. `self.motor` je **má**. `hlaska` u auta je přepis (lekce 09).

→ viz `priklady/je_vs_ma.py`

## Téma projektu

Téma je **vaše**, učitel ho schválí v první hodině. Musí dávat smysl a splnit seznam v záložce **Úkoly**.

Nesmí to být kopie z hodin: knihovna, autoservis, mailer, oblečení, pizza, elektronika, filmotéka, škola, košík, tarify, VIP lístek, osoba s adresou.

Obsah podle školního řádu: slušné, bez urážek, násilí, erotiky, drog, zbraní a nenávisti. V datech nejsou známky spolužáků ani citlivé údaje o konkrétních lidech.

Nápady, které nemusíte použít: půjčovna (kolo / koloběžka), jídelna (jídlo / polévka), hon na poklady (místnost / předmět), sportovní klub (hráč / zápas). Herní strategie a šachovnice z původních úkolů 14, 15 a 18 jsou v pořádku, **když** je sami navrhněte — neopisujte.

## Časté chyby

| Chyba | Následek |
|-------|----------|
| hned `class` bez seznamu tříd | duplicity, špatný vztah je / má |
| auto dědí z motoru | motor **má**, není jím |
| tři třídy vedle sebe bez rodiče | společný kód třikrát |
| v cyklu `if` podle typu | chybí polymorfismus |
| výjimka jen `print` v metodě | volající ji neošetří |
| `for x in self.seznam` místo `for x in objekt` | chybí `__iter__` |

## Shrnutí

| Pojem | Význam |
|-------|--------|
| návrh | třídy a vztahy **před** kódem |
| je | dědičnost |
| má | složení |
| pololetní projekt | jedna aplikace z lekcí 03–14, známka |

Příště relační databáze — tabulky, klíče, ještě bez SQL:
[lekce 16](../16-relacni-databaze/lekce.md).

Volitelně: [návrhové vzory (bonus)](../../bonus/07-navrhove-vzory/lekce.md) — mimo 170 hodin.

Známku určuje **učitel** (téma, návrh, splnění seznamu, že kód umíte vysvětlit). Automatický test výstup nekontroluje.

## Co dál

→ [Lekce 16: Principy relační databáze](../16-relacni-databaze/lekce.md)
