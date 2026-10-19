# Cvičení — Statické metody a proměnné

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Proměnnou třídy zapisujte **jménem třídy**, ne přes `self`.

## Cvičení 1 — Jednotka (★☆☆)

Třída `Obdelnik` má u třídy `jednotka = "cm"` a v konstruktoru strany `a`, `b`. Vypište `Obdelnik.jednotka`.

Ověření: výstup je `cm`. Objekt vytvořit nemusíte.

@reseni
```python
class Obdelnik:
    jednotka = "cm"

    def __init__(self, a, b):
        self.a = a
        self.b = b


print(Obdelnik.jednotka)
```
@end

---

## Cvičení 2 — Objednávky (★★☆)

Třída `Objednavka` má u třídy `pocet = 0`. V konstruktoru nastavte `cislo` a přičtěte jedničku k `Objednavka.pocet`. Vytvořte dvě objednávky a vypište `Objednavka.pocet`.

Ověření: výstup je `2`.

@reseni
```python
class Objednavka:
    pocet = 0

    def __init__(self, cislo):
        self.cislo = cislo
        Objednavka.pocet = Objednavka.pocet + 1


Objednavka(1)
Objednavka(2)
print(Objednavka.pocet)
```
@end

---

## Cvičení 3 — Počítadlo u objektu (★☆☆)

Proč je `Clen.pocet` pořád `0`? Opravte konstruktor tak, aby po dvou členech vypsal `2`.

```python
class Clen:
    pocet = 0

    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pocet = self.pocet + 1


Clen("Eva")
Clen("Karel")
print(Clen.pocet)
```

@reseni
`self.pocet = ...` uloží jedničku **jen do toho objektu**. Třída zůstane na nule. Přičítejte u třídy:

```python
class Clen:
    pocet = 0

    def __init__(self, jmeno):
        self.jmeno = jmeno
        Clen.pocet = Clen.pocet + 1


Clen("Eva")
Clen("Karel")
print(Clen.pocet)  # 2
```
@end

---

## Cvičení 4 — Metr na centimetry (★★☆)

Třída `Delka` se **statickou** metodou `m_na_cm(metry)`, která vrátí `metry * 100`. Objekt nevytvářejte. Vypište `Delka.m_na_cm(3)`.

Ověření: výstup je `300`. Nad metodou musí být `@staticmethod`.

@reseni
```python
class Delka:
    @staticmethod
    def m_na_cm(metry):
        return metry * 100


print(Delka.m_na_cm(3))
```
@end
