-- Tabulka produktů: klíč, povinný text, cena.
-- sqlite3 produkty.db < produkty.sql

CREATE TABLE produkty (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    cena REAL
);
