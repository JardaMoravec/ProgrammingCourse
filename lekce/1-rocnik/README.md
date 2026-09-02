# 1. ročník — lekce

**Strukturované programování v Pythonu** — 81 hodin (27 týdnů × 3 h)

Kompletní osnova: [`kurikulum/1-rocnik.yaml`](../../kurikulum/1-rocnik.yaml)

Úvod na rozcestníku (žáci): [`uvod.md`](uvod.md)

## Struktura každé lekce

| Soubor | Účel | Pro koho |
|--------|------|----------|
| `lekce.md` | Teorie | žáci |
| `cviceni.md` | Procvičení v hodině **s řešením** (`@reseni`) | žáci |
| `ukoly/*/ukol.yaml` | Zadání úkolu + VPL testy (**zdroj pravdy**) | učitel |
| `ukoly/*/data.txt` | Testovací data u souborových úkolů | učitel |
| `ukoly.md` | Souhrn úkolů pro žáky (**generované**, není v Gitu) | CI / lokální build |
| `ukoly/*/vpl_evaluate.cases` | VPL soubor pro Moodle (**generované**) | CI / lokální build |
| `meta.yaml` | Metadata lekce | systém |
| `priklady/` | Ukázkový kód k teorii | žáci |

Lekce **01–03** (úvod) nemají `ukoly.md` — jsou čistě teoretické / instalace.

## Přehled lekcí

| # | ID | Téma | Úkoly VPL |
|---|-----|------|-----------|
| 01 | `01-programovani-a-jazyky` | Programování a jazyky | — |
| 02 | `02-python-a-prostredi` | Python a IDE | — |
| 03 | `03-bloky-kodu` | Bloky kódu | — |
| 04 | `04-promenne-a-pamet` | Proměnné, paměť a pojmenování | 4 |
| 05 | `05-aritmeticke-operatory` | Aritmetické operátory | 5 |
| 06 | `06-vstup-a-vystup` | Vstup a výstup (input, print) | 4 |
| 07 | `07-datove-typy` | Datové typy a přetypování | 4 |
| 08 | `08-porovnaci-operatory` | Logické operátory | 4 |
| 09 | `09-vetveni-podminek` | Větvení if/elif/else | 5 |
| 10 | `10-vnorene-podminky` | Vnořené podmínky | 4 |
| 11 | `11-chyby-a-vyjimky` | Výjimky try/except | 4 |
| 12 | `12-cyklus-while` | Cyklus while | 4 |
| 13 | `13-cyklus-for` | Cyklus for a range | 4 |
| 14 | `14-ridici-struktury-procviceni` | Řízení — procvičení | 4 |
| 15 | `15-funkce-zaklady` | Funkce — základy | 4 |
| 16 | `16-seznamy` | Seznamy | 4 |
| 17 | `17-metody-seznamu` | Metody seznamů | 4 |
| 18 | `18-tuples-a-range` | Tuples a range | 4 |
| 19 | `19-slovniky` | Slovníky | 4 |
| 20 | `20-cykly-nad-kolekcemi` | Cykly nad kolekcemi | 4 |
| 21 | `21-kolekce-procviceni` | Kolekce — procvičení | 4 |
| 22 | `22-moduly-a-import` | Moduly a math | 4 |
| 23 | `23-retezce-zaklady` | Řetězce | 4 |
| 24 | `24-retezce-metody` | Metody řetězců | 4 |
| 25 | `25-soubory-cteni` | Čtení ze souboru | 4 |
| 26 | `26-soubory-zapis` | Zápis do souboru | 4 |
| 27 | `27-funkce-pokrocile` | Funkce — lokální/globální | 4 |

**Celkem: 97 úkolů** s VPL testy (lekce 04–27).

## Build

```bash
python scripts/generate_tasks.py          # ukoly.md + vpl_evaluate.cases z ukol.yaml
python scripts/build_html_output.py   # HTML pro žáky
```

Moodle: [`moodle/README.md`](../../moodle/README.md)
