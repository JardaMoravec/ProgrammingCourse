"""Základní funkce — parametry a return."""


def soucet(a, b):
    return a + b


def je_sude(n):
    return n % 2 == 0


def pozdrav(jmeno="světe"):
    print(f"Ahoj, {jmeno}!")


if __name__ == "__main__":
    print("Součet 3 + 7 =", soucet(3, 7))
    print("10 je sudé:", je_sude(10))
    pozdrav("Python")
