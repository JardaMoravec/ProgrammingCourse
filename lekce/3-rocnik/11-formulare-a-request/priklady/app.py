from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    jmeno = ""
    if request.method == "POST":
        jmeno = request.form.get("jmeno", "")
    return render_template("index.html", jmeno=jmeno)
