"""Žák a Učitel jsou osoby — __str__ u potomka."""


class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def __str__(self):
        return self.jmeno + " " + self.prijmeni


class Zak(Osoba):
    def __init__(self, jmeno, prijmeni, rocnik):
        super().__init__(jmeno, prijmeni)
        self.rocnik = rocnik

    def __str__(self):
        return super().__str__() + ", " + str(self.rocnik) + ". ročník"


class Ucitel(Osoba):
    def __init__(self, jmeno, prijmeni, predmet):
        super().__init__(jmeno, prijmeni)
        self.predmet = predmet

    def __str__(self):
        return super().__str__() + ", učitel " + self.predmet


z = Zak("Eva", "Nováková", 2)
print(z)

u = Ucitel("Jan", "Dvořák", "matematiky")
print(u)
