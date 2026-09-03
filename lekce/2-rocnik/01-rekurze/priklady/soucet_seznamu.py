"""Součet prvků seznamu rekurzí přes index."""


def soucet_seznamu(polozky, index=0):
    if index >= len(polozky):
        return 0
    return polozky[index] + soucet_seznamu(polozky, index + 1)


if __name__ == "__main__":
    print(soucet_seznamu([10, 20, 30]))  # 60
    print(soucet_seznamu([]))            # 0
