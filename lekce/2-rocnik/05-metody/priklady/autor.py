"""Přidání knihy metodou místo autor.knihy.append."""


class Kniha:
    def __init__(self, nazev):
        self.nazev = nazev


class Autor:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.knihy = []

    def pridej_knihu(self, kniha):
        self.knihy.append(kniha)


a = Autor("Karel")
a.pridej_knihu(Kniha("R.U.R."))
print(len(a.knihy))
print(a.knihy[0].nazev)
