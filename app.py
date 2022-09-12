from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>/<idade>")
def hello_world(name=None, idade=None):
    return render_template("home.html", name=name, idade=idade)





