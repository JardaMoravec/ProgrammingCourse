"""Žák a Učitel dědí informace z osoby — super()."""


class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni


class Zak(Osoba):
    def __init__(self, jmeno, prijmeni, rocnik):
        super().__init__(jmeno, prijmeni)
        self.rocnik = rocnik


class Ucitel(Osoba):
    def __init__(self, jmeno, prijmeni, predmet):
        super().__init__(jmeno, prijmeni)
        self.predmet = predmet


z = Zak("Eva", "Nováková", 2)
print(z.cele_jmeno())
print(z.rocnik)

u = Ucitel("Jan", "Dvořák", "matematika")
print(u.cele_jmeno())
print(u.predmet)
