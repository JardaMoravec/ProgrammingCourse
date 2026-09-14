"""Auto se zeptá kola — metoda volá metodu jiného objektu."""


class Kolo:
    def __init__(self, aktualni, maximum):
        self.aktualni = aktualni
        self.maximum = maximum

    def tlak_ok(self):
        return self.aktualni <= self.maximum


class Auto:
    def __init__(self, znacka, kolo):
        self.znacka = znacka
        self.kolo = kolo

    def pneu_ok(self):
        return self.kolo.tlak_ok()


k = Kolo(2.2, 2.5)
a = Auto("Skoda", k)
print(a.pneu_ok())
