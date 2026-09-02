import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "skola"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "knihy.db",
)
db = SQLAlchemy(app)


class Kniha(db.Model):
    __tablename__ = "knihy"
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.Text, nullable=False)


def init_db():
    db.create_all()


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
            db.session.add(Kniha(nazev=nazev))
            db.session.commit()
            flash("Přidáno")
            return redirect(url_for("index"))
    knihy = Kniha.query.all()
    return render_template("index.html", knihy=knihy, chyba=chyba)
