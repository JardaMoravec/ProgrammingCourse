"""Továrna — if podle druhu jen při vzniku, ne v cyklu."""


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


def udelej_zvire(druh, jmeno):
    if druh == "pes":
        return Pes(jmeno)
    if druh == "kocka":
        return Kocka(jmeno)
    raise ValueError("neznamy druh")


a = udelej_zvire("pes", "Azor")
b = udelej_zvire("kocka", "Micka")
print(a.ozvi_se())
print(b.ozvi_se())
