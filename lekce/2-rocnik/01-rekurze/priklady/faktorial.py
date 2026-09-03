"""Rekurzivní faktoriál."""


def faktorial(n):
    if n <= 1:
        return 1
    return n * faktorial(n - 1)


if __name__ == "__main__":
    print(faktorial(0))  # 1
    print(faktorial(5))  # 120
