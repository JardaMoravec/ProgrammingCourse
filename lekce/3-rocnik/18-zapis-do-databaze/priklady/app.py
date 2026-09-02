import os
import sqlite3

from flask import Flask, flash, g, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "skola"
app.config["DATABASE"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "skola.db",
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
        """
        CREATE TABLE IF NOT EXISTS polozky (
            id INTEGER PRIMARY KEY,
            nazev TEXT NOT NULL
        )
        """
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
            db.execute("INSERT INTO polozky (nazev) VALUES (?)", (nazev,))
            db.commit()
            flash("Přidáno")
            return redirect(url_for("index"))
    db = get_db()
    radky = db.execute("SELECT nazev FROM polozky").fetchall()
    pocet = db.execute("SELECT COUNT(*) FROM polozky").fetchone()[0]
    return render_template("index.html", radky=radky, pocet=pocet, chyba=chyba)
