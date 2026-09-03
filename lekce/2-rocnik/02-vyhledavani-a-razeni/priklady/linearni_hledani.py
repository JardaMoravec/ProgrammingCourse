"""Lineární hledání — cyklus a rekurze. Pozice od jedné."""


def linearni(pole, x):
    for i in range(len(pole)):
        if pole[i] == x:
            return i + 1
    return None


def linearni_rek(pole, x, i=0):
    if i >= len(pole):
        return None
    if pole[i] == x:
        return i + 1
    return linearni_rek(pole, x, i + 1)


if __name__ == "__main__":
    pole = [4, 8, 10, 45]
    print(linearni(pole, 10))      # 3
    print(linearni_rek(pole, 10))  # 3
    print(linearni(pole, 7))       # None
