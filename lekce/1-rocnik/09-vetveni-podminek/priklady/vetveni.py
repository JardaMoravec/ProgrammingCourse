bohata = True
stastna = False

if bohata and stastna:
    print("Gratuluji!")
elif bohata:
    print("Zkus se víc usmívat.")
elif stastna:
    print("Zkus míň utrácet.")
else:
    print("To je mi líto.")

# Výpočet zisku
nakupni = float(input("Nákupní cena: "))
prodejni = float(input("Prodejní cena: "))
rozdil = prodejni - nakupni

if rozdil >= 0:
    print(f"Vydělali jste: {rozdil} Kč")
else:
    print(f"Prodělali jste: {-rozdil} Kč")
