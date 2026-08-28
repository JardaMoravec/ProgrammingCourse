# Cvičení — Úvod do Flasku

Soubory spouštějte v téže složce:

```bash
python -m flask --app NAZEV run --debug
```

(`NAZEV` = jméno souboru bez `.py`.)

---

## Úkol 1 — Pozdrav (★☆☆)

Vytvořte soubor `pozdrav.py`. Na adrese `/` ať aplikace vrátí přesně:

`Vítej ve 3. ročníku`

Ověřte v prohlížeči na `http://127.0.0.1:5000`.

@reseni
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Vítej ve 3. ročníku"
```

Spustění: `python -m flask --app pozdrav run --debug`
@end

---

## Úkol 2 — Profil z proměnných (★★☆)

Soubor `profil.py`. Do proměnných uložte **jméno** a **třídu** (klidně fiktivní).
Na adrese `/` vraťte **jeden řádek** ve tvaru:

`Eva Nováková, 3.A`

(místo ukázky použijte své hodnoty). Pořád jen cesta `/` — další adresy až v lekci 04.

@reseni
```python
from flask import Flask

app = Flask(__name__)

jmeno = "Eva Nováková"
trida = "3.A"


@app.route("/")
def index():
    return f"{jmeno}, {trida}"
```

Spustění: `python -m flask --app profil run --debug`
@end
