"""Auto obsahuje Motor — objekt jako atribut."""


class Motor:
    def __init__(self, typ, obsah, palivo):
        self.typ = typ
        self.obsah = obsah
        self.palivo = palivo


class Auto:
    def __init__(self, znacka, spz, motor):
        self.znacka = znacka
        self.spz = spz
        self.motor = motor


m = Motor("TSI", 1500, "benzin")
a = Auto("Skoda", "1A2 3456", m)
print(a.znacka)
print(a.motor.palivo)
