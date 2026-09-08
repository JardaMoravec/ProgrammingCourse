# Cvičení — Konstruktor

Cvičení jsou na hodinu. Úkoly do AMOS mají jiná zadání. Atributy nastavujte v `__init__`, ne až po vytvoření objektu. Vlastní metody (kromě konstruktoru) nepište.

## Cvičení 1 — Auto konstruktorem (★☆☆)

Třída `Auto` s konstruktorem `__init__(self, znacka, barva)`. Vypište větu `Skoda, barva modra`.

Ověření: `Auto("Skoda", "modra")` vypíše přesně tu větu.

@reseni
```python
class Auto:
    def __init__(self, znacka, barva):
        self.znacka = znacka
        self.barva = barva


a = Auto("Skoda", "modra")
print(f"{a.znacka}, barva {a.barva}")
```
@end

---

## Cvičení 2 — Dva studenti (★★☆)

Třída `Student` s konstruktorem `__init__(self, jmeno, rocnik)`. Vytvořte dva objekty. U prvního změňte ročník na `2`. Druhý zůstane v `1`.

Ověření: po změně má první `rocnik == 2`, druhý `rocnik == 1`.

@reseni
```python
class Student:
    def __init__(self, jmeno, rocnik):
        self.jmeno = jmeno
        self.rocnik = rocnik


a = Student("Anna", 1)
b = Student("Petr", 1)
a.rocnik = 2
print(a.rocnik)  # 2
print(b.rocnik)  # 1
```
@end

---

## Cvičení 3 — TypeError (★☆☆)

Třída už má konstruktor se dvěma parametry. Proč spadne poslední řádek? Opravte vytvoření tak, aby se vypsalo `Eva Novak`.

```python
class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni


o = Osoba()
print(o.jmeno, o.prijmeni)
```

@reseni
`__init__` čeká jméno a příjmení. Prázdné `Osoba()` je `TypeError`. Hodnoty patří do závorek:

```python
class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni


o = Osoba("Eva", "Novak")
print(o.jmeno, o.prijmeni)  # Eva Novak
```
@end

---

## Cvičení 4 — Adresa v osobě (★★☆)

Třída `Adresa` (`ulice`, `mesto`) a třída `Osoba` (`jmeno`, `adresa`). Adresu předejte do konstruktoru osoby jako objekt. Vypište `Karel, Brno`.

Ověření: `o.adresa.mesto` je `Brno`.

@reseni
```python
class Adresa:
    def __init__(self, ulice, mesto):
        self.ulice = ulice
        self.mesto = mesto


class Osoba:
    def __init__(self, jmeno, adresa):
        self.jmeno = jmeno
        self.adresa = adresa


adr = Adresa("Komenskeho 12", "Brno")
o = Osoba("Karel", adr)
print(f"{o.jmeno}, {o.adresa.mesto}")
```
@end

---

## Cvičení 5 — Pojmenované argumenty (★☆☆)

Třída `Osoba` s konstruktorem `__init__(self, jmeno, prijmeni)`. Vytvořte objekt **pojmenovanými argumenty** v pořadí `prijmeni` napřed, `jmeno` potom. Vypište `Eva Novak`.

Ověření: výpis je `Eva Novak`.

@reseni
```python
class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni


o = Osoba(prijmeni="Novak", jmeno="Eva")
print(o.jmeno, o.prijmeni)  # Eva Novak
```
@end
