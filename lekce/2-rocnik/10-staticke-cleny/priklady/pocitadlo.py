"""Počítadlo instancí — jedna hodnota u třídy."""


class Auto:
    pocet = 0

    def __init__(self, spz):
        self.spz = spz
        Auto.pocet = Auto.pocet + 1


Auto("1A1 1111")
Auto("2B2 2222")
print(Auto.pocet)
