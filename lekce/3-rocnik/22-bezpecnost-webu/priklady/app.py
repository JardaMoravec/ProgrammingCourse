import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("skola.db")
    conn.execute(
        "CREATE TABLE IF NOT EXISTS polozky "
        "(id INTEGER PRIMARY KEY, nazev TEXT NOT NULL)"
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    dotaz = request.args.get("q", "").strip()
    conn = sqlite3.connect("skola.db")
    conn.row_factory = sqlite3.Row
    if dotaz:
        radky = conn.execute(
            "SELECT nazev FROM polozky WHERE nazev = ?",
            (dotaz,),
        ).fetchall()
    else:
        radky = conn.execute("SELECT nazev FROM polozky").fetchall()
    conn.close()
    return render_template("index.html", radky=radky, dotaz=dotaz)
