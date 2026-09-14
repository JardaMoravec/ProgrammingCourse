"""Přepis __str__ doplní rodiče přes super()."""


class Zvire:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return self.jmeno + ", vek " + str(self.vek)


class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno):
        super().__init__(jmeno, vek)
        self.plemeno = plemeno

    def __str__(self):
        return super().__str__() + ", " + self.plemeno


print(Pes("Azor", 5, "labrador"))
