# Cvičení — Nahrávání souborů a obrázků

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Úkol 1 — Odevzdání výkresu (★☆☆)

Soubor `vykres.py`. Na `/` formulář POST s `enctype="multipart/form-data"` a polem `type="file"` `name="soubor"`.

Po odeslání soubor **uložte** do `static/uploads/` pod názvem z `secure_filename`. Složku vytvořte `os.makedirs(..., exist_ok=True)`.

Pak `flash` s textem **`Uloženo:`** a původním (zabezpečeným) názvem, třeba `Uloženo: figurka.png`, a `redirect` na `/`.
V šabloně `get_flashed_messages()`.

Obrázek zatím nevypisujte. V Síti ověřte POST **302** a GET `/` **200**.

@reseni
`vykres.py`:

```python
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "skola"

SLOZKA = os.path.join("static", "uploads")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        soubor = request.files.get("soubor")
        jmeno = secure_filename(soubor.filename) if soubor else ""
        if jmeno:
            os.makedirs(SLOZKA, exist_ok=True)
            soubor.save(os.path.join(SLOZKA, jmeno))
            flash("Uloženo: " + jmeno)
            return redirect(url_for("index"))
    return render_template("index.html")
```

`templates/index.html`:

```html
<h1>Výkres</h1>
{% for zprava in get_flashed_messages() %}
  <p>{{ zprava }}</p>
{% endfor %}
<form action="{{ url_for('index') }}" method="post" enctype="multipart/form-data">
  <label>Soubor <input type="file" name="soubor"></label>
  <button type="submit">Odevzdat</button>
</form>
```

Spustění: `python -m flask --app vykres run --debug`
@end

---

## Úkol 2 — Nástěnka (★★☆)

Soubor `nastenka.py`. Formulář POST, pole `name="foto"`.

Po odeslání:

- nic nevybrané (`filename` prázdné) → na stránce **`Vyberte soubor`** (stav **200**, bez redirect),
- soubor vybraný → uložte do `static/uploads/` (zabezpečený název), `flash("Vyvěšeno")`, `redirect` na `/`.

Na stránce vypište nahrané soubory: `os.listdir` složky `static/uploads` a v šabloně `{% for %}` s `<img>` přes `url_for('static', filename='uploads/' + jmeno)`.

Ověřte: bez souboru hláška zůstane, s fotkou 302 a pak je obrázek vidět.

@reseni
`nastenka.py`:

```python
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "skola"

SLOZKA = os.path.join("static", "uploads")


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        soubor = request.files.get("foto")
        if soubor is None or soubor.filename == "":
            chyba = "Vyberte soubor"
        else:
            jmeno = secure_filename(soubor.filename)
            if not jmeno:
                chyba = "Vyberte soubor"
            else:
                os.makedirs(SLOZKA, exist_ok=True)
                soubor.save(os.path.join(SLOZKA, jmeno))
                flash("Vyvěšeno")
                return redirect(url_for("index"))
    obrazky = []
    if os.path.isdir(SLOZKA):
        obrazky = os.listdir(SLOZKA)
    return render_template("index.html", chyba=chyba, obrazky=obrazky)
```

`templates/index.html`:

```html
<h1>Nástěnka</h1>
{% for zprava in get_flashed_messages() %}
  <p>{{ zprava }}</p>
{% endfor %}
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
<form action="{{ url_for('index') }}" method="post" enctype="multipart/form-data">
  <label>Foto <input type="file" name="foto"></label>
  <button type="submit">Vyvěsit</button>
</form>
{% for jmeno in obrazky %}
  <p>
    <img src="{{ url_for('static', filename='uploads/' + jmeno) }}" alt="{{ jmeno }}">
  </p>
{% endfor %}
```

Spustění: `python -m flask --app nastenka run --debug`
@end
