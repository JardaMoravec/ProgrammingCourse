# Bonus — lekce

**Volitelné lekce mimo hodinovou dotaci ročníků.**

Kompletní osnova: [`kurikulum/bonus.yaml`](../../kurikulum/bonus.yaml)

Úvod na rozcestníku (žáci): [`uvod.md`](uvod.md)

Nejsou v 81 h (1. ročník) ani v 68 h (3. ročník). Lze je přeskočit.

## Přehled lekcí

| # | ID | Téma | Úkoly VPL | Doporučeno po |
|---|-----|------|-----------|----------------|
| 01 | `01-git-a-github` | Git a GitHub | — | 1. ročník, lekce 27 |
| 02 | `02-docker` | Docker | — | bonus 01 |
| 03 | `03-orm` | ORM (Flask-SQLAlchemy) | 2 | 3. ročník, lekce 20 |

Git a Docker mají jen cvičení v hodině, bez úkolu v AMOS. ORM má Flask úkoly s VPL hodnotitelem.

## Build

```bash
python scripts/generate_tasks.py          # ukoly.md + VPL testy z ukol.yaml
python scripts/build_html_output.py   # HTML pro žáky
```

Moodle: [`moodle/README.md`](../../moodle/README.md)
