# Cvičení — Speciální metody a vlastnosti

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

## Cvičení 3 — Nastav cenu (★★☆)

Třída `Produkt` (`nazev`, `cena`). Metoda `nastav_cena(self, cena)` nastaví cenu; zápornou nahradí `0`. Metoda `cena_s_dph(self)` vrátí cenu × 1.21. `__str__` vypíše název a cenu.

Ověření: po `nastav_cena(-10)` je `cena` `0`. `Produkt("chleba", 100).cena_s_dph()` je `121.0`.

@reseni
```python
class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def nastav_cena(self, cena):
        if cena < 0:
            cena = 0
        self.cena = cena

    def cena_s_dph(self):
        return self.cena * 1.21

    def __str__(self):
        return self.nazev + ", " + str(self.cena)


p = Produkt("chleba", 100)
print(p.cena_s_dph())  # 121.0
p.nastav_cena(-10)
print(p.cena)          # 0
print(p)
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
