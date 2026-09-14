"""Metody vracejí hodnotu a mění atribut."""


class Osoba:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def cele_jmeno(self):
        return self.jmeno + " " + self.prijmeni

    def nastav_vek(self, vek):
        self.vek = vek

    def jsem_plnolety(self):
        return self.vek >= 18


o = Osoba("Karel", "Omáčka", 16)
print(o.cele_jmeno())
o.nastav_vek(30)
print(o.jsem_plnolety())
