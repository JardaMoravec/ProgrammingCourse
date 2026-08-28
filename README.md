# Kurz programování

Znalostní báze studijních materiálů pro 1.–3. ročník.

## Zdroj pravdy (data kurzu)

Veškerý obsah kurzu patří **pouze** do těchto složek:

| Složka | Co obsahuje |
|--------|-------------|
| `lekce/` | Teorie (`lekce.md`), cvičení (`cviceni.md`), metadata (`meta.yaml`), ukoly (`ukoly/*/ukol.yaml`, `data.txt`), ukázkový kód (`priklady/`) |
| `kurikulum/` | Osnovy ročníků, kompetence, struktura kurzu (`*.yaml`) |

Vše ostatní je **generované**, **šablony**, **nástroje** nebo **archiv migrace** — neupravujte tam obsah lekcí.

### Generované (nepatří do Gitu)

| Výstup | Generátor | Zdroj |
|--------|-----------|-------|
| `graficky-vystup/` | `build_html_output.py` | `lekce/**/*.md` |
| `lekce/**/ukoly.md` | `generate_tasks.py` | `lekce/**/ukoly/*/ukol.yaml` |
| `lekce/**/ukoly/*/vpl_evaluate.cases` | `generate_tasks.py` | `ukol.yaml` (1. ročník) |
| `lekce/**/ukoly/*/vpl_evaluate.py` + `.sh` | `generate_tasks.py` | `ukol.yaml` (Flask, 3. ročník) |

### Není datová vrstva

| Složka / soubor | Účel |
|-----------------|------|
| `scripts/` | Generátory (logika, ne obsah lekcí) |
| `sablony/` | Prázdné vzory pro nové soubory |
| `moodle/`, `PUBLIKACE.md` | Návody pro učitele |
| `zdroje/` | Dočasné DOCX/PPTX k migraci — po přepsání do `lekce/` smazat |
| `testy/` | Placeholder — budoucí kvízy patří do `lekce/` nebo `kurikulum/` |
| `assets/` | Placeholder — obrázky patří do příslušné lekce nebo sem po dohodě |

Původní soubory ve `zdroje/` projekt nepotřebuje k běhu — po migraci je lze odstranit.

## Struktura projektu

| Složka | Účel |
|--------|------|
| `lekce/` | **Hlavní obsah** (zdroj pravdy) |
| `kurikulum/` | **Osnovy a kompetence** (zdroj pravdy) |
| `graficky-vystup/` | Generovaný HTML výstup |
| `scripts/` | Generátory |
| `sablony/` | Šablony pro nové lekce |
| `zdroje/` | Archiv migrace (dočasné) |
| `moodle/` | Návod k Moodle VPL |

## Ročníky

- **1. ročník** — `lekce/1-rocnik/` — základy Pythonu
- **2. ročník** — `lekce/2-rocnik/` — pokročilý Python (OOP, algoritmy)
- **3. ročník** — `lekce/3-rocnik/` — tvorba webových stránek

Detailní osnova: `kurikulum/`.

## Build

```bash
pip install -r requirements.txt
python scripts/generate_tasks.py          # ukoly.md + VPL testy z ukol.yaml
python scripts/build_html_output.py   # HTML pro prohlížeč
```

Otevřete `graficky-vystup/index.html`. Úkoly pro Moodle: [`moodle/README.md`](moodle/README.md).

## Publikace na web (GitHub Pages)

Návod: [`PUBLIKACE.md`](PUBLIKACE.md). Po pushi do `main` GitHub Actions web sestaví automaticky.

## Jak přidat novou lekci

1. Zkopíruj šablony ze složky `sablony/`
2. Vytvoř složku `lekce/X-rocnik/NN-nazev-lekce/`
3. Doplň záznam do `kurikulum/X-rocnik.yaml`
4. Spusť generátory (viz Build)
