"""Jeden cyklus, stejné volání, jiný výsledek."""


class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def ozvi_se(self):
        return "..."


class Pes(Zvire):
    def ozvi_se(self):
        return "Haf!"


class Kocka(Zvire):
    def ozvi_se(self):
        return "Mnou!"


seznam = [Pes("Azor"), Kocka("Micka"), Pes("Rex")]
for zvire in seznam:
    print(zvire.jmeno + ": " + zvire.ozvi_se())
