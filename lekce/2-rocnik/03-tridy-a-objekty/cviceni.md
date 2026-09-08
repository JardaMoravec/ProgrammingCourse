# Cvičení — Třídy, objekty a atributy

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Zatím **bez** `__init__` a bez vlastních metod — atributy nastavte tečkou.

## Cvičení 1 — Auto (★☆☆)

Třída `Auto`. Nastavte `znacka` a `barva`. Vypište větu ve tvaru `Skoda, barva modra`.

Ověření: pro značku `Skoda` a barvu `modra` je výstup přesně ta věta.

@reseni
```python
class Auto:
    pass


a = Auto()
a.znacka = "Skoda"
a.barva = "modra"
print(f"{a.znacka}, barva {a.barva}")
```
@end

---

## Cvičení 2 — Dva filmy (★★☆)

Třída `Film` s atributy `nazev` a `rok`. Vytvořte **dva** objekty. U prvního změňte rok. Druhý se nesmí změnit.

Ověření: po změně prvního na `2010` má druhý pořád `1994`.

@reseni
```python
class Film:
    pass


prvni = Film()
prvni.nazev = "Forrest Gump"
prvni.rok = 1994

druhy = Film()
druhy.nazev = "Pulp Fiction"
druhy.rok = 1994

prvni.rok = 2010
print(prvni.rok)  # 2010
print(druhy.rok)  # 1994
```
@end

---

## Cvičení 3 — AttributeError (★☆☆)

Spusťte kód. Proč spadne? Opravte ho tak, aby vypsal `Eva`.

```python
class Osoba:
    pass


a = Osoba()
a.jmeno = "Karel"
b = Osoba()
print(b.jmeno)
```

@reseni
Objekt `b` je jiná instance. Atribut `jmeno` má jen `a`. Než ho čtete u `b`, musíte ho nastavit:

```python
class Osoba:
    pass


a = Osoba()
a.jmeno = "Karel"
b = Osoba()
b.jmeno = "Eva"
print(b.jmeno)  # Eva
```
@end

---

## Cvičení 4 — Koníčky (★★☆)

Třída `Clovek`. Atribut `jmeno` a atribut `konicky` (seznam řetězců, na začátku prázdný). Přidejte dva koníčky přes `append` a vypište, kolik jich je.

Ověření: po `cteni` a `beh` je `len(c.konicky)` rovno `2`.

@reseni
```python
class Clovek:
    pass


c = Clovek()
c.jmeno = "Anna"
c.konicky = []
c.konicky.append("cteni")
c.konicky.append("beh")
print(len(c.konicky))  # 2
```
@end
