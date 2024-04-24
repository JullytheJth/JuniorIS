from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    era = []
    if request.method == 'POST':
        era = request.form.getlist("era")
    return render_template("index.html", era=era)