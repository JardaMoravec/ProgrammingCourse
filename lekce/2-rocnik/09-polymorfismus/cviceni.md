# Cvičení — Polymorfismus

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Jde o **přepis** stejné metody, ne o novou metodu s jiným názvem.

## Cvičení 1 — Kytara (★☆☆)

Třída `Nastroj` s metodou `zahraj(self)`, která vrátí `tic`. Třída `Kytara(Nastroj)` metodu **přepíše** tak, aby vrátila `brnk`. Vypište `Kytara().zahraj()`.

Ověření: výstup je `brnk`.

@reseni
```python
class Nastroj:
    def zahraj(self):
        return "tic"


class Kytara(Nastroj):
    def zahraj(self):
        return "brnk"


print(Kytara().zahraj())
```
@end

---

## Cvičení 2 — Kapela (★★☆)

Stejný rodič `Nastroj` a `zahraj`. `Housle` vrátí `e-e`, `Buben` vrátí `bum`. Dejte oba nástroje do seznamu a cyklem vypište `zahraj()` u každého.

Ověření: dva řádky `e-e` a `bum` (v tomto pořadí). Bez `if` podle typu.

@reseni
```python
class Nastroj:
    def zahraj(self):
        return "tic"


class Housle(Nastroj):
    def zahraj(self):
        return "e-e"


class Buben(Nastroj):
    def zahraj(self):
        return "bum"


kapela = [Housle(), Buben()]
for nastroj in kapela:
    print(nastroj.zahraj())
```
@end

---

## Cvičení 3 — Není to přepis (★☆☆)

Proč poslední `print` vypíše `sss`, ne `vrrr`? Opravte vrták tak, aby `zvuk()` vrátilo `vrrr`.

```python
class Stroj:
    def zvuk(self):
        return "sss"


class Vrtacka(Stroj):
    def vrtat(self):
        return "vrrr"


print(Vrtacka().zvuk())
```

@reseni
Metoda se jmenuje `vrtat`, rodičovská `zvuk`. To **není** přepis — `zvuk()` pořád bere tělo ze `Stroj`. Přejmenujte metodu na `zvuk`:

```python
class Stroj:
    def zvuk(self):
        return "sss"


class Vrtacka(Stroj):
    def zvuk(self):
        return "vrrr"


print(Vrtacka().zvuk())  # vrrr
```
@end

---

## Cvičení 4 — Expresní balík (★★☆)

Třída `Balik` (`hmotnost` celé číslo). `__str__` vrátí `hmotnost kg`. Třída `ExpresniBalik(Balik)` má navíc `hodiny`. V `__str__` použijte `super()` a připojte `, 24 h` (hodiny jako číslo). Vypište `print(ExpresniBalik(3, 24))`.

Ověření: výstup je `3 kg, 24 h`.

@reseni
```python
class Balik:
    def __init__(self, hmotnost):
        self.hmotnost = hmotnost

    def __str__(self):
        return str(self.hmotnost) + " kg"


class ExpresniBalik(Balik):
    def __init__(self, hmotnost, hodiny):
        super().__init__(hmotnost)
        self.hodiny = hodiny

    def __str__(self):
        return super().__str__() + ", " + str(self.hodiny) + " h"


print(ExpresniBalik(3, 24))
```
@end
