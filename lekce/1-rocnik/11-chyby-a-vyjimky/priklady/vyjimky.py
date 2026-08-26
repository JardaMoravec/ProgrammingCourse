while True:
    try:
        x = int(input("Zadejte celé číslo: "))
        y = 10 / x
        print(f"Výsledek 10 / {x} = {y}")
        break
    except ValueError:
        print("Zadaná hodnota není celé číslo. Zkuste znovu.")
    except ZeroDivisionError:
        print("Nulou dělit nelze.")
