"""Tuple a range."""

bod = (3, 4)
print("Souřadnice:", bod)

def rozdel(a, b):
    return a // b, a % b

podil, zbytek = rozdel(17, 5)
print(podil, zbytek)
