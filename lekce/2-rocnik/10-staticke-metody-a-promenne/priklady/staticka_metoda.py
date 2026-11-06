"""Statická metoda — bez objektu, bez self."""


class Cas:
    @staticmethod
    def hodiny_na_minuty(hodiny):
        return hodiny * 60


print(Cas.hodiny_na_minuty(2))
print(Cas.hodiny_na_minuty(0))
