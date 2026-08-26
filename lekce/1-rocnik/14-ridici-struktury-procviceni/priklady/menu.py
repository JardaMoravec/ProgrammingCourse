"""Jednoduché menu — procvičení řídicích struktur."""

while True:
    print("\n1) Součet  2) Rozdíl  3) Konec")
    volba = input("Volba: ")

    if volba == "3":
        print("Na shledanou.")
        break
    elif volba in ("1", "2"):
        a = float(input("První číslo: "))
        b = float(input("Druhé číslo: "))
        if volba == "1":
            print("Součet:", a + b)
        else:
            print("Rozdíl:", a - b)
    else:
        print("Neplatná volba, zkuste znovu.")
