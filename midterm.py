# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)


@sample.route("/")
def main():
    return render_template("login.html")

@sample.route("/Register.html")
def Register():
    return render_template("Register.html")

@sample.route("/login.html")
def homepage():
    return render_template("login.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5000)