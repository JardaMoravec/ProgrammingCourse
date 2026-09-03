"""Bublinkové řazení — bez sort() a sorted()."""


def bublinkove(pole):
    n = len(pole)
    for i in range(n):
        for j in range(n - 1 - i):
            if pole[j] > pole[j + 1]:
                pole[j], pole[j + 1] = pole[j + 1], pole[j]
    return pole


if __name__ == "__main__":
    print(bublinkove([4, 1, 3, 2]))
    print(bublinkove([2, 435, 3, 4, 68, 9]))
