# Cvičení — Principy relační databáze

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. SQL zatím **nepište** — stačí tabulky na papír a v Pythonu seznam slovníků, který už znáte z 1. ročníku.

## Cvičení 1 — Primární klíč (★☆☆)

Tabulka `zaci`:

| id | jmeno | email | trida |
|----|-------|-------|-------|
| 1 | Anna | anna@skola.cz | 1.A |
| 2 | Boris | boris@skola.cz | 1.A |
| 3 | Cyril | cyril@skola.cz | 1.B |

1. Který sloupec je vhodný **primární klíč**? Proč ne `jmeno` a proč ne `email`?
2. Přibude žák se stejným e-mailem jako Anna. Co se stane, když e-mail **není** klíč? Co by se stalo, kdyby byl?

@reseni
1. `id`. Jméno se opakuje (dvě Anny). E-mail bývá jedinečný, ale žák ho může změnit; `id` se nemění.
2. Bez klíče na e-mailu databáze duplicitu **nechá** — dva řádky, stejný e-mail. Kdyby e-mail byl primární klíč, druhý řádek **neprojde**.
@end

---

## Cvičení 2 — Návrh 1:N (★★☆)

Obchod eviduje **zákazníky** a **objednávky**. Jeden zákazník má víc objednávek, objednávka patří jednomu zákazníkovi.

Na papír nakreslete **dvě** tabulky: sloupce, primární klíče a cizí klíč. Do každé dejte dva ukázkové řádky, ať je vidět odkaz.

@reseni
**zakaznici:** `id` (PK), `jmeno`  
**objednavky:** `id` (PK), `cislo`, `zakaznik_id` (FK → `zakaznici.id`)

| id | jmeno |
|----|-------|
| 1 | Novák |
| 2 | Svobodová |

| id | cislo | zakaznik_id |
|----|-------|-------------|
| 1 | A100 | 1 |
| 2 | A101 | 1 |
| 3 | A200 | 2 |

Jméno zákazníka u objednávky **není** — bylo by to opakování. Spojení tabulek je až u `JOIN`.
@end

---

## Cvičení 3 — Relační, nebo objektová? (★☆☆)

U každé věty napište **ano**, nebo **ne**.

1. SQLite, kterou použijete v další lekci, je **relační** databáze.
2. Objektová databáze ukládá objekty a odkazy mezi nimi, ne nutně tabulky.
3. Když v Pythonu máte třídu `Kniha` a ukládáte do SQLite, používáte objektovou databázi.
4. Excel s tabulkou knih je totéž co databáze: hlídá primární klíč a cizí klíč.

@reseni
1. ano
2. ano
3. ne — třídy jsou v programu; SQLite je relační. Schovat SQL za objekty umí ORM, to ale **není** objektová databáze.
4. ne — chybí vynucené klíče, integrita a SQL
@end

---

## Cvičení 4 — Hledání podle klíče (★☆☆)

Tabulka filmů v paměti. Najděte film s `id` `3` a vypište název.

```python
filmy = [
    {"id": 1, "nazev": "Matrix"},
    {"id": 2, "nazev": "Amelie"},
    {"id": 3, "nazev": "Avatar"},
]
hledane_id = 3
```

Ověření: výstup je `Avatar`. Když `hledane_id` změníte na `9`, má se vypsat `Nenalezeno`.

@reseni
```python
filmy = [
    {"id": 1, "nazev": "Matrix"},
    {"id": 2, "nazev": "Amelie"},
    {"id": 3, "nazev": "Avatar"},
]
hledane_id = 3
nalezeno = None
for f in filmy:
    if f["id"] == hledane_id:
        nalezeno = f
        break

if nalezeno is None:
    print("Nenalezeno")
else:
    print(nalezeno["nazev"])
```
@end

---

## Cvičení 5 — Dvě tabulky (★★☆)

Interpret a alba — vztah **1:N**. Vypište názvy **všech** alb interpreta s `id` `1`, každé na vlastní řádek, v pořadí v seznamu.

```python
interpreti = [
    {"id": 1, "jmeno": "Chinaski"},
    {"id": 2, "jmeno": "Kabát"},
]
alba = [
    {"id": 1, "nazev": "Premium 2003", "interpret_id": 1},
    {"id": 2, "nazev": "Dole v dole", "interpret_id": 2},
    {"id": 3, "nazev": "Originál", "interpret_id": 1},
]
```

Ověření: dva řádky `Premium 2003` a `Originál`. Album *Dole v dole* se vypsat nesmí.

@reseni
```python
interpreti = [
    {"id": 1, "jmeno": "Chinaski"},
    {"id": 2, "jmeno": "Kabát"},
]
alba = [
    {"id": 1, "nazev": "Premium 2003", "interpret_id": 1},
    {"id": 2, "nazev": "Dole v dole", "interpret_id": 2},
    {"id": 3, "nazev": "Originál", "interpret_id": 1},
]

for a in alba:
    if a["interpret_id"] == 1:
        print(a["nazev"])
```

Seznam `interpreti` tady k výpisu nepotřebujete — `interpret_id` už říká, která alba patří jedničce. V databázi by totéž hlídal cizí klíč.
@end
