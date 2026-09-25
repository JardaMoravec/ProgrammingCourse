# Cvičení — Koncepce jazyka SQL a SQLite

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Odpovědi pište jako text. Databázi nespouštějte a do Pythonu SQL nevkládejte.

## Cvičení 1 — Rodina (★☆☆)

Ke každému příkazu napište rodinu: **DDL**, **DQL**, **DML**, **DCL**, nebo **TCL**.

1. `CREATE TABLE zaci (id INTEGER PRIMARY KEY, jmeno TEXT);`
2. `SELECT jmeno FROM zaci;`
3. `INSERT INTO zaci (id, jmeno) VALUES (1, 'Anna');`
4. `DELETE FROM zaci;`
5. `DROP TABLE zaci;`
6. `GRANT SELECT ON zaci TO ucitel;`
7. `BEGIN;`

@reseni
1. DDL
2. DQL
3. DML
4. DML — maže řádky, tabulka zůstane
5. DDL — maže tabulku
6. DCL
7. TCL
@end

---

## Cvičení 2 — Soubor, nebo server? (★☆☆)

U každé věty napište **ano**, nebo **ne**.

1. SQLite potřebuje běžící server a heslo.
2. Soubor `knihy.db` je u SQLite celá databáze.
3. Základní `SELECT` v SQLite a v PostgreSQL je tentýž druh příkazu.
4. `GRANT` v SQLite založí uživatele databáze.
5. Příkaz `.tables` je SQL a půjde spustit i v PostgreSQL.

@reseni
1. ne — SQLite je soubor, bez serveru a bez účtu
2. ano
3. ano — drobnosti dialektu přijdou později, `SELECT` jako čtení je společný
4. ne — DCL patří k serveru; SQLite hlídá oprávnění k souboru
5. ne — tečka je příkaz nástroje `sqlite3`
@end

---

## Cvičení 3 — Tři věty pro města (★★☆)

Na papír napište SQL pro tabulku `mesta`:

- sloupce `id` (primární klíč, `INTEGER`) a `nazev` (`TEXT`)
- řádek `id` 1, název `Praha`
- řádek `id` 2, název `Brno`
- výpis všech názvů

U každé věty napište rodinu. Středník na konci věty.

@reseni
```sql
CREATE TABLE mesta (
    id INTEGER PRIMARY KEY,
    nazev TEXT
);

INSERT INTO mesta (id, nazev) VALUES (1, 'Praha');
INSERT INTO mesta (id, nazev) VALUES (2, 'Brno');

SELECT nazev FROM mesta;
```

`CREATE TABLE` je DDL, `INSERT` je DML, `SELECT` je DQL. Výpis názvů by byly řádky `Praha` a `Brno`.
@end

---

## Cvičení 4 — Co by skript vypsal (★☆☆)

Skript z lekce nespouštějte. Přečtěte ho a odpovězte slovy.

```sql
CREATE TABLE knihy (
    id INTEGER PRIMARY KEY,
    nazev TEXT
);

INSERT INTO knihy (id, nazev) VALUES (1, 'R.U.R.');
INSERT INTO knihy (id, nazev) VALUES (2, 'Krakatit');

SELECT nazev FROM knihy;
```

1. Jak se jmenuje tabulka a které má sloupce?
2. Co vypíše poslední příkaz? Napište řádky pod sebe.
3. Co vypíše `.tables`, když skript doběhne v programu `sqlite3`?
4. Proč druhé spuštění téhož skriptu na stejném souboru spadne na `CREATE TABLE`?

@reseni
1. Tabulka `knihy`, sloupce `id` a `nazev`.
2. `R.U.R.` a `Krakatit`.
3. `knihy`
4. Tabulka už v souboru je. `CREATE TABLE` ji založí jen jednou.
@end

---

## Cvičení 5 — Přepis z okna sqlite3 (★★☆)

Někdo nechal v nástroji tento přepis. U každého řádku napište **SQL**, nebo **nástroj**.

```text
sqlite> .tables
knihy
sqlite> SELECT nazev FROM knihy;
R.U.R.
Krakatit
sqlite> .schema knihy
sqlite> DROP TABLE knihy;
sqlite> .quit
```

Který řádek tabulku **smaže**? Zůstane po něm v souboru tabulka `knihy`?

@reseni
- `.tables` — nástroj
- `SELECT …` — SQL (DQL)
- `.schema knihy` — nástroj
- `DROP TABLE knihy;` — SQL (DDL); tento řádek tabulku smaže
- `.quit` — nástroj

Po `DROP TABLE` tabulka `knihy` v souboru **není**. `.quit` už jen zavře nástroj.
@end
