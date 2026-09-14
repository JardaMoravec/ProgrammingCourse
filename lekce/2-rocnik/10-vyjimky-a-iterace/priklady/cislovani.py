"""Vlastní iterátor — __next__ a StopIteration."""


class Cislovani:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        hodnota = self.i
        self.i = self.i + 1
        return hodnota


for x in Cislovani(3):
    print(x)
