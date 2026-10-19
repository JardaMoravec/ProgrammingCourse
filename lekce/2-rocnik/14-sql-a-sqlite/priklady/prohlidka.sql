-- Až po prvni_dotaz.sql, na stejný soubor knihy.db.
-- Tečkové příkazy fungují v programu sqlite3, ne v DB Browseru.
--   sqlite3 knihy.db < prohlidka.sql

.headers on
.mode column
.tables
.schema knihy
SELECT * FROM knihy;
