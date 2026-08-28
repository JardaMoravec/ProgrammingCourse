---
id: 02-python-a-prostredi
rocnik: 1
nazev: Python, instalace a vývojové prostředí
hodiny: 3
obtiznost: zacatecnik
prerekvizity: [01-programovani-a-jazyky]
cile:
  - Nainstalujete Python a ověříte funkčnost
  - Rozlišíte konzoli, skript a IDE
  - Pochopíte rozdíl mezi knihovnou a balíčkem
  - Spustíte první program
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/01 - Úvod do Pythonu.pptx"
---

# Python, instalace a vývojové prostředí

## Cíle lekce

- Pochopíte vlastnosti Pythonu
- Nainstalujete a spustíte Python
- Víte, co jsou knihovny a balíčky a k čemu slouží PIP
- Víte, jakým nástrojem psát větší programy

## Python v kostce

- **Open-source** — zdrojový kód je volně dostupný
- **Interpretovaný** — kód se spouští přes interpret
- **Dynamicky typovaný** — typ proměnné nemusíte deklarovat
- **Multi-paradigm** — procedurální, objektové i funkcionální styly

### Proč Python pro začátečníky?

- jednoduchá syntaxe (odsazování místo `{ }`),
- program často „něco dělá“, než spadne — motivující pro učení,
- není nutné hned psát třídy ani importovat knihovny,
- výpočetně náročné části jsou napsané v C.

### Proč začít právě Pythonem? (přehled)

| Výhoda | Popis |
|--------|-------|
| Čitelná syntaxe | Kód připomíná psaný text |
| Bohatý ekosystém | Django, Pandas, knihovny pro vše |
| Trh práce | Žádaná dovednost v IT |
| Komunita | Kurzy, fóra, hotová řešení |

### Omezení Pythonu (ať víte, co čekat)

- pomalejší než C/Rust u extrémních výpočtů,
- vyšší spotřeba paměti,
- mobilní a frontend vývoj není jeho silná stránka.

## Knihovny a balíčky

Programátor nemusí psát **vše od nuly**. Hotový kód, který řeší opakující se úkoly (matematika, práce se soubory, stahování z internetu…), se sdružuje do **knihoven**. V Pythonu je jich tisíce — proto se říká, že Python má **bohatý ekosystém**.

### Co je knihovna?

**Knihovna** (anglicky *library*) je soubor **připraveného kódu** — funkcí, tříd nebo konstant — který můžete ve svém programu **použít**, aniž byste ho sami psali.

Představte si to jako **nástrojovou sadu**: místo abyste si vyrobili kladivo, použijete hotové z dílny. Chcete odmocninu? Nemusíte psát algoritmus — stačí knihovna `math`:

```python
import math
print(math.sqrt(16))   # 4.0
```

Knihovna vám **ušetří čas** a často obsahuje kód, který je **důkladně otestovaný** tisíci programátory.

### Co je balíček?

**Balíček** (anglicky *package*) je **způsob, jak je knihovna zabalená a distribuovaná** — obvykle složka se soubory `.py` a popisem (název, verze, závislosti). Jeden balíček může obsahovat jednu knihovnu, nebo i více souvisejících modulů.

| Pojem | Co to je | Příklad |
|-------|----------|---------|
| **Knihovna** | hotový kód, který používáte | `math`, `random` |
| **Balíček** | balení k distribuci a instalaci | balíček `requests` z internetu |
| **Modul** | konkrétní soubor `.py` uvnitř balíčku | soubor `math.py` ve standardní knihovně |

> V běžné řeči se *knihovna* a *balíček* často zaměňují — pro začátek stačí vědět: **knihovna = co používáte**, **balíček = co stáhnete a nainstalujete**.

### Vestavěná knihovna vs. balíčky třetích stran

| Typ | Odkud pochází | Instalace | Příklady |
|-----|---------------|-----------|----------|
| **Standardní knihovna** | součást Pythonu | žádná — už je nainstalovaná | `math`, `random`, `os` |
| **Balíčky třetích stran** | napsali je jiní autoři | přes **PIP** | `requests`, `pandas`, `flask` |

Standardní knihovna pokrývá základy (matematika, soubory, datum, sítě…). Když potřebujete něco specializovaného (analýza dat, webový framework), doinstalujete **externí balíček**.

### PIP — správce balíčků

