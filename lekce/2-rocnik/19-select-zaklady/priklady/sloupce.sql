CREATE TABLE knihy (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    rok INTEGER
);

INSERT INTO knihy (id, nazev, rok) VALUES (1, 'R.U.R.', 1920);
INSERT INTO knihy (id, nazev, rok) VALUES (2, 'Krakatit', 1924);

SELECT rok, nazev FROM knihy;
