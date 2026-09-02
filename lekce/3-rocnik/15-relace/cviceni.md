# Cvičení — Relace (session)

Soubory spouštějte ze složky se `.py` a `templates/`:

```bash
python -m flask --app NAZEV run --debug
```

---

## Cvičení 1 — Stanoviště (★☆☆)

Soubor `stanoviste.py`. Na `/` formulář POST s polem `name="jmeno"`. Nastavte `app.secret_key`.

Po odeslání jméno uložte do `session["jmeno"]` a `redirect` na `/`.
Na stránce vypište **`Ahoj, `** a to jméno (třeba `Ahoj, Eva`).

Flash nepoužívejte — po F5 má jméno **zůstat**. V Síti ověřte POST **302** a GET **200**.

@reseni
`stanoviste.py`:

```python
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "skola"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "")
        session["jmeno"] = jmeno
        return redirect(url_for("index"))
    return render_template("index.html", jmeno=session.get("jmeno", ""))
```

`templates/index.html`:

```html
<h1>Stanoviště</h1>
{% if jmeno %}
  <p>Ahoj, {{ jmeno }}</p>
{% endif %}
<form action="{{ url_for('index') }}" method="post">
  <label>Jméno <input name="jmeno"></label>
  <button type="submit">Zapamatovat</button>
</form>
```

Spustění: `python -m flask --app stanoviste run --debug`
@end

---

## Cvičení 2 — Šatna (★★☆)

Soubor `satna.py`. Pole `name="jmeno"`, `secret_key`, jméno do `session`.

Po odeslání:

- prázdné jméno nebo mezery → na stránce **`Vyplňte jméno`** (stav **200**, bez redirect),
- neprázdné → `session["jmeno"]`, `redirect` na `/`, text **`Ahoj, `** a jméno.

Přidejte **POST** `/odhlasit`: `session.clear()` (nebo `pop`) a `redirect` na `/`.
Tlačítko v šabloně jako `<form method="post">`, ne odkaz.

Ověřte: po odhlášení jméno zmizí, F5 ho nevrátí. Druhý prohlížeč (anonymní okno) vás nevidí.

@reseni
`satna.py`:

```python
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "skola"


@app.route("/", methods=["GET", "POST"])
def index():
    chyba = ""
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "").strip()
        if not jmeno:
            chyba = "Vyplňte jméno"
        else:
            session["jmeno"] = jmeno
            return redirect(url_for("index"))
    return render_template(
        "index.html",
        chyba=chyba,
        jmeno=session.get("jmeno", ""),
    )


@app.route("/odhlasit", methods=["POST"])
def odhlasit():
    session.clear()
    return redirect(url_for("index"))
```

`templates/index.html`:

```html
<h1>Šatna</h1>
{% if chyba %}
  <p>{{ chyba }}</p>
{% endif %}
{% if jmeno %}
  <p>Ahoj, {{ jmeno }}</p>
  <form action="{{ url_for('odhlasit') }}" method="post">
    <button type="submit">Odhlásit</button>
  </form>
{% else %}
  <form action="{{ url_for('index') }}" method="post">
    <label>Jméno <input name="jmeno"></label>
    <button type="submit">Zapsat</button>
  </form>
{% endif %}
```

Spustění: `python -m flask --app satna run --debug`
@end
