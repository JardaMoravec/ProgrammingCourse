vek = int(input("Věk: "))

if vek >= 18:
    if vek < 65:
        print("Produktivní věk (18–64).")
    else:
        print("Důchodový věk.")
else:
    print("Neplnoletý.")

print("---")

# Ekvivalent bez vnoření
if 18 <= vek < 65:
    print("Produktivní věk — zkrácený zápis.")
