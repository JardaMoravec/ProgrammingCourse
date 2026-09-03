"""Binární hledání v seřazeném seznamu. Pozice od jedné."""


def binarni(pole, x, levy=0, pravy=None):
    if pravy is None:
        pravy = len(pole) - 1
    if levy > pravy:
        return None
    stred = (levy + pravy) // 2
    if pole[stred] == x:
        return stred + 1
    if pole[stred] > x:
        return binarni(pole, x, levy, stred - 1)
    return binarni(pole, x, stred + 1, pravy)


if __name__ == "__main__":
    pole = [4, 8, 10, 45, 48, 49, 51, 100]
    print(binarni(pole, 45))  # 4
    print(binarni(pole, 4))   # 1
    print(binarni(pole, 7))   # None
