"""Souhrn: konstruktor, metoda, __str__, __eq__ a __len__."""


class Kniha:
    def __init__(self, nazev):
        self.nazev = nazev

    def __eq__(self, jina):
        return self.nazev == jina.nazev

    def __str__(self):
        return self.nazev


class Policka:
    def __init__(self):
        self.knihy = []

    def pridej(self, kniha):
        self.knihy.append(kniha)

    def __len__(self):
        return len(self.knihy)


a = Kniha("R.U.R.")
b = Kniha("R.U.R.")
p = Policka()
p.pridej(a)
p.pridej(Kniha("Krakatit"))
print(a)
print(a == b)
print(len(p))
