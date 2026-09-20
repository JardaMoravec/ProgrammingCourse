"""Typická past: kód vypadá čistě, průměr je špatně.

range(len(cisla) - 1) vynechá poslední prvek.
[2, 4, 6] má dát 4.0, tohle dá 2.0.
"""


def prumer(cisla):
    soucet = 0
    for i in range(len(cisla) - 1):
        soucet += cisla[i]
    return soucet / len(cisla)


print(prumer([2, 4, 6]))
