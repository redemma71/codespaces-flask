from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/yadda")
def yadda():
    return render_template("yadda.html",title="Yadda Yadda Yadda")
