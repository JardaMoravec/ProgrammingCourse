"""Strategie — stejné volání, jiný postup."""


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


for zvire in [Pes("Azor"), Kocka("Micka")]:
    print(zvire.jmeno + ": " + zvire.ozvi_se())
