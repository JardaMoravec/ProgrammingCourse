"""__str__ vnořeného objektu přes str(self.adresa)."""


class Adresa:
    def __init__(self, ulice, mesto):
        self.ulice = ulice
        self.mesto = mesto

    def __str__(self):
        return self.ulice + ", " + self.mesto


class Osoba:
    def __init__(self, jmeno, adresa):
        self.jmeno = jmeno
        self.adresa = adresa

    def __str__(self):
        return self.jmeno + ", " + str(self.adresa)


o = Osoba("Karel", Adresa("Komenskeho 12", "Brno"))
print(o)
