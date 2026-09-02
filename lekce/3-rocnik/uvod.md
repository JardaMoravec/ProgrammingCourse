## Hlavní téma

Budete tvořit **dynamické webové stránky v Pythonu** — framework **Flask**. Naučíte se routy, šablony, formuláře a napojení aplikace na databázi, kterou už znáte z 2. ročníku.

Předmět má **68 hodin** (34 týdnů × 2 h). SQL ani HTML/CSS se tu znovu neučí: HTML a CSS jen shrneme, databázi ve Flasku **napojíte**.

## Struktura kurzu

| Blok | Hodiny | Co se naučíte |
|------|--------|----------------|
| Úvod a shrnutí | 4 h | jak funguje web, připomenutí HTML a CSS |
| Flask — základy | 18 h | instalace, routy, šablony Jinja2, statické soubory |
| Formuláře | 10 h | `request`, validace, soubory, relace (session) |
| Databáze ve Flasku | 12 h | `sqlite3`, výpis, zápis, úprava a mazání |
| Projekt | 24 h | vlastní aplikace a prezentace |

Lekce **21 (ORM)** je **bonus** — není v 68 hodinách, lze ji přeskočit. Bezpečnost webu (XSS, SQL injection) je v povinné výuce.

## Požadavky na žáky

Z předchozích ročníků a jiných předmětů potřebujete:

- Python: funkce, řetězce, základy objektů (1. a 2. ročník),
- **SQL** — `SELECT`, `INSERT`, relace 1:N a `JOIN` (2. ročník, PRG),
- **HTML a CSS** — značky, odkazy, formuláře, jednoduchý styl (jiné předměty ve 2. ročníku).

Potřebujete Python 3, editor, webový prohlížeč a SQLite. Flask nainstalujete v lekci 03.

Kdo SQL nebo HTML neovládá, doplní to *před* lekcemi o databázi ve Flasku — tady se příkazy SQL znovu nevykládají.

## Jak číst tento materiál

Každá lekce má až tři záložky:

| Záložka | Kdy | Co s tím |
|---------|-----|----------|
| **Lekce** | teorie v hodině i doma | čtěte a zkoušejte příklady (`priklady/`) |
| **Cvičení** | v hodině | procvičení s řešením (tlačítko *Zobrazit řešení*) |
| **Úkoly** | samostatně | odevzdáváte; řešení v materiálu **není** |

U webu odevzdáváte často víc souborů najednou (`*.py`, složka `templates/`, od lekce 07 i `static/`). Co přesně nahrát, je u každého úkolu.

Lekce **02** má jen cvičení. Lekce **23–24** jsou projekt (zadání, práce, prezentace).

## Odevzdávání do AMOS

1. Úkol najdete v **AMOS** u příslušné lekce.
2. Nahrajte soubory podle zadání. U šablon musí zůstat složka `templates/` (a později `static/`).
3. Spusťte **Evaluate**. Test kontroluje routy a HTML značky — text na stránce může být vlastní, struktura musí sedět.
4. Lekce **01** se odevzdává jako snímek / výpis (ne automatický test). **Projekt** podle zadání v lekci 23, ne přes Evaluate.

Cvičení z hodiny do AMOS nepatří.

**Odevzdání úkolů je povinné.** Termín je vždy v AMOS. Neodevzdání může mít negativní důsledky na prospěch. Absence žáka odevzdání **neomlouvá** — posouvá jen termín. Některé úkoly jsou **známkované**; učitel to řekne předem a je to uvedené v AMOS.
