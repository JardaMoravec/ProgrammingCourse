# Cvičení — SELECT — základy

Ukázkové tabulky si v sqlite3 založte a naplňte. Odevzdává se jen dotaz `SELECT`.

## 1. Názvy filmů ★

```sql
CREATE TABLE filmy (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    rok INTEGER
);

INSERT INTO filmy (id, nazev, rok) VALUES (1, 'Kolja', 1996);
INSERT INTO filmy (id, nazev, rok) VALUES (2, 'Pelisky', 1999);
```

Vypište jen názvy filmů.

@reseni
```sql
SELECT nazev FROM filmy;
```
@end

## 2. Trasa a cena ★★

```sql
CREATE TABLE jizdenky (
    id INTEGER PRIMARY KEY,
    trasa TEXT NOT NULL,
    cena INTEGER NOT NULL
);

INSERT INTO jizdenky (id, trasa, cena) VALUES (1, 'Brno-Praha', 220);
INSERT INTO jizdenky (id, trasa, cena) VALUES (2, 'Brno-Olomouc', 90);
```

Vypište trasu a cenu. Ve výsledku je nejdřív trasa.

@reseni
```sql
SELECT trasa, cena FROM jizdenky;
```
@end

## 3. Město jednou ★★

```sql
CREATE TABLE zamestnanci (
    id INTEGER PRIMARY KEY,
    jmeno TEXT NOT NULL,
    mesto TEXT NOT NULL
);

INSERT INTO zamestnanci (id, jmeno, mesto) VALUES (1, 'Eva', 'Brno');
INSERT INTO zamestnanci (id, jmeno, mesto) VALUES (2, 'Karel', 'Praha');
INSERT INTO zamestnanci (id, jmeno, mesto) VALUES (3, 'Anna', 'Brno');
```

Vypište města tak, aby se žádné neopakovalo.

@reseni
```sql
SELECT DISTINCT mesto FROM zamestnanci;
```
@end
