from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    era = []
    first =[]
    extinct=[]
    status=""
    intro="Select events and geological times from these menus"
    if request.method == 'POST':
        era = request.form.getlist("era")
        first = request.form.getlist("first")
        extinct = request.form.getlist("extinct")
        status="Submitted"
        intro=""
    return render_template("index.html", era=era, first=first, extinct=extinct, status=status, intro=intro)
