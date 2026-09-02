# Cvičení — ORM (bonus)

Nejdřív `python -m pip install flask-sqlalchemy`. Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

SQL řetězce (`CREATE TABLE`, `SELECT`, `INSERT`) a modul `sqlite3` **nepoužívejte**. Tabulku založí `create_all`, cesta k `.db` je `sqlite:///` + `__file__`.

---

## Cvičení 1 — Skleník (★☆☆)

Soubor `sklenik.py`. Model **`Rostlina`**, tabulka **`rostliny`** (`__tablename__`), sloupce `id` a `nazev`.

Při startu `create_all` v `app_context`. Když je tabulka prázdná, vložte **Bazalka** a **Máta** (`add` + `commit`) — ať je na stránce co číst. Do pohledu `INSERT` nepatří.

Na `/` jen GET: `Rostlina.query.all()`, šablona `<h1>Skleník</h1>` a `<ul>` s `{% for %}` — `{{ rostlina.nazev }}`. Formulář dnes ne.

@reseni
`sklenik.py`:

```python
import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "sklenik.db",
)
db = SQLAlchemy(app)


class Rostlina(db.Model):
    __tablename__ = "rostliny"
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()
    if Rostlina.query.count() == 0:
        db.session.add(Rostlina(nazev="Bazalka"))
        db.session.add(Rostlina(nazev="Máta"))
        db.session.commit()


@app.route("/")
def index():
    rostliny = Rostlina.query.all()
    return render_template("index.html", rostliny=rostliny)
```

`templates/index.html`:

```html
<h1>Skleník</h1>
<ul>
  {% for rostlina in rostliny %}
    <li>{{ rostlina.nazev }}</li>
  {% endfor %}
</ul>
```

Spustění: `python -m flask --app sklenik run --debug`
@end

---

## Cvičení 2 — Deskové hry (★★☆)

Soubor `hry.py`. Model **`Hra`**, tabulka **`hry`**, sloupce `id` a `nazev`. `create_all` při startu, **bez** předvyplnění řádků. Nastavte `app.secret_key`.

Routa `/` umí GET i POST. Formulář `method="post"`, pole `name="nazev"`.

| POST | Stav | Chování |
|------|------|---------|
| prázdný název (i mezery) | **200** | `Vyplňte název.`, bez `add` |
| neprázdný | **302** na `/` | `db.session.add`, `commit`, `flash("Přidáno")` |

Na stránce `<h1>Hry</h1>`, `{% for %}` přes `Hra.query.all()`, `get_flashed_messages()` a `{{ chyba }}`. Po přidání **Doby** musí v seznamu být.

@reseni
`hry.py`:

```python
import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "skola"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "hry.db",
)
db = SQLAlchemy(app)


class Hra(db.Model):
    __tablename__ = "hry"
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        nazev = request.form.get("nazev", "").strip()
        if not nazev:
            chyba = "Vyplňte název."
        else:
            db.session.add(Hra(nazev=nazev))
            db.session.commit()
            flash("Přidáno")
            return redirect(url_for("index"))
    hry = Hra.query.all()
    return render_template("index.html", hry=hry, chyba=chyba)
```

`templates/index.html`:

```html
<h1>Hry</h1>
{% for zprava in get_flashed_messages() %}
  <p>{{ zprava }}</p>
{% endfor %}
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
<ul>
  {% for hra in hry %}
    <li>{{ hra.nazev }}</li>
  {% endfor %}
</ul>
<form action="{{ url_for('index') }}" method="post">
  <label>Název <input name="nazev"></label>
  <button type="submit">Přidat</button>
</form>
```

Spustění: `python -m flask --app hry run --debug`
@end
