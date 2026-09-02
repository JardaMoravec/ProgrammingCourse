# Cvičení — Úprava a mazání záznamů v aplikaci

Navazujete na [lekci 18](../18-zapis-do-databaze/cviceni.md): stejné soubory a tabulky. Dnes **měníte** nebo **mažete** řádek.

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

Vedle `.py` zkopírujte databázi ze složky `data/` této lekce (`sklad.db` / `klice.db`), pokud ji ještě nemáte z minula.

Do `SELECT` přidejte **`id`**. Formulář na přidání z lekce 18 můžete nechat — dnes na něj test není.

---

## Úkol 1 — Sklad učebnic (★☆☆)

Soubor `sklad.py`. V `sklad.db` jsou **Čítanka** a **Matematika**.

U každého názvu ve výpisu formulář **POST** na `/smazat/<id>` (`url_for('smazat', id=radek.id)`). Routa jen `methods=["POST"]`: `DELETE FROM ucebnice WHERE id = ?`, `commit`, `redirect` na `/`. `g` pořád nepotřebujete. `flash` dnes ne.

Po smazání Čítanky zbude v seznamu Matematika. GET na `/smazat/1` má dát **405**, ne smazání.

@reseni
`sklad.py`:

```python
import sqlite3

from flask import Flask, redirect, render_template, url_for

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
    radky = conn.execute("SELECT id, nazev FROM ucebnice").fetchall()
    conn.close()
    return render_template("index.html", radky=radky)


@app.route("/smazat/<int:id>", methods=["POST"])
def smazat(id):
    conn = sqlite3.connect("sklad.db")
    conn.execute("DELETE FROM ucebnice WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

`templates/index.html`:

```html
<h1>Sklad</h1>
<ul>
  {% for radek in radky %}
    <li>
      {{ radek.nazev }}
      <form action="{{ url_for('smazat', id=radek.id) }}" method="post">
        <button type="submit">Smazat</button>
      </form>
    </li>
  {% endfor %}
</ul>
```

Spustění: `python -m flask --app sklad run --debug`
@end

---

## Úkol 2 — Evidence klíčů (★★☆)

Soubor `klice.py` z lekce 18 (`g`, `get_db`, `app_context`). V `klice.db` jsou **sborovna** a **telocvicna**.

U každého klíče odkaz **Upravit** na `/upravit/<id>`. Šablona `templates/upravit.html`.

GET: `SELECT id, nazev FROM klice WHERE id = ?` a **`fetchone()`**. `None` → `abort(404)`.

POST: pole `name="nazev"`, `.strip()`. Prázdné: **200**, **`Vyplňte název.`**, bez `UPDATE`. Neprázdné: `UPDATE klice SET nazev = ? WHERE id = ?`, `commit`, `flash("Uloženo")`, `redirect` na `/`.

Na seznamu dál **`Klíčů: …`** přes `COUNT(*)` a `fetchone()`.

@reseni
`klice.py`:

```python
import os
import sqlite3

from flask import Flask, abort, flash, g, redirect, render_template, request, url_for

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


@app.route("/")
def index():
    db = get_db()
    radky = db.execute("SELECT id, nazev FROM klice").fetchall()
    pocet = db.execute("SELECT COUNT(*) FROM klice").fetchone()[0]
    return render_template("index.html", radky=radky, pocet=pocet)


@app.route("/upravit/<int:id>", methods=["GET", "POST"])
def upravit(id):
    db = get_db()
    radek = db.execute(
        "SELECT id, nazev FROM klice WHERE id = ?",
        (id,),
    ).fetchone()
    if radek is None:
        abort(404)
    chyba = ""
    if request.method == "POST":
        nazev = request.form.get("nazev", "").strip()
        if not nazev:
            chyba = "Vyplňte název."
        else:
            db.execute(
                "UPDATE klice SET nazev = ? WHERE id = ?",
                (nazev, id),
            )
            db.commit()
            flash("Uloženo")
            return redirect(url_for("index"))
    return render_template("upravit.html", radek=radek, chyba=chyba)
```

`templates/index.html`:

```html
<h1>Klíče</h1>
{% for zprava in get_flashed_messages() %}
  <p>{{ zprava }}</p>
{% endfor %}
<p>Klíčů: {{ pocet }}</p>
<ul>
  {% for radek in radky %}
    <li>
      {{ radek.nazev }}
      <a href="{{ url_for('upravit', id=radek.id) }}">Upravit</a>
    </li>
  {% endfor %}
</ul>
```

`templates/upravit.html`:

```html
<h1>Upravit</h1>
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
<form action="{{ url_for('upravit', id=radek.id) }}" method="post">
  <label>Název <input name="nazev" value="{{ radek.nazev }}"></label>
  <button type="submit">Uložit</button>
</form>
```

Spustění: `python -m flask --app klice run --debug`
@end
