"""print(o) použije __str__."""


class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def __str__(self):
        return self.jmeno + " " + self.prijmeni


o = Osoba("Karel", "Omáčka")
print(o)
print(str(o))
