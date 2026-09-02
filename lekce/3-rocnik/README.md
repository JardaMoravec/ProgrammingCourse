# 3. ročník — lekce

**Tvorba webových stránek v Pythonu a Flasku** — 68 hodin (34 týdnů × 2 h)

Kompletní osnova: `[kurikulum/3-rocnik.yaml](../../kurikulum/3-rocnik.yaml)`

Předpoklady z 2. ročníku: **SQL a databáze** (PRG), **HTML a CSS** (jiné předměty). Zde se SQL ani HTML/CSS neučí — HTML/CSS se jen shrne v lekci 02, databáze se řeší jako **napojení Flask aplikace**.

Úvod na rozcestníku (žáci): [`uvod.md`](uvod.md)

## Struktura každé lekce


| Soubor                       | Účel                                                | Pro koho           |
| ---------------------------- | --------------------------------------------------- | ------------------ |
| `lekce.md`                   | Teorie                                              | žáci               |
| `cviceni.md`                 | Procvičení v hodině **s řešením** (`@reseni`)       | žáci               |
| `ukoly/*/ukol.yaml`          | Zadání úkolu + VPL testy (**zdroj pravdy**)         | učitel             |
| `ukoly/*/data.txt`           | Testovací data u souborových úkolů                  | učitel             |
| `ukoly.md`                   | Souhrn úkolů pro žáky (**generované**, není v Gitu) | CI / lokální build |
| `ukoly/*/vpl_evaluate.cases` | VPL stdin testy (**generované**, 1. ročník)         | CI / lokální build |
| `ukoly/*/vpl_evaluate.py`    | VPL Flask hodnotitel (**generované**)               | CI / lokální build |
| `ukoly/*/vpl_evaluate.sh`    | VPL obálka pro Flask hodnotitel (**generované**)    | CI / lokální build |
| `meta.yaml`                  | Metadata lekce                                      | systém             |
| `priklady/`                  | Ukázkový kód k teorii                               | žáci               |


Lekce **01** má úkol k odevzdání **snímku / výpisu** (ne VPL). Lekce **02** má jen cvičení. Lekce **03–22** mají Flask úkoly s VPL hodnotitelem. Lekce **23** má úkol k odevzdání aplikace (ne VPL, bez cvičení). Lekce **24** je jen prezentace (bez cvičení i bez úkolu). Lekce **05** trvá 4 hodiny, **23** trvá 20 hodin (zadání a práce), **24** trvá 4 hodiny (prezentace). Lekce **21** je **bonus** mimo 68 hodin (ORM, bez časové dotace — jde přeskočit).

## Přehled lekcí

| # | ID | Téma | Úkoly VPL |
|---|-----|------|-----------|
| 01 | `01-jak-funguje-web` | Jak funguje web | 1 (soubor) |
| 02 | `02-html-css-shrnuti` | HTML a CSS — shrnutí | — |
| 03 | `03-uvod-do-flasku` | Úvod do Flasku | 1 |
| 04 | `04-routy-a-pohledy` | Routy a pohledové funkce | 2 |
| 05 | `05-sablony-jinja` | Šablony Jinja2 (4 h) | 2 |
| 06 | `06-dedicnost-sablon` | Dědičnost šablon | 1 |
| 07 | `07-staticke-soubory` | Statické soubory (CSS, obrázky) | 1 |
| 08 | `08-dynamicke-url` | Dynamické URL a url_for | 1 |
| 09 | `09-konfigurace-a-chyby` | Konfigurace a chybové stránky | 1 |
| 10 | `10-flask-procviceni` | Flask základy — procvičení | 1 |
| 11 | `11-formulare-a-request` | Formuláře a objekt request | 1 |
| 12 | `12-validace-vstupu` | Validace dat na serveru | 1 |
| 13 | `13-presmerovani-a-flash` | Přesměrování a flash zprávy | 1 |
| 14 | `14-nahravani-souboru` | Nahrávání souborů a obrázků | 1 |
| 15 | `15-relace` | Relace (session) | 1 |
| 16 | `16-pripojeni-databaze` | Připojení aplikace k databázi | 1 |
| 17 | `17-vypis-z-databaze` | Výpis z databáze do šablony | 1 |
| 18 | `18-zapis-do-databaze` | Zápis z formuláře do databáze | 1 |
| 19 | `19-crud-v-aplikaci` | Úprava a mazání v aplikaci | 1 |
| 20 | `20-databaze-procviceni` | Databáze — procvičení | 1 |
| 21 | `21-orm` | ORM — bonus (0 h) | 2 |
| 22 | `22-bezpecnost-webu` | Bezpečnost (XSS, SQL injection) | 2 |
| 23 | `23-projekt` | Projekt — zadání a práce (20 h) | 1 (soubor) |
| 24 | `24-projekt-prezentace` | Projekt — odevzdání a prezentace (4 h) | — |

**Celkem: 23 lekcí v 68 h + 1 bonus** (lekce 01 a 23 mají úkol bez VPL, lekce 03–22 mají Flask VPL; lekce 24 je prezentace bez `ukoly.md`).

## Build

```bash
python scripts/generate_tasks.py          # ukoly.md + VPL testy z ukol.yaml
python scripts/build_html_output.py   # HTML pro žáky
```

Moodle: `[moodle/README.md](../../moodle/README.md)`
