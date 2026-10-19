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
| 06 | `06-specialni-metody` | Speciální metody | 3 | 2 |
| 07 | `07-tridy-procviceni` | Třídy — souhrn a procvičení | 5 | 5 ★ |
| 08 | `08-dedicnost` | Dědičnost | 5 | 3 |
| 09 | `09-polymorfismus` | Polymorfismus | 3 | 3 ★ |
| 10 | `10-staticke-cleny` | Statické metody a proměnné | 5 | 3 |
| 11 | `11-vyjimky-a-iterace` | Vlastní výjimky a iterace | 3 | 3 |
| 12 | `12-oop-navrh-a-procviceni` | OOP — návrh a pololetní projekt | 9 | 1 |
| 13 | `13-relacni-databaze` | Principy relační databáze | 5 | 3 |
| 14 | `14-sql-a-sqlite` | Koncepce jazyka SQL a SQLite | 5 | 2 |
| 15 | `15-create-table` | Definování tabulek (CREATE TABLE) | 5 | 3 |
| 16 | `16-select-zaklady` | SELECT — základy | 5 | 3 |
| 17 | `17-select-where` | SELECT — WHERE | 5 | — |
| 18 | `18-select-razeni` | SELECT — řazení, LIMIT a NULL | 5 | — |
| 19 | `19-join-a-relace` | JOIN a relace 1:N | 5 | — |
| 20 | `20-agregace` | Agregační funkce | 5 | — |
| 21 | `21-group-by` | GROUP BY, HAVING a složitější dotazy | 5 | — |
| 22 | `22-insert` | INSERT | 5 | — |
| 23 | `23-update-delete` | UPDATE a DELETE | 5 | — |
| 24 | `24-transakce-a-bezpecnost` | Transakce, integrita, DCL a výkon | 5 | — |
| 25 | `25-sqlite3-select` | sqlite3 — připojení a SELECT | 5 | — |
| 26 | `26-sqlite3-dml` | sqlite3 — zápis a parametrizované dotazy | 5 | — |
| 27 | `27-konzolova-crud` | Konzolová CRUD aplikace | 5 | — |
| 28 | `28-sql-aplikace-procviceni` | SQL v aplikaci — souhrn a procvičení | 5 | — |
| 29 | `29-projekt` | Projekt — zadání a práce | 20 | — |
| 30 | `30-projekt-prezentace` | Projekt — odevzdání a prezentace | 5 | — |

★ lekce končí známkovaným úkolem s tajným zadáním (hodnotí učitel, zadání není v materiálu).

**Celkem: 30 lekcí v 170 h.** Lekce 01 a 02 po 10 h (dva týdny). Lekce 04 má 4 h, lekce 05 a 06 po 3 h — uvolněných 5 h je lekce **07** (souhrn tříd). Lekce 09 a 11 po 3 h — uvolněné 4 h jdou do lekce **12** (9 h, pololetní projekt). Ostatní běžné lekce po 5 h. Lekce 29 trvá 4 týdny, lekce 30 jeden týden.

## Moduly (ŠVP)

| Modul | ŠVP | Osnova | Lekce |
|-------|-----|--------|-------|
| Algoritmizace | 21 h | **20 h** | 01–02 |
| Úvod do objektového programování | 47 h | 45 h | 03–12 |
| Základy jazyka SQL | 51 h | **70 h** | 13–26 |
| Aplikované programování | 51 h | **35 h** (bez GUI) | 27–30 |
