"""Pes a kočka přepíší stejnou metodu ozvi_se."""


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


p = Pes("Azor")
k = Kocka("Micka")
z = Zvire("neznamo")
print(p.ozvi_se())
print(k.ozvi_se())
print(z.ozvi_se())
