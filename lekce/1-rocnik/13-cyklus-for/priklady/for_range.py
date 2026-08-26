print("range(5):")
for i in range(5):
    print(i, end=" ")
print("\n")

print("range(3, 7):")
for i in range(3, 7):
    print(i, end=" ")
print("\n")

print("Sudá 0–8:")
for x in range(0, 10, 2):
    print(x, end=" ")
print("\n")

# Součet sudých a lichých 1–30
suda = licha = 0
for n in range(1, 31):
    if n % 2 == 0:
        suda += n
    else:
        licha += n
print("Sudá:", suda, "| Lichá:", licha)
