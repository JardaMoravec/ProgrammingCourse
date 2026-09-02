# Cvičení — Zápis z formuláře do databáze

Navazujete na [lekci 17](../17-vypis-z-databaze/cviceni.md): stejné soubory a tabulky. Dnes **přidáváte** řádek z formuláře.

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

Vedle `.py` zkopírujte databázi ze složky `data/` této lekce (`sklad.db` / `klice.db`), pokud ji ještě nemáte z minula. `CREATE TABLE` dál patří jen do `init_db`.

Po úspěšném odeslání **přesměruje** — F5 pak nevloží řádek znovu.

---

## Cvičení 1 — Sklad učebnic (★☆☆)

Soubor `sklad.py` jako minule. V `sklad.db` už jsou **Čítanka** a **Matematika**.

Routa `/` umí GET i POST (`methods=["GET", "POST"]`). Formulář `method="post"`, pole `name="nazev"`.

Při POST ořežte `.strip()`. Prázdný název: stav **200**, hláška **`Vyplňte název.`**, bez `INSERT`. Neprázdný: `INSERT INTO ucebnice (nazev) VALUES (?)`, `commit`, `redirect` na `/`. `g` pořád nepotřebujete. `flash` dnes ne.

Na stránce dál `<h1>Sklad</h1>` a `<ul>` s `{% for %}`. Po přidání **Fyzika** musí v seznamu být i ta.

@reseni
`sklad.py`:

```python
import sqlite3

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("sklad.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS ucebnice "
        "(id INTEGER PRIMARY KEY, nazev TEXT NOT NULL)"
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        nazev = request.form.get("nazev", "").strip()
        if not nazev:
            chyba = "Vyplňte název."
        else:
            conn = sqlite3.connect("sklad.db")
            conn.execute(
                "INSERT INTO ucebnice (nazev) VALUES (?)",
                (nazev,),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))
    conn = sqlite3.connect("sklad.db")
    conn.row_factory = sqlite3.Row
    radky = conn.execute("SELECT nazev FROM ucebnice").fetchall()
    conn.close()
    return render_template("index.html", radky=radky, chyba=chyba)
```

`templates/index.html`:

```html
<h1>Sklad</h1>
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
<ul>
  {% for radek in radky %}
    <li>{{ radek.nazev }}</li>
  {% endfor %}
</ul>
<form action="{{ url_for('index') }}" method="post">
  <label>Název <input name="nazev"></label>
  <button type="submit">Přidat</button>
</form>
```

Spustění: `python -m flask --app sklad run --debug`
@end

---

## Cvičení 2 — Evidence klíčů (★★☆)

Soubor `klice.py` z lekce 17 (`g`, `get_db`, `app_context`). V `klice.db` jsou **sborovna** a **telocvicna**.

Stejný formulář (`name="nazev"`). Navíc `app.secret_key`, po úspěchu `flash("Přidáno")` a `redirect`. V šabloně `get_flashed_messages()`.

Prázdný název: **200**, **`Vyplňte název.`**, bez flash a bez `INSERT`.

Na stránce dál **`Klíčů: …`** přes `COUNT(*)` a `fetchone()` — po přidání třetího klíče uvidíte **`Klíčů: 3`**.

@reseni
`klice.py`:

```python
import os
import sqlite3

from flask import Flask, flash, g, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "skola"
app.config["DATABASE"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "klice.db",
)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(chyba=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        "CREATE TABLE IF NOT EXISTS klice "
        "(id INTEGER PRIMARY KEY, nazev TEXT NOT NULL)"
    )
    db.commit()


with app.app_context():
    init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        nazev = request.form.get("nazev", "").strip()
        if not nazev:
            chyba = "Vyplňte název."
        else:
            db = get_db()
            db.execute("INSERT INTO klice (nazev) VALUES (?)", (nazev,))
            db.commit()
            flash("Přidáno")
            return redirect(url_for("index"))
    db = get_db()
    radky = db.execute("SELECT nazev FROM klice").fetchall()
    pocet = db.execute("SELECT COUNT(*) FROM klice").fetchone()[0]
    return render_template("index.html", radky=radky, pocet=pocet, chyba=chyba)
```

`templates/index.html`:

```html
<h1>Klíče</h1>
{% for zprava in get_flashed_messages() %}
  <p>{{ zprava }}</p>
{% endfor %}
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
<p>Klíčů: {{ pocet }}</p>
<ul>
  {% for radek in radky %}
    <li>{{ radek.nazev }}</li>
  {% endfor %}
</ul>
<form action="{{ url_for('index') }}" method="post">
  <label>Název <input name="nazev"></label>
  <button type="submit">Přidat</button>
</form>
```

Spustění: `python -m flask --app klice run --debug`
@end
