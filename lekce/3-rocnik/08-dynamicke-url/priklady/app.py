from flask import Flask, render_template

app = Flask(__name__)

CLANKY = {
    1: "Zápis do kroužků začíná v pondělí.",
    2: "V pátek je ředitelské volno.",
}


@app.route("/")
def index():
    return render_template("index.html", clanky=CLANKY)


@app.route("/clanek/<int:cislo>")
def clanek(cislo):
    text = CLANKY.get(cislo, "Článek neexistuje.")
    return render_template("clanek.html", cislo=cislo, text=text)
