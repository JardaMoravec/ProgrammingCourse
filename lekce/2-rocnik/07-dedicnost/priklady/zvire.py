"""Pes a kočka dědí ze zvířete."""


class Zvire:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def predstavit(self):
        return self.jmeno + ", vek " + str(self.vek)


class Pes(Zvire):
    def stekej(self):
        return "Haf!"


class Kocka(Zvire):
    def zamnoukej(self):
        return "Mnou!"


p = Pes("Azor", 5)
print(p.predstavit())
print(p.stekej())

k = Kocka("Micka", 3)
print(k.predstavit())
print(k.zamnoukej())
