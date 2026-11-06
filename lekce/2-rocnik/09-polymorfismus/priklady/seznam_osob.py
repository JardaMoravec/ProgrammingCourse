"""Jeden cyklus, stejné volání, jiný výsledek."""


class Osoba:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def prezentuj_se(self):
        return "Jsem osoba."


class Zak(Osoba):
    def prezentuj_se(self):
        return "Jsem žák."


class Ucitel(Osoba):
    def prezentuj_se(self):
        return "Jsem učitel."


seznam = [Zak("Eva"), Ucitel("Jan"), Zak("Tomáš")]
for osoba in seznam:
    print(osoba.jmeno + ": " + osoba.prezentuj_se())
