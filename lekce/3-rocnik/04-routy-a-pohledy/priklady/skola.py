from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>SPŠ ukázka</h1>
    <p>Vítejte na stránkách školy.</p>
    <p><a href="/kontakt">Kontakt</a></p>
    """


@app.route("/kontakt")
def kontakt():
    return """
    <h1>Kontakt</h1>
    <p>E-mail: info@skola.cz</p>
    <p><a href="/">Zpět na hlavní stránku</a></p>
    """
