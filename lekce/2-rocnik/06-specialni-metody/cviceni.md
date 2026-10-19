# Cvičení — Speciální metody

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Dědičnost nepište.

## Cvičení 1 — Film (★☆☆)

Třída `Film` (`nazev`, `rok`) s `__str__`. `print(film)` má vypsat `Matrix (1999)`.

Ověření: výstup je přesně ta věta.

@reseni
```python
class Film:
    def __init__(self, nazev, rok):
        self.nazev = nazev
        self.rok = rok

    def __str__(self):
        return self.nazev + " (" + str(self.rok) + ")"


f = Film("Matrix", 1999)
print(f)
```
@end

---

## Cvičení 2 — None místo textu (★☆☆)

Proč `print(o)` vypíše `None`? Opravte `__str__` tak, aby výstup byl `Eva`.

```python
class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        print(self.jmeno)


o = Osoba("Eva")
print(o)
```

@reseni
`__str__` má **vrátit** řetězec. `print` uvnitř nic nevrátí, takže vnější `print(o)` dostane `None`.

```python
class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return self.jmeno


o = Osoba("Eva")
print(o)  # Eva
```
@end

---

## Cvičení 3 — Stejný účet (★★☆)

Třída `Ucet` (`cislo`, celé číslo). `__eq__` vrátí `True`, když mají oba účty stejné číslo.

Ověření: `Ucet(1) == Ucet(1)` je `True`. `Ucet(1) == Ucet(2)` je `False`.

@reseni
```python
class Ucet:
    def __init__(self, cislo):
        self.cislo = cislo

    def __eq__(self, jiny):
        return self.cislo == jiny.cislo


print(Ucet(1) == Ucet(1))  # True
print(Ucet(1) == Ucet(2))  # False
```
@end

---

## Cvičení 4 — str vnořeného objektu (★★☆)

Třída `Motor` (`typ`, `palivo`) a třída `Auto` (`znacka`, `motor`). Obě mají `__str__`. `print(auto)` má vypsat `Skoda, TSI benzin`.

Ověření: ve `__str__` auta použijte `str(self.motor)`.

@reseni
```python
class Motor:
    def __init__(self, typ, palivo):
        self.typ = typ
        self.palivo = palivo

    def __str__(self):
        return self.typ + " " + self.palivo


class Auto:
    def __init__(self, znacka, motor):
        self.znacka = znacka
        self.motor = motor

    def __str__(self):
        return self.znacka + ", " + str(self.motor)


a = Auto("Skoda", Motor("TSI", "benzin"))
print(a)  # Skoda, TSI benzin
```
@end

---

## Cvičení 5 — Délka košíku (★★☆)

Třída `Kosik`. Metoda `pridej(self, nazev)` přidá název do seznamu. `__len__` vrátí počet položek.

Ověření: prázdný košík má `len` `0`. Po `pridej("chleba")` a `pridej("mleko")` je `len(kosik)` `2`.

@reseni
```python
class Kosik:
    def __init__(self):
        self.polozky = []

    def pridej(self, nazev):
        self.polozky.append(nazev)

    def __len__(self):
        return len(self.polozky)


k = Kosik()
print(len(k))  # 0
k.pridej("chleba")
k.pridej("mleko")
print(len(k))  # 2
```
@end
