from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        skola="SPŠ ukázka",
        hlaseni=["Třídní schůzky ve čtvrtek", "Zítra odpadá 6. hodina"],
    )
