"""Tabulka knih v paměti — analogie relační tabulky, ne databáze."""

knihy = [
    {"id": 1, "nazev": "R.U.R.", "rok": 1920},
    {"id": 2, "nazev": "Válka s Mloky", "rok": 1936},
    {"id": 3, "nazev": "Krakatit", "rok": 1922},
]

hledane_id = 2
nalezeno = None
for k in knihy:
    if k["id"] == hledane_id:
        nalezeno = k
        break

if nalezeno is None:
    print("Nenalezeno")
else:
    print(nalezeno["nazev"])
