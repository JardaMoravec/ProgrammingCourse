# Moodle — Virtual Programming Lab (VPL)

Návod pro učitele: jak z repozitáře založit automaticky hodnocené úkoly v Moodle.

## E2E automatizace (základ)

Skript `scripts/moodle_e2e.py` otevře Moodle v prohlížeči Chromium, přihlásí
uživatele, najde nebo vytvoří a pojmenuje sekci podle čísla lekce, načte údaje
z `ukol.yaml` a vyplní formulář nové VPL aktivity. Ve výchozím stavu formulář
neukládá; k uložení je nutné výslovně přidat `--save`.

1. Nainstalujte závislosti a prohlížeč:

   ```bash
   python -m pip install -r requirements-moodle.txt
   python -m playwright install chromium
   ```

2. Zkopírujte `moodle/e2e.example.json` na `moodle/e2e.local.json` a nastavte
   `base_url`, `username` a `password`. Lokální konfigurace je v `.gitignore`.
   V objektu `courses` nastavte mapování názvu třídy na ID jejího kurzu.
   Heslo je v tomto souboru uložené jako prostý text; chraňte přístup k počítači
   a soubor nikam nesdílejte.
3. Spusťte například:

   ```bash
   python scripts/moodle_e2e.py --class 3I --lesson 7 --task 1 --pause
   ```

   Skript použije přihlašovací údaje pouze při lokálním přihlášení přes běžný
   Moodle formulář. Pokud škola používá SSO nebo jiný formulář, ponechte
   přihlašovací pole prázdná a přihlaste se ručně v otevřeném prohlížeči.
4. Ročník se odvodí z prvního čísla třídy (např. `2I` → 2. ročník,
   `1:IM` → 1. ročník). Skript nastaví název a úplný popis úkolu, na začátek
   popisu vloží ikonu kalendáře a tučný nadpis „Zadání:“. Běžné úkoly mají
   v popisu termín 10 dní od spuštění a vypnutý začátek i konec období odevzdání.
   Známkované úkoly se vybírají kódem `Z01` (složka `z01-*`) a název aktivity
   bude `ZNÁMKOVANÝ ÚKOL - <skutečný název úkolu>`; jejich období odevzdání
   se předvyplní na otevření za hodinu a uzavření za dvě hodiny.
   Pomocí „Omezit přístup“ se známkovaná aktivita úplně skryje až do půlnoci
   následujícího dne; popis se nezobrazuje ani na titulní straně kurzu.
   Čas lze po vytvoření aktivity ručně doladit v jejím nastavení. Pokud sekce
   pro lekci chybí, skript ji vytvoří za sekcí předchozí lekce a pojmenuje
   `Lekce NN - úkoly`. U první lekce použije jako předchozí sekci úvodní
   sekci kurzu. S `--pause` zůstane
   formulář otevřený pro kontrolu. Moodle může přepnout režim úprav i načíst
   editor asynchronně nebo pomalu načítat části kurzu; skript čeká na
   zobrazení konkrétních ovládacích prvků místo čekání na úplné načtení
   formuláře VPL. Počká na
   inicializaci JavaScriptového přepínače
   před kliknutím, až 90 sekund na potvrzení režimu a až 60 sekund na další
   prvky stránky. Běh vypisuje časované kroky; pokud se nepodaří najít sekci,
   zobrazí také URL a názvy sekcí nalezené v kurzu. Pokud se v dialogu
   výběru aktivity neaktivuje tlačítko „Přidat“, vypíše stav volby VPL,
   tlačítek a případných zaškrtávacích polí.
5. Po kontrole formulář uložte výslovným spuštěním s `--save`; skript použije
   tlačítko „Uložit a zobrazit“ a ověří, že se aktivita zobrazuje v cílové
   sekci. Pokud úkol obsahuje právě jeden soubor `*.cases`, nahraje jeho obsah
   do „Tests configuration“. Ostatní soubory `vpl_*` (například
   `vpl_evaluate.py`, `vpl_evaluate.sh` nebo `vpl_run.sh`) nahraje do
   „Execution files“ u běžných i známkovaných úkolů. V „Execution options“
   nastaví Run a Evaluate na Ano. V „Requested files“ vytvoří soubor uvedený
   v `soubor` v `ukol.yaml`, nebo `main.py`, pokud položka není uvedena.
   Požadované Python soubory začínají komentářem `# Zde napište svůj kód`.
   Například:

   ```bash
   python scripts/moodle_e2e.py --class 2I --lesson 8 --task 1 --save
   python scripts/moodle_e2e.py --class 2I --lesson 2 --task Z01 --save
   ```

