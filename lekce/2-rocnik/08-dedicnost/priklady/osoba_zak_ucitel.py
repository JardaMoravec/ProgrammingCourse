"""Žák a Učitel jsou osoby — dědí cele_jmeno."""


class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni


class Zak(Osoba):
    def ucit_se(self):
        return "Učím se!"


class Ucitel(Osoba):
    def ucit(self, predmet):
        return "Učím " + predmet


z = Zak("Eva", "Nováková")
print(z.cele_jmeno())
print(z.ucit_se())

u = Ucitel("Jan", "Dvořák")
print(u.cele_jmeno())
print(u.ucit("matematiku"))
