# Cvičení — Připojení aplikace k databázi

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

Po spuštění vedle `.py` vznikne soubor `.db`.
`CREATE TABLE` patří do `init_db` při startu, **ne** do pohledu. Dnes bez `SELECT` a `INSERT`.

---

## Cvičení 1 — Sklad učebnic (★☆☆)

Soubor `sklad.py`. Funkce `init_db()` otevře `sklad.db`, spustí

`CREATE TABLE IF NOT EXISTS ucebnice (id INTEGER PRIMARY KEY, nazev TEXT NOT NULL)`

a spojení zavře. Zavolejte ji **při načtení souboru**, ne z `index()`.

Na `/` šablona: `<h1>Sklad</h1>` a přesně **`Připojeno`**. `g` zatím nepotřebujete. `commit` po `CREATE` nezapomeňte.

Ověřte: po startu existuje `sklad.db`. F5 na `/` stránku jen znovu ukáže — zakládání tabulky v Síti u GET nehledejte.

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
    return render_template("index.html")
```

`templates/index.html`:

```html
<h1>Sklad</h1>
<p>Připojeno</p>
```

Spustění: `python -m flask --app sklad run --debug`
@end

---

## Cvičení 2 — Evidence klíčů (★★☆)

Soubor `klice.py`. Cestu k `klice.db` dejte do `app.config["DATABASE"]` přes `__file__` (vedle `.py`).

Použijte `get_db()` s `g` a `teardown_appcontext` jako v lekci. Tabulka `klice` sloupce `id` a `nazev`.

`init_db()` volá `get_db()`, a ten ukládá spojení do `g`. `g` existuje jen **uvnitř kontextu aplikace**: Flask ho otevře sám, když přijde GET/POST. Při startu souboru ještě žádný požadavek není — `g` tam není a holé `init_db()` spadne.

Proto:

```python
with app.app_context():
    init_db()
```

`with` na chvíli kontext **otevře** (jako by zrovna běžel požadavek), `init_db()` může použít `g`, a na konci bloku kontext **zavře** — spustí se `teardown_appcontext` a spojení se uklidí. Ve cvičení 1 `g` nebylo, stačilo `init_db()` samo.

Zavolejte to **jednou při načtení souboru**, ne z pohledu.
Na `/` vypište přesně **`Evidence je připravená`**. Řádky do tabulky nevkládejte.

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
    init_db()  # bez kontextu get_db() nemá g — ještě nepřišel GET


@app.route("/")
def index():
    return render_template("index.html")
```

`templates/index.html`:

```html
<h1>Klíče</h1>
<p>Evidence je připravená</p>
```

Spustění: `python -m flask --app klice run --debug`
@end
