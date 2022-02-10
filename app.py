from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/nutri")
def nutri():
    return render_template("nutri.html")


@app.route("/nextmeal")
def nextmeal():
    return render_template("nextmeal.html")
