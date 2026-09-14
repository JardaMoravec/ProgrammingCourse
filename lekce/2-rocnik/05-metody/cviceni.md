# Cvičení — Metody a self

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. `__str__` nepište — stačí vlastní metody.

## Cvičení 1 — Obdélník (★☆☆)

Třída `Obdelnik` s konstruktorem `__init__(self, a, b)` a metodou `obsah(self)`, která **vrátí** `a * b`.

Ověření: `Obdelnik(5, 3).obsah()` je `15`.

@reseni
```python
class Obdelnik:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obsah(self):
        return self.a * self.b


print(Obdelnik(5, 3).obsah())  # 15
```
@end

---

## Cvičení 2 — Čítač (★★☆)

Třída `Citac` s atributem `hodnota` (na začátku `0`). Metoda `zvys(self, n=1)` přičte `n`. Vypište hodnotu po `zvys()` a po `zvys(4)`.

Ověření: výstup je `1` a na dalším řádku `5`.

@reseni
```python
class Citac:
    def __init__(self):
        self.hodnota = 0

    def zvys(self, n=1):
        self.hodnota = self.hodnota + n


c = Citac()
c.zvys()
print(c.hodnota)  # 1
c.zvys(4)
print(c.hodnota)  # 5
```
@end

---

## Cvičení 3 — Chybí self (★☆☆)

Proč spadne volání? Opravte metodu tak, aby vypsala `Ahoj, Eva`.

```python
class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def pozdrav():
        return "Ahoj, " + self.jmeno


o = Osoba("Eva")
print(o.pozdrav())
```

@reseni
V hlavičce chybí `self`. Python do prvního parametru dosadí objekt — bez `self` není kam.

```python
class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def pozdrav(self):
        return "Ahoj, " + self.jmeno


o = Osoba("Eva")
print(o.pozdrav())  # Ahoj, Eva
```
@end

---

## Cvičení 4 — Přidej knihu (★★☆)

Třída `Kniha` (`nazev`) a třída `Autor` (`jmeno`, `knihy` jako prázdný seznam v konstruktoru). Metoda `pridej_knihu(self, kniha)` přidá knihu do seznamu. Vypište počet knih po přidání jedné.

Ověření: `len(a.knihy)` je `1`.

@reseni
```python
class Kniha:
    def __init__(self, nazev):
        self.nazev = nazev


class Autor:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.knihy = []

    def pridej_knihu(self, kniha):
        self.knihy.append(kniha)


a = Autor("Karel")
a.pridej_knihu(Kniha("R.U.R."))
print(len(a.knihy))  # 1
```
@end
