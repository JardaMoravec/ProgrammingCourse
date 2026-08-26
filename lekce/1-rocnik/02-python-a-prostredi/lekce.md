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
  - Spustíte první program
migrovano_z:
  - "zdroje/Programování 1.docx"
  - "zdroje/01 - Úvod do Pythonu.pptx"
---

# Python, instalace a vývojové prostředí

## Cíle lekce

- Pochopíte vlastnosti Pythonu
- Nainstalujete a spustíte Python
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

## Instalace

1. Stáhněte Python z [python.org](https://www.python.org/) — volte **Python 3**, nejnovější stabilní verzi.
2. Při instalaci ve Windows zaškrtněte **„Add Python to PATH“**.
3. Ověřte v terminálu:

```bash
python --version
```

### PIP — správce balíčků

PIP instaluje knihovny třetích stran:

```bash
pip install nazev_balicku
```

Na Linuxu: `sudo apt install python3-pip`

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
| REPL | Konzole Pythonu — Read-Eval-Print Loop |
| Skript | Soubor `.py` s kódem |
| IDE | Integrated Development Environment |
| PIP | Instalátor balíčků |

## Co dál

→ [Lekce 03: Anatomie programu a bloky kódu](../03-bloky-kodu/lekce.md)
