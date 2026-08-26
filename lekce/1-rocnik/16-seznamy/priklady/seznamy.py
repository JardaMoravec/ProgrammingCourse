"""Základy seznamů."""

cisla = [10, 20, 30]
for i, c in enumerate(cisla):
    print(f"Index {i}: {c}")

cisla.append(40)
print("Po append:", cisla)
print("Součet:", sum(cisla))
