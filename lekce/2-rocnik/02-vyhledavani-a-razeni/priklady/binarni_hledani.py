"""Binární hledání — půlení seznamu řezem. Pozice od jedné."""


def binarni(pole, x):
    if not pole:
        return None
    stred = len(pole) // 2  # celočíselné dělení: 5 // 2 je 2, ne 2.5
    if pole[stred] == x:
        return stred + 1
    if pole[stred] > x:
        return binarni(pole[:stred], x)
    nalez = binarni(pole[stred + 1:], x)
    if nalez is None:
        return None
    return stred + 1 + nalez


if __name__ == "__main__":
    pole = [4, 8, 10, 45, 48, 49, 51, 100]
    print(binarni(pole, 45))  # 4
    print(binarni(pole, 4))   # 1
    print(binarni(pole, 7))   # None
