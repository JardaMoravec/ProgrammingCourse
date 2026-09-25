# Cvičení — Definování tabulek (CREATE TABLE)

Cvičení jsou na hodinu, řešení je schované. Úkoly do AMOS mají jiná zadání a odevzdávají se jako `reseni.sql`.

## Cvičení 1 — Knihy (★☆☆)

Napište `CREATE TABLE` pro tabulku `knihy`:

- `id` — celé číslo, primární klíč
- `nazev` — text, povinný
- `rok` — celé číslo

@reseni
```sql
CREATE TABLE knihy (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    rok INTEGER
);
```
@end

---

## Cvičení 2 — Účty (★★☆)

Tabulka `ucty`. E-mail musí být vyplněný a v tabulce jen jednou. Heslo do tabulky nepište.

- `id` — primární klíč
- `email` — text, povinný a jedinečný
- `jmeno` — text, povinné

@reseni
```sql
CREATE TABLE ucty (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    jmeno TEXT NOT NULL
);
```
@end

---

## Cvičení 3 — Autoři a knihy (★★☆)

Dvě tabulky. Jeden autor má víc knih, kniha odkazuje na autora.

**autori:** `id` (primární klíč), `jmeno` (povinný text)

**knihy:** `id` (primární klíč), `nazev` (povinný text), `autor_id` (cizí klíč na `autori.id`)

@reseni
```sql
CREATE TABLE autori (
    id INTEGER PRIMARY KEY,
    jmeno TEXT NOT NULL
);

CREATE TABLE knihy (
    id INTEGER PRIMARY KEY,
    nazev TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autori (id)
);
```

`autori` musí být v souboru **nad** `knihy`.
@end
