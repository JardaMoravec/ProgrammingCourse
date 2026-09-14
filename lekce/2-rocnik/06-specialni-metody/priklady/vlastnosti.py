"""Čtení a zápis vlastnosti metodou — zapouzdření."""


class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def vek_osoby(self):
        return self.vek

    def nastav_vek(self, vek):
        if vek < 0:
            vek = 0
        self.vek = vek

    def __str__(self):
        return self.jmeno + ", vek " + str(self.vek)


o = Osoba("Eva", 16)
o.nastav_vek(18)
print(o.vek_osoby())
print(o)
