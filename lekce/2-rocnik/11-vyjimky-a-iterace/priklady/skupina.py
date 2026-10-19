"""Skupina jde procházet cyklem for díky __iter__."""


class Skupina:
    def __init__(self):
        self.jmena = []

    def pridej(self, jmeno):
        self.jmena.append(jmeno)

    def __iter__(self):
        return iter(self.jmena)


s = Skupina()
s.pridej("Eva")
s.pridej("Karel")
for jmeno in s:
    print(jmeno)
