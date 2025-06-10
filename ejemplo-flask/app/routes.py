from app import app
from app.views import saludo
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/saludo", methods=["GET"])
def saludo_view():
    return saludo()
