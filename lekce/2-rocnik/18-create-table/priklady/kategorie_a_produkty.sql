-- Dvě tabulky a cizí klíč.
-- sqlite3 obchod.db < kategorie_a_produkty.sql

CREATE TABLE kategorie (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL
);

CREATE TABLE produkty (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    kategorie_id INTEGER,
    FOREIGN KEY (kategorie_id) REFERENCES kategorie (id)
);
