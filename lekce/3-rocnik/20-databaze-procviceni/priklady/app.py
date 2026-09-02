import os
import sqlite3

from flask import Flask, abort, flash, g, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "knihovna"
app.config["DATABASE"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "knihovna.db",
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
        CREATE TABLE IF NOT EXISTS knihy (
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
            db.execute("INSERT INTO knihy (nazev) VALUES (?)", (nazev,))
            db.commit()
            flash("Přidáno")
            return redirect(url_for("index"))
    db = get_db()
    radky = db.execute("SELECT id, nazev FROM knihy").fetchall()
    return render_template("index.html", radky=radky, chyba=chyba)


@app.route("/upravit/<int:id>", methods=["GET", "POST"])
def upravit(id):
    db = get_db()
    radek = db.execute(
        "SELECT id, nazev FROM knihy WHERE id = ?",
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
                "UPDATE knihy SET nazev = ? WHERE id = ?",
                (nazev, id),
            )
            db.commit()
            flash("Uloženo")
            return redirect(url_for("index"))
    return render_template("upravit.html", radek=radek, chyba=chyba)


@app.route("/smazat/<int:id>", methods=["POST"])
def smazat(id):
    db = get_db()
    db.execute("DELETE FROM knihy WHERE id = ?", (id,))
    db.commit()
    flash("Smazáno")
    return redirect(url_for("index"))
