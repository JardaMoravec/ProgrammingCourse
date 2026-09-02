# Cvičení — Výpis dat z databáze do šablony

Navazujete na cvičení z [lekce 16](../16-pripojeni-databaze/cviceni.md): stejné soubory a tabulky. Dnes jen **čtete**.

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

Vedle `.py` zkopírujte připravenou databázi ze složky `data/` této lekce (`sklad.db` / `klice.db`). Když tam máte prázdný soubor z lekce 16, přepište ho.

**Nevkládejte řádky** — `INSERT` je [lekce 18](../18-zapis-do-databaze/lekce.md).

---

## Cvičení 1 — Sklad učebnic (★☆☆)

Soubor `sklad.py` jako minule. Zkopírujte `data/sklad.db` vedle něj (uvnitř jsou učebnice **Čítanka** a **Matematika**).

V `index()` otevřete `sklad.db`, `SELECT nazev FROM ucebnice`, vyzvedněte řádky **`fetchall()`**, spojení zavřete. Seznam předejte do šablony.

Na `/` `<h1>Sklad</h1>` a `<ul>` s `{% for %}` — oba názvy jako `<li>`. `g` pořád nepotřebujete. `init_db` z lekce 16 nechte (jen `CREATE TABLE`).

@reseni
`sklad.py`:

```python
import sqlite3

from flask import Flask, render_template

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


@app.route("/")
def index():
    conn = sqlite3.connect("sklad.db")
    conn.row_factory = sqlite3.Row
    radky = conn.execute("SELECT nazev FROM ucebnice").fetchall()
    conn.close()
    return render_template("index.html", radky=radky)
```

`templates/index.html`:

```html
<h1>Sklad</h1>
<ul>
  {% for radek in radky %}
    <li>{{ radek.nazev }}</li>
  {% endfor %}
</ul>
```

Spustění: `python -m flask --app sklad run --debug`
@end

---

## Cvičení 2 — Evidence klíčů (★★☆)

Soubor `klice.py` z lekce 16 (`g`, `get_db`, `app_context`). Zkopírujte `data/klice.db` vedle něj (klíče **sborovna** a **telocvicna**).

V `index()`:

- `SELECT nazev FROM klice` + **`fetchall()`** — seznam do `{% for %}`,
- `SELECT COUNT(*) FROM klice` + **`fetchone()`** — číslo na stránce jako **`Klíčů: 2`**.

`fetchone()` vrátí jeden řádek; počet je `radek[0]`. `init_db` dál jen při startu, bez `INSERT`.

@reseni
`klice.py`:

```python
import os
import sqlite3

from flask import Flask, g, render_template

app = Flask(__name__)
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


@app.route("/")
def index():
    db = get_db()
    radky = db.execute("SELECT nazev FROM klice").fetchall()
    pocet = db.execute("SELECT COUNT(*) FROM klice").fetchone()[0]
    return render_template("index.html", radky=radky, pocet=pocet)
```

`templates/index.html`:

```html
<h1>Klíče</h1>
<p>Klíčů: {{ pocet }}</p>
<ul>
  {% for radek in radky %}
    <li>{{ radek.nazev }}</li>
  {% endfor %}
</ul>
```

Spustění: `python -m flask --app klice run --debug`
@end
