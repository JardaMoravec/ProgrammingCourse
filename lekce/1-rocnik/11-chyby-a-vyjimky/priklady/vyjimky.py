try:
    x = int(input("Zadejte celé číslo: "))
    y = 10 / x
    print(f"Výsledek 10 / {x} = {y}")
except ValueError:
    print("Zadaná hodnota není celé číslo.")
except ZeroDivisionError:
    print("Nulou dělit nelze.")
