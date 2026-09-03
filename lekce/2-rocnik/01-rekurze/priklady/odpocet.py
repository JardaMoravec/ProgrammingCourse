"""Rekurzivní odpočet od zadaného čísla k nule."""


def odpocet(x):
    print(x)
    if x > 0:
        odpocet(x - 1)


if __name__ == "__main__":
    cislo = int(input())
    odpocet(cislo)
