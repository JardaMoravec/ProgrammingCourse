"""Žák a Učitel přepíší stejnou metodu prezentuj_se."""


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


z = Zak("Eva")
u = Ucitel("Jan")
o = Osoba("Neznámá osoba")
print(z.prezentuj_se())
print(u.prezentuj_se())
print(o.prezentuj_se())
