"""Dva objekty stejné třídy mají vlastní data."""


class Osoba:
    pass


o = Osoba()
o.jmeno = "Karel"

p = Osoba()
p.jmeno = "Eva"

o.jmeno = "Petr"
print(o.jmeno)  # Petr
print(p.jmeno)  # Eva
