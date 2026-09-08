"""Osoba s konstruktorem — atributy hned při vytvoření."""


class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni


o = Osoba("Karel", "Omáčka")
print(o.jmeno)
print(o.prijmeni)

p = Osoba(jmeno="Eva", prijmeni="Novák")
print(p.jmeno)
print(p.prijmeni)
