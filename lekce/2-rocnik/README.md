# 2. ročník — lekce

**Objektové programování a SQL** — 170 hodin (34 týdnů × 5 h)

Kompletní osnova: [`kurikulum/2-rocnik.yaml`](../../kurikulum/2-rocnik.yaml)

Předpoklady z 1. ročníku: **strukturované programování v Pythonu** (funkce, kolekce, soubory). SQL a OOP se učí zde. Ve 3. ročníku se SQL neučí znovu — Flask ho jen napojí.

**Tkinter / GUI se neučí.** Algoritmizace je SŠ základ ve dvou lekcích po 10 h (blízko ŠVP 21 h). Těžiště ročníku je **SQL**.

Každá lekce = vlastní složka (stejná struktura jako 1. ročník).

Úvod na rozcestníku: `uvod.md` (žáci vidí na `index.html`).

Šablony: `sablony/`

## Přehled lekcí

| # | ID | Téma | Hodiny | Úkoly |
|---|-----|------|--------|-------|
| 01 | `01-rekurze` | Rekurze — základ | 10 | 5 |
| 02 | `02-vyhledavani-a-razeni` | Vyhledávání a řazení — základ | 10 | 5 ★ |
| 03 | `03-tridy-a-objekty` | Třídy, objekty a atributy | 5 | 3 |
| 04 | `04-konstruktor` | Konstruktor | 4 | 5 ★ |
| 05 | `05-metody` | Metody a self | 3 | 3 |
| 06 | `06-specialni-metody` | Speciální metody | 3 | 4 |
| 07 | `07-tridy-procviceni` | Třídy — souhrn a procvičení | 5 | 5 ★ |
| 08 | `08-dedicnost` | Dědičnost | 5 | 3 |
| 09 | `09-polymorfismus` | Polymorfismus | 3 | 3 ★ |
| 10 | `10-staticke-metody-a-promenne` | Statické metody a proměnné | 3 | 3 |
| 11 | `11-moduly-a-soubory` | Moduly a třídy ve více souborech | 3 | 4 |
| 12 | `12-vlastnosti` | Vlastnosti a @property | 5 | 4 |
| 13 | `13-dataclasses` | Dataclasses | 5 | 4 |
| 14 | `14-vyjimky-a-iterace` | Vlastní výjimky a iterace | 3 | 3 |
| 15 | `15-oop-navrh-a-pololetni-projekt` | OOP — návrh a pololetní projekt | 18 | 1 |
| 16 | `16-relacni-databaze` | Principy relační databáze | 3 | 3 |
| 17 | `17-sql-a-sqlite` | Koncepce jazyka SQL a SQLite | 3 | 2 |
| 18 | `18-create-table` | Definování tabulek (CREATE TABLE) | 3 | 3 |
| 19 | `19-select-zaklady` | SELECT — základy | 3 | 3 |
| 20 | `20-select-where` | SELECT — WHERE | 3 | — |
| 21 | `21-select-razeni` | SELECT — řazení, LIMIT a NULL | 3 | — |
| 22 | `22-join-a-relace` | JOIN a relace 1:N | 3 | — |
| 23 | `23-agregace` | Agregační funkce | 3 | — |
| 24 | `24-group-by` | GROUP BY, HAVING a složitější dotazy | 3 | — |
| 25 | `25-insert` | INSERT | 3 | — |
| 26 | `26-update-delete` | UPDATE a DELETE | 5 | — |
| 27 | `27-transakce-a-bezpecnost` | Transakce, integrita, DCL a výkon | 5 | — |
| 28 | `28-sqlite3-select` | sqlite3 — připojení a SELECT | 5 | — |
| 29 | `29-sqlite3-dml` | sqlite3 — zápis a parametrizované dotazy | 5 | — |
| 30 | `30-konzolova-crud` | Konzolová CRUD aplikace | 5 | — |
| 31 | `31-sql-aplikace-procviceni` | SQL v aplikaci — souhrn a procvičení | 5 | — |
| 32 | `32-projekt` | Projekt — zadání a práce | 20 | — |
| 33 | `33-projekt-prezentace` | Projekt — odevzdání a prezentace | 5 | — |

★ lekce končí známkovaným úkolem s tajným zadáním (hodnotí učitel, zadání není v materiálu).

**Celkem: 33 lekcí v 170 h.** Lekce 01 a 02 po 10 h. Lekce 05, 06, 09–11 a 14 mají 3 h. Nové OOP lekce 11–13 a lekce 15 završují první pololetí v 85 h; pololetní projekt má 18 h. SQL je zkráceno na 50 h, aplikované programování zůstává 35 h. Závěrečný projekt (lekce 32–33) trvá 25 h.

## Moduly (ŠVP)

| Modul | ŠVP | Osnova | Lekce |
|-------|-----|--------|-------|
| Algoritmizace | 21 h | **20 h** | 01–02 |
| Úvod do objektového programování | 47 h | **65 h** | 03–15 |
| Základy jazyka SQL | 51 h | **50 h** | 16–29 |
| Aplikované programování | 51 h | **35 h** (bez GUI) | 30–33 |
