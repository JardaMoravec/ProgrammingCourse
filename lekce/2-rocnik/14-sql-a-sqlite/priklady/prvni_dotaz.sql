-- První SQL: tabulka, dva řádky, výpis sloupce.
-- Nový soubor (když knihy.db už existuje, smažte ho a spusťte znovu):
--   sqlite3 knihy.db < prvni_dotaz.sql

CREATE TABLE knihy (
    id INTEGER PRIMARY KEY,
    nazev TEXT
);

INSERT INTO knihy (id, nazev) VALUES (1, 'R.U.R.');
INSERT INTO knihy (id, nazev) VALUES (2, 'Krakatit');

SELECT nazev FROM knihy;
