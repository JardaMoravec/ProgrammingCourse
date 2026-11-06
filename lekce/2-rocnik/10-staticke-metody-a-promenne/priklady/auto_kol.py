"""Počet kol patří třídě, SPZ patří autu."""


class Auto:
    kol = 4

    def __init__(self, spz):
        self.spz = spz


a = Auto("1A1 1111")
b = Auto("2B2 2222")
print(a.spz)
print(b.spz)
print(Auto.kol)
print(a.kol)
