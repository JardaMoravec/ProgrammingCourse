"""== dvou knih porovná název přes __eq__."""


class Kniha:
    def __init__(self, nazev):
        self.nazev = nazev

    def __eq__(self, jina):
        return self.nazev == jina.nazev


a = Kniha("R.U.R.")
b = Kniha("R.U.R.")
c = Kniha("Válka s Mloky")
print(a == b)
print(a == c)
print(a != c)