**PIP** (*Pip Installs Packages*) stahuje balíčky z online repozitáře [PyPI](https://pypi.org/) (Python Package Index) a nainstaluje je do vašeho Pythonu:

```bash
pip install requests
```

Ověření, že balíček je nainstalovaný:

```bash
pip show requests
```

Seznam nainstalovaných balíčků:

```bash
pip list
```

Na Linuxu může být potřeba nejdřív nainstalovat PIP: `sudo apt install python3-pip`

> **Poznámka:** syntaxi `import` a různé způsoby importu probereme podrobně v [lekci 22](../22-moduly-a-import/lekce.md). Teď stačí vědět, že knihovnu **načtete** příkazem `import` a pak voláte její funkce.

### Výhody knihoven a balíčků

| Výhoda | Vysvětlení |
|--------|------------|
| **Rychlejší vývoj** | Nemusíte psát vše sami — stahování souboru, grafy, databáze už někdo vyřešil |
| **Ověřený kód** | Populární balíčky používají miliony lidí — chyby se rychle opravují |
| **Specializace** | Na web (`flask`), data (`pandas`), hry (`pygame`) existují balíčky „na míru“ |
| **Spolupráce** | Tým sdílí stejné balíčky — všichni pracují se stejnými nástroji |
| **Učení z cizího kódu** | Čtení dokumentace a příkladů knihoven rozvíjí programátorské myšlení |

### Nevýhody a na co si dát pozor

| Nevýhoda / riziko | Vysvětlení |
|-------------------|------------|
| **Závislost na cizím kódu** | Když autor balíčku přestane udržovat projekt, může přestat fungovat s novým Pythonem |
| **Bezpečnost** | Instalujete cizí kód — vybírejte známé balíčky s mnoha staženími na PyPI |
| **Konflikt verzí** | Dva projekty mohou chtít různé verze stejného balíčku (řeší se virtualenv — až později) |
| **Přehlcení** | Příliš mnoho balíčků = těžší orientace, co kód vlastně dělá |
| **„Černá skříňka“** | Používáte funkci, ale nechápete, jak funguje uvnitř — u učení občas lepší napsat si jednoduchou věc sami |

> **Pravidlo pro začátečníky:** nejdřív zvládněte základy Pythonu (proměnné, cykly, funkce). Knihovny pak **rozšiřují** to, co už umíte — nenahrazují pochopení jazyka.

## Instalace

1. Stáhněte Python z [python.org](https://www.python.org/) — volte **Python 3**, nejnovější stabilní verzi.
2. Při instalaci ve Windows zaškrtněte **„Add Python to PATH“**.
3. Ověřte v terminálu:

```bash
python --version
```

## Tři způsoby práce s Pythonem

| Způsob | Kdy použít |
|--------|------------|
| **Konzole (REPL)** | Rychlé testy, kalkulačka, jeden příkaz |
| **Soubor `.py`** | Větší programy, ukládání kódu |
| **IDE** | Pohodlná práce na projektech |

### Konzole

Spuštění: `python` v terminálu.

```python
>>> print("Ahoj!")
Ahoj!
>>> 2 + 2
4
```

Ukončení: `exit()` nebo Ctrl+Z (Win) / Ctrl+D (Linux).

### První skript

Soubor `hello.py`:

```python
print("Ahoj světe!")
```

Spuštění: `python hello.py`

→ viz `priklady/hello.py`

### Vývojová prostředí (IDE)

| IDE / editor | Odkaz |
|--------------|-------|
| PyCharm | [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/) |
| VS Code | [code.visualstudio.com](https://code.visualstudio.com/) |
| Cursor | editor s AI podporou |

Pro začátek stačí i jednoduchý editor s podporou Pythonu.

## Zen of Python

V konzoli zadejte:

```python
import this
```

Ukáže principy, na kterých Python stojí — např. *„Čitelnost se počítá.“*

## Shrnutí

| Pojem | Význam |
|-------|--------|
| Knihovna | Hotový kód (funkce, třídy), který importujete do programu |
| Balíček | Zabalená knihovna k distribuci a instalaci (např. přes PIP) |
| PyPI | Online repozitář Python balíčků |
| REPL | Konzole Pythonu — Read-Eval-Print Loop |
| Skript | Soubor `.py` s kódem |
| IDE | Integrated Development Environment |
| PIP | Instalátor balíčků |

## Co dál

→ [Lekce 03: Anatomie programu a bloky kódu](../03-bloky-kodu/lekce.md)
