CREATE TABLE zamestnanci (
    id INTEGER PRIMARY KEY,
    jmeno TEXT NOT NULL,
    mesto TEXT NOT NULL
);

INSERT INTO zamestnanci (id, jmeno, mesto) VALUES (1, 'Eva', 'Brno');
INSERT INTO zamestnanci (id, jmeno, mesto) VALUES (2, 'Karel', 'Praha');
INSERT INTO zamestnanci (id, jmeno, mesto) VALUES (3, 'Anna', 'Brno');

SELECT DISTINCT mesto FROM zamestnanci;
