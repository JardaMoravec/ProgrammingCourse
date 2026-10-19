"""Tričko dědí naskladnit z oblečení."""


class Obleceni:
    def __init__(self, pocet_kusu, velikost, barva):
        self.pocet_kusu = pocet_kusu
        self.velikost = velikost
        self.barva = barva

    def naskladnit(self, pocet):
        self.pocet_kusu = self.pocet_kusu + pocet


class Triko(Obleceni):
    def __init__(self, pocet_kusu, velikost, barva, s_lemecek):
        super().__init__(pocet_kusu, velikost, barva)
        self.s_lemecek = s_lemecek


t = Triko(10, "L", "modra", True)
t.naskladnit(5)
print(t.pocet_kusu)
print(t.s_lemecek)
