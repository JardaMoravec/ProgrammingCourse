# Moodle — Virtual Programming Lab (VPL)

Návod pro učitele: jak z repozitáře založit automaticky hodnocené úkoly v Moodle.

## Struktura v repozitáři

Každá lekce **04–27** obsahuje:

```
lekce/1-rocnik/NN-nazev/
  ukoly.md              ← zadání pro žáky (generované)
  ukoly/
    01-slug/
      ukol.yaml            ← zdroj pravdy: zadání + VPL testy
      vpl_evaluate.cases   ← generované pro Moodle
      data.txt             ← volitelně (úkoly se soubory)
```

Lekce **01–03** jsou teoretické — úkoly nemají.

## Založení aktivity v Moodle

1. Přidejte aktivitu **Virtual programming lab**.
2. Jazyk: **Python 3**.
3. Požadovaný soubor od studenta: `main.py` (nebo dle zadání).
4. Zapněte **Automatic evaluation**.
5. V menu aktivity: **Execution options → Files** (soubory ke spuštění):
   - vložte obsah `vpl_evaluate.cases` ze složky úkolu,
   - pokud existuje `data.txt`, přidejte ho také (Execution files).
6. V **Test cases** vložte stejný obsah `vpl_evaluate.cases` (nebo jen v Execution files — dle verze VPL).
7. Zkratka názvu: kód z `ukoly.md`, např. `PRG-1-09-01`.

## Formát vpl_evaluate.cases (BIOTES)

```
Case = Popis testu
Input = vstup pro program
Output = "očekávaný výstup"

Case = Druhý test
Input = 10
20
Output = "Součet: 30"
```

- `Input` = text poslaný na stdin (více řádků = více `input()`).
- `Output` v uvozovkách = přesná shoda textu.
- Pro čísla s desetinnou tečkou lze použít numerický režim (viz dokumentace VPL).

Dokumentace: [VPL BIOTES](https://vpl.dis.ulpgc.es/documentation/vpl-4.4.2/biotes.html)

## Generování / úpravy

Po změně dat spusťte:

```bash
python scripts/generate_tasks.py
python scripts/build_html_output.py
```

Úpravy zadání a testů: soubor `ukoly/NN-slug/ukol.yaml` v příslušné lekci, poté spusťte generátor.

## Mapování ze složky Úkoly 1

| Původní úkol | Lekce | Moodle kód |
|--------------|-------|------------|
| úkol 1 — důchod | 09 | PRG-1-09-06 |
| úkol 3 — zisk | 09 | PRG-1-09-01 |
| úkol 6 — vlastnosti čísla | 09 | PRG-1-09-02 |
| úkol 9 — BMI | 09 | PRG-1-09-03 |
| úkol 4a — krychle | 09 | PRG-1-09-04 |
| úkol 4b/5 — obdélník | 09 | PRG-1-09-05 |
| úkol 12 — výjimky | 11 | (validace vstupu) |
| úkol 15 — hádání | 12 | PRG-1-12-01 |
| úkol 16 — sudá/lichá | 13 | PRG-1-13-01 |

## Hodnocení

- **Cvičení** v hodině — s řešením v materiálech (záložka Cvičení).
- **Úkoly** — samostatná práce, odevzdání a bodování přes VPL v Moodle.
