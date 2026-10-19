"""len(policka) zavolá __len__."""


class Kniha:
    def __init__(self, nazev):
        self.nazev = nazev


class Policka:
    def __init__(self):
        self.knihy = []

    def pridej(self, kniha):
        self.knihy.append(kniha)

    def __len__(self):
        return len(self.knihy)


p = Policka()
p.pridej(Kniha("R.U.R."))
p.pridej(Kniha("Válka s Mloky"))
print(len(p))
print(len(Policka()))
