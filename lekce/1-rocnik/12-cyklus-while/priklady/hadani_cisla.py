import random

tajne = random.randint(1, 100)
pokusy = 0
max_pokusu = 10

while pokusy < max_pokusu:
    pokusy += 1
    try:
        tip = int(input("Hádejte číslo 1–100: "))
    except ValueError:
        print("Zadejte celé číslo.")
        continue

    if tip == tajne:
        print(f"Výhra! Počet pokusů: {pokusy}")
        break
    elif tip < tajne:
        print("Větší.")
    else:
        print("Menší.")
else:
    print(f"Prohra. Číslo bylo {tajne}.")
