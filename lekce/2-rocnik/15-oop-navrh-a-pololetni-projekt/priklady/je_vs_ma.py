"""Připomínka: je = dědičnost, má = složení."""


class Motor:
    def __init__(self, vykon):
        self.vykon = vykon


class Vozidlo:
    def __init__(self, znacka):
        self.znacka = znacka

    def hlaska(self):
        return "jedeme"


class Auto(Vozidlo):
    def __init__(self, znacka, vykon):
        super().__init__(znacka)
        self.motor = Motor(vykon)

    def hlaska(self):
        return "brum"


a = Auto("Skoda", 90)
print(a.znacka)
print(a.motor.vykon)
print(a.hlaska())
