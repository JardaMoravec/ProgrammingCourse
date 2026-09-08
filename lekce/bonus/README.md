# Bonus — lekce

**Volitelné lekce mimo hodinovou dotaci ročníků.**

Kompletní osnova: [`kurikulum/bonus.yaml`](../../kurikulum/bonus.yaml)

Úvod na rozcestníku (žáci): [`uvod.md`](uvod.md)

Nejsou v 81 h (1. ročník) ani v 68 h (3. ročník). Lze je přeskočit.

## Přehled lekcí

| # | ID | Téma | Úkoly VPL | Doporučeno po |
|---|-----|------|-----------|----------------|
| 01 | `01-konzole` | Konzole — Windows a Linux | — | 1. ročník, lekce 02 |
| 02 | `02-git-a-github` | Git a GitHub | — | 1. ročník, lekce 27 |
| 03 | `03-docker` | Docker | — | bonus 02 |
| 04 | `04-orm` | ORM (Flask-SQLAlchemy) | 2 | 3. ročník, lekce 20 |
| 05 | `05-csv-json-xml` | CSV, JSON a XML | 3 | 1. ročník, lekce 26 |
| 06 | `06-api-rest-graphql` | API — REST a GraphQL | — | 3. ročník, lekce 01 |

Konzole, Git, Docker a REST/GraphQL mají jen cvičení v hodině. CSV/JSON/XML a ORM mají úkoly v AMOS.

## Build

```bash
python scripts/generate_tasks.py          # ukoly.md + VPL testy z ukol.yaml
python scripts/build_html_output.py   # HTML pro žáky
```

Moodle: [`moodle/README.md`](../../moodle/README.md)