## Stažení odevzdání

Skript `scripts/moodle_download_submissions.py` stáhne odevzdání VPL aktivity
bez změn v Moodle. Přihlásí se do kurzu a aktivity podle třídy, lekce a čísla
úkolu, otevře „Submissions list“ a v nabídce tří teček zvolí
„Download submissions“. Stažený archiv i ZIP archivy odevzdané uvnitř
studentských složek rozbalí do `řešení/<třída> - Lekce NN - <název úkolu>`.
Rozbalené vnořené ZIP soubory smaže. Existující cílovou složku nepřepisuje.

```bash
python scripts/moodle_download_submissions.py --class 2IM --lesson 7 --task Z02
python scripts/moodle_download_submissions.py --class 3I --lesson 5 --task 1
```

Použijte `Z01` pro známkovaný úkol a běžné číslo (např. `1`) pro ostatní.
Při použití školního SSO dokončete přihlášení v otevřeném okně Chromium.
Skript počká na načtení seznamu odevzdání, klikne na nabídku `#action-menu-toggle-1`
a počká, až se zobrazí volba ke stažení.
Výsledky zůstávají lokální v ignorované složce `řešení/`. Pokud cílová složka
již existuje, nejprve ji ručně přejmenujte nebo přesuňte.

## 1. ročník — stdin / stdout (`vpl_evaluate.cases`)

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

Bonus **CSV, JSON a XML** (`lekce/bonus/05-csv-json-xml`) používá stejný typ VPL (`vpl_evaluate.cases`) jako 1. ročník. Testovací soubor nemusí být `data.txt` — název je v zadání (`zaci.csv`, `knihy.json`, `knihy.xml`).

### Založení aktivity

1. Přidejte aktivitu **Virtual programming lab**.
2. Jazyk: **Python 3**.
3. Požadovaný soubor od studenta: `main.py` (nebo dle zadání).
4. Zapněte **Automatic evaluation**.
5. V menu aktivity: **Execution options → Files** (soubory ke spuštění):
   - vložte obsah `vpl_evaluate.cases` ze složky úkolu,
   - pokud existuje `data.txt`, přidejte ho také (Execution files).
6. V **Test cases** vložte stejný obsah `vpl_evaluate.cases` (nebo jen v Execution files — dle verze VPL).
7. Zkratka názvu: kód z `ukoly.md`, např. `PRG-1-09-01`.

### Formát vpl_evaluate.cases (BIOTES)

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

2. ročník používá stejný typ VPL jako 1. ročník: **jeden úkol = jedna aktivita**, soubor `main.py`, testy v `ukoly/NN-slug/vpl_evaluate.cases`. Výjimka jsou lekce **12** a **13** (a pololetní projekt v lekci 11): automatický test nemají, žák odevzdá textový dokument a hodnotí učitel.

Úkol **Vitrína** v lekci 04 (`PRG-2-04-05`, `typ: oop`) cases nepoužívá. Do **Execution files** vložte `vpl_evaluate.sh` a `vpl_evaluate.py`. Test hlídá výpis a zároveň třídy, konstruktory a složení. Bez správné struktury je známka 0, i kdyby text na výstupu seděl. Když struktura sedí, body se dělí podle jednotlivých vstupů.

Lekce **12** a **13** mají v `ukol.yaml` `typ: soubor` a pole `odevzdani`. Do AMOS se nahrává TXT, PDF nebo DOCX s odpovědí nebo tabulkou.

## 2. ročník od lekce 14 — SQL (`vpl_evaluate.py` + `vpl_evaluate.sh`)

Žák odevzdá `reseni.sql`. Generátor z `ukol.yaml` (`typ: sql`) sestaví hodnotitel, který skript pustí v **nové** SQLite databázi v paměti a zkontroluje tabulky, typy sloupců, `NOT NULL`, `UNIQUE`, primární a cizí klíč.

```
lekce/2-rocnik/NN-nazev/ukoly/01-slug/
  ukol.yaml
  vpl_run.sh         ← generované, tlačítko Run
  vpl_evaluate.py    ← generované
  vpl_evaluate.sh    ← generované, tlačítko Evaluate
```

