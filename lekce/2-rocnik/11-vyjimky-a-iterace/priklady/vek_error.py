"""Vlastní výjimka — věk nesmí být záporný."""


class VekError(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.nastav_vek(vek)

    def nastav_vek(self, vek):
        if vek < 0:
            raise VekError()
        self.vek = vek


try:
    Osoba("Eva", -1)
except VekError:
    print("vek nesmi byt zaporny")

o = Osoba("Karel", 18)
print(o.jmeno)
print(o.vek)
