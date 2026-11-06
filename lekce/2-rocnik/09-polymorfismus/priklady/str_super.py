"""Přepis __str__ doplní rodiče přes super()."""


class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return self.jmeno + ", věk " + str(self.vek)


class Zak(Osoba):
    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return super().__str__() + ", " + str(self.rocnik) + ". ročník"


class Ucitel(Osoba):
    def __init__(self, jmeno, vek, predmet):
        super().__init__(jmeno, vek)
        self.predmet = predmet

    def __str__(self):
        return super().__str__() + ", učitel " + self.predmet


print(Zak("Eva", 14, 2))
print(Ucitel("Jan", 40, "matematiky"))
