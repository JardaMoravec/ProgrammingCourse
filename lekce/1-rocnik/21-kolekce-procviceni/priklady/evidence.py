"""Evidence studentů — procvičení kolekcí."""


def prumer(znamky):
    return sum(znamky) / len(znamky)


studenti = [
    {"jmeno": "Anna", "znamky": [1, 2, 1]},
    {"jmeno": "Petr", "znamky": [3, 2, 4]},
]

for s in studenti:
    print(s["jmeno"], "průměr:", prumer(s["znamky"]))
