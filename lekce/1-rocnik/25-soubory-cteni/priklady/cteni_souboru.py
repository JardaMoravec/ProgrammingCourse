"""Čtení ze souboru — ukázka."""

# Vytvoř ukázkový soubor pro test
with open("ukazka.txt", "w", encoding="utf-8") as f:
    f.write("První řádek\nDruhý řádek\n")

with open("ukazka.txt", "r", encoding="utf-8") as f:
    for radek in f:
        print(radek.strip())
