# Cvičení — Databáze (souhrn)

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

Dnes **skládáte** lekce 16–19. Nová syntaxe nepřibývá. Stejný soubor `galerie.py` postupně rozšiřujte.

---

## Cvičení 1 — Založení tabulky (★☆☆)

Soubor `galerie.py`. Funkce `init_db()` otevře `galerie.db`, spustí

`CREATE TABLE IF NOT EXISTS obrazy (id INTEGER PRIMARY KEY, nazev TEXT NOT NULL)`

a spojení zavře. Zavolejte ji **při načtení souboru**, ne z `index()`. `g` zatím nepotřebujete. `commit` po `CREATE` nezapomeňte.

Na `/` šablona: `<h1>Galerie</h1>` a přesně **`Připraveno`**.

@reseni
`galerie.py`:

```python
import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("galerie.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS obrazy "
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
<h1>Galerie</h1>
<p>Připraveno</p>
```

Spustění: `python -m flask --app galerie run --debug`
@end

---

## Cvičení 2 — Výpis (★☆☆)

Zkopírujte `data/galerie.db` vedle `galerie.py` (uvnitř obrazy **Západ slunce** a **Portrét**). Když tam máte prázdný soubor ze cvičení 1, přepište ho.

V `index()` `SELECT nazev FROM obrazy`, **`fetchall()`**, spojení zavřete. Seznam do šablony.

Na `/` `<h1>Galerie</h1>` a `<ul>` s `{% for %}` — oba názvy jako `<li>`. `init_db` ze cvičení 1 nechte.

@reseni
`galerie.py` — v `index()`:

```python
@app.route("/")
def index():
    conn = sqlite3.connect("galerie.db")
    conn.row_factory = sqlite3.Row
    radky = conn.execute("SELECT nazev FROM obrazy").fetchall()
    conn.close()
    return render_template("index.html", radky=radky)
```

`templates/index.html`:

```html
<h1>Galerie</h1>
<ul>
  {% for radek in radky %}
    <li>{{ radek.nazev }}</li>
  {% endfor %}
</ul>
```

Spustění: `python -m flask --app galerie run --debug`
@end

---

## Cvičení 3 — Přidání (★★☆)

Routa `/` umí GET i POST. Formulář `method="post"`, pole `name="nazev"`.

Při POST ořežte `.strip()`. Prázdný název: **200**, **`Vyplňte název.`**, bez `INSERT`. Neprázdný: `INSERT INTO obrazy (nazev) VALUES (?)`, `commit`, `redirect` na `/`. `flash` dnes ne.

Po přidání **Krajina** musí v seznamu být i ta.

@reseni
```python
from flask import Flask, redirect, render_template, request, url_for
```

```python
@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        nazev = request.form.get("nazev", "").strip()
        if not nazev:
            chyba = "Vyplňte název."
        else:
            conn = sqlite3.connect("galerie.db")
            conn.execute("INSERT INTO obrazy (nazev) VALUES (?)", (nazev,))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))
    conn = sqlite3.connect("galerie.db")
    conn.row_factory = sqlite3.Row
    radky = conn.execute("SELECT nazev FROM obrazy").fetchall()
    conn.close()
    return render_template("index.html", radky=radky, chyba=chyba)
```

Do šablony přidejte hlášku a formulář:

```html
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
<form action="{{ url_for('index') }}" method="post">
  <label>Název <input name="nazev"></label>
  <button type="submit">Přidat</button>
</form>
```

Spustění: `python -m flask --app galerie run --debug`
@end

---

## Cvičení 4 — Smazání (★★☆)

Do `SELECT` přidejte **`id`**. U každého názvu formulář **POST** na `/smazat/<id>` (`url_for('smazat', id=radek.id)`). Routa jen `methods=["POST"]`: `DELETE FROM obrazy WHERE id = ?`, `commit`, `redirect`.

GET na `/smazat/1` má dát **405**.

@reseni
```python
@app.route("/smazat/<int:id>", methods=["POST"])
def smazat(id):
    conn = sqlite3.connect("galerie.db")
    conn.execute("DELETE FROM obrazy WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))
```

V `index()`:

```python
radky = conn.execute("SELECT id, nazev FROM obrazy").fetchall()
```

V šabloně u každé položky:

```html
<li>
  {{ radek.nazev }}
  <form action="{{ url_for('smazat', id=radek.id) }}" method="post">
    <button type="submit">Smazat</button>
  </form>
</li>
```

Spustění: `python -m flask --app galerie run --debug`
@end

---

## Cvičení 5 — Úprava (★★★)

Odkaz **Upravit** na `/upravit/<id>`. Šablona `templates/upravit.html`.

GET: `SELECT id, nazev FROM obrazy WHERE id = ?` a **`fetchone()`**. `None` → `abort(404)`.

POST: pole `name="nazev"`, `.strip()`. Prázdné: **200**, **`Vyplňte název.`**. Neprázdné: `UPDATE obrazy SET nazev = ? WHERE id = ?`, `commit`, `redirect` na `/`.

@reseni
```python
from flask import abort
```

```python
@app.route("/upravit/<int:id>", methods=["GET", "POST"])
def upravit(id):
    conn = sqlite3.connect("galerie.db")
    conn.row_factory = sqlite3.Row
    radek = conn.execute(
        "SELECT id, nazev FROM obrazy WHERE id = ?",
        (id,),
    ).fetchone()
    if radek is None:
        conn.close()
        abort(404)
    chyba = ""
    if request.method == "POST":
        nazev = request.form.get("nazev", "").strip()
        if not nazev:
            chyba = "Vyplňte název."
        else:
            conn.execute(
                "UPDATE obrazy SET nazev = ? WHERE id = ?",
                (nazev, id),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))
    conn.close()
    return render_template("upravit.html", radek=radek, chyba=chyba)
```

V seznamu odkaz:

```html
<a href="{{ url_for('upravit', id=radek.id) }}">Upravit</a>
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

Spustění: `python -m flask --app galerie run --debug`
@end
