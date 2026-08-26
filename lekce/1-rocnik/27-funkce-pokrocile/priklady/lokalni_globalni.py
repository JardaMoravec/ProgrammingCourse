"""Lokální vs globální."""


def secti(a, b):
    soucet = a + b  # lokální
    return soucet


x = 10
print(secti(x, 5))
