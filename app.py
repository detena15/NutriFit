from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


# @app.route("/profile")
# def profile():
#     return render_template("profile.html")
