"""Výchozí hodnota parametru v konstruktoru."""


class Produkt:
    def __init__(self, nazev, cena, mena="Kc"):
        self.nazev = nazev
        self.cena = cena
        self.mena = mena


a = Produkt("chleba", 32)
b = Produkt("syr", 48, "EUR")
print(a.mena)
print(b.mena)