Jail nic dalšího nepotřebuje. Modul `sqlite3` je součást Pythonu.

Příkaz `sqlite3 reseni.sql` **nepoužívejte**. SQLite ten argument bere jako soubor databáze, otevře konzoli a čeká na další příkazy. Skript se nespustí a hodnocení se nedostane ke slovu. `vpl_run.sh` i `vpl_evaluate.sh` pouští SQL z Pythonu a hned skončí.

### Založení aktivity

1. Přidejte aktivitu **Virtual programming lab**.
2. Jazyk: **Python 3**. Jazyk SQL / SQLite nechte být — ten spouští konzoli.
3. Požadovaný soubor od studenta: `reseni.sql`.
4. Zapněte **Automatic evaluation**.
5. Do **Execution files** vložte tři generované soubory:
   - `vpl_run.sh`
   - `vpl_evaluate.sh`
   - `vpl_evaluate.py`
6. `vpl_run.sh` je skript pro **Run**, `vpl_evaluate.sh` pro **Evaluate**. `reseni.sql` mezi soubory ke spuštění nepatří — ten odevzdává žák.
7. Zkratka názvu: kód z `ukoly.md`, např. `PRG-2-15-01`.

## 3. ročník — Flask (`vpl_evaluate.py` + `vpl_evaluate.sh`)

Úkoly ve Flasku nečtou stdin. Generátor z `ukol.yaml` (`typ: flask`) vytvoří **validační skripty**, které aplikaci načtou a přes testovací klient ověří routy a HTML značky (ne přesný text na stránce).

```
lekce/3-rocnik/NN-nazev/ukoly/01-slug/
  ukol.yaml
  vpl_evaluate.py    ← generované
  vpl_evaluate.sh    ← generované
```

Lekce **01** (záložka Síť) zůstává odevzdání **souboru** (snímek / výpis) — bez VPL.

### Prostředí jailu

V automatickém hodnocení musí být nainstalovaný **Flask** (stejně jako ho žáci mají lokálně):

```bash
python3 -m pip install flask
```

Bez toho skript napíše, že Flask v jailu chybí, a dá 0 bodů. **SQLite** (`sqlite3`) je v Pythonu — u lekcí 16–20 a 22 další balíček není potřeba.

Bonusová lekce **ORM** (`lekce/bonus/04-orm`) potřebuje v jailu navíc **Flask-SQLAlchemy**:

```bash
python3 -m pip install flask-sqlalchemy
```

### Založení aktivity

1. Přidejte aktivitu **Virtual programming lab**.
2. Jazyk: **Python 3**.
3. Požadovaný soubor od studenta: přesně název z zadání (`plakat.py`, `krouzek.py`, …).
4. Zapněte **Automatic evaluation**.
5. Do **Execution files** vložte oba generované soubory:
   - `vpl_evaluate.sh`
   - `vpl_evaluate.py`
6. Označte je jako soubory **ke spuštění / hodnocení**, ne jako odevzdání žáka.
7. Zkratka názvu: kód z `ukoly.md`, např. `PRG-3-04-01`.

Skript hodnotí strukturu (stav 200, značky `h1`/`p`/`ul`, odkazy `href`). Od lekce **11** umí i **POST** (`post:` a `data:`). Od lekce **13** i přesměrování (`status: 302`, `location:`, `follow_redirects:`). Od lekce **14** i nahrání souboru (`upload:` a `saved:`). Od lekce **15** i relaci (`then:` na stejném klientovi, `other_get:` na čistém). Od lekce **16** i SQLite (`db:`, `db_tables:`, `db_min_rows:`). Bonusové ORM kontroluje v kódu `flask_sqlalchemy`, ne `sqlite3`. Vlastní text (název kroužku, jídlo, tituly knih) je v pořádku.

U úkolů se **šablonami** (od lekce 05) nahrajte i složku `templates/` (`index.html`, …). Od lekce **07** i složku `static/` (CSS, SVG). V `ukol.yaml` to hodnotitel kontroluje. Když Moodle soubory zploští do jedné složky, hodnotitel hledá soubory i vedle `.py`.

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
- **Úkoly** — samostatná práce, odevzdání a bodování přes VPL v Moodle (1. a 2. ročník stdin, 3. ročník Flask), nebo soubor u úkolů bez automatického testu.
