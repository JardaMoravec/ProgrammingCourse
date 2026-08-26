"""Zápis do souboru."""

with open("vystup.txt", "w", encoding="utf-8") as f:
    f.write("Ahoj ze souboru!\n")
    f.write("Druhý řádek\n")

print("Soubor vystup.txt vytvořen.")
