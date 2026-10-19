"""Zaměstnanec je osoba — dědí cele_jmeno."""


class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni


class Zamestnanec(Osoba):
    def nastav_pozici(self, pozice):
        self.pozice = pozice


z = Zamestnanec("Karel", "Omáčka")
z.nastav_pozici("skladnik")
print(z.cele_jmeno())
print(z.pozice)
