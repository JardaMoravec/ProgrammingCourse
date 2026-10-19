# Cvičení — Principy relační databáze

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. SQL ani Python **nepište** — stačí text a tabulky na papír.

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

## Cvičení 4 — Řádek podle klíče (★☆☆)

Tabulka `filmy`:

| id | nazev |
|----|-------|
| 1 | Matrix |
| 2 | Amelie |
| 3 | Avatar |

1. Který název patří k `id` 3?
2. Co zapíšete, když hledáte `id` 9?
3. Proč na to nestačí hledat podle sloupce `nazev`?

@reseni
1. Avatar
2. Takový řádek v tabulce není.
3. Název se může opakovat. `id` je primární klíč, takže určí nejvýš jeden řádek.
@end

---

## Cvičení 5 — Alba jednoho interpreta (★★☆)

Vztah **1:N**. Do sešitu vypište názvy alb interpreta s `id` 1. Album jiného interpreta tam nepatří.

**interpreti**

| id | jmeno |
|----|-------|
| 1 | Chinaski |
| 2 | Kabát |

**alba**

| id | nazev | interpret_id |
|----|-------|--------------|
| 1 | Premium 2003 | 1 |
| 2 | Dole v dole | 2 |
| 3 | Originál | 1 |

@reseni
Premium 2003  
Originál

*Dole v dole* má `interpret_id` 2, takže patří Kabátu. Seznam interpretů k výpisu nepotřebujete — cizí klíč už říká, která alba patří jedničce.
@end
