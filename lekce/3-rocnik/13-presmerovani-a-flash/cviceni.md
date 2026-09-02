# Cvičení — Přesměrování a flash zprávy

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Cvičení 1 — Díky za přihlášku (★☆☆)

Soubor `soutez.py`. Na `/` formulář POST s polem `name="jmeno"` (jméno stačí nekontrolovat).

Po odeslání jméno **načtěte** (`request.form.get`), ale **nikam ho neukládejte** — databáze je až později. Dnes jde o přesměrování.

Pak **přesměrujte** na `/hotovo` (`redirect` + `url_for`). Tam šablona s `<h1>Díky</h1>`.

Flash zatím nepište. V Síti ověřte POST **302** a GET `/hotovo` **200**. F5 na `/hotovo` už nesmí znovu odesílat formulář.

@reseni
`soutez.py`:

```python
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "")
        # Zatím nikam neukládáme — jen přesměrujeme.
        return redirect(url_for("hotovo"))
    return render_template("index.html")


@app.route("/hotovo")
def hotovo():
    return render_template("hotovo.html")
```

`templates/index.html`:

```html
<h1>Soutěž</h1>
<form action="{{ url_for('index') }}" method="post">
  <label>Jméno <input name="jmeno"></label>
  <button type="submit">Přihlásit</button>
</form>
```

`templates/hotovo.html`:

```html
<h1>Díky</h1>
<p><a href="{{ url_for('index') }}">Zpět</a></p>
```

Spustění: `python -m flask --app soutez run --debug`
@end

---

## Cvičení 2 — Hlášení s flash (★★☆)

Soubor `hlaseni.py`. Na `/` formulář POST, pole `name="jmeno"`.

Po odeslání (jméno nemusíte validovat) ho vložte do flash, třeba
`flash(f"Odesláno: {jmeno}")`, a `redirect` zpět na `/`.
V šabloně vypište zprávy přes `get_flashed_messages()`.

Nastavte `app.secret_key` (libovolný krátký řetězec). Bez něj `flash` spadne.

Ověřte: po odeslání „Eva“ je v Síti 302 a pak GET `/` s textem **Odesláno: Eva**.
Další F5 hlášku už neukáže.

@reseni
`hlaseni.py`:

```python
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "skola"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "")
        flash(f"Odesláno: {jmeno}")
        return redirect(url_for("index"))
    return render_template("index.html")
```

`templates/index.html`:

```html
<h1>Hlášení</h1>
{% for zprava in get_flashed_messages() %}
  <p>{{ zprava }}</p>
{% endfor %}
<form action="{{ url_for('index') }}" method="post">
  <label>Jméno <input name="jmeno"></label>
  <button type="submit">Odeslat</button>
</form>
```

Spustění: `python -m flask --app hlaseni run --debug`
@end
