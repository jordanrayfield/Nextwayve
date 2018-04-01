from flask import Flask, render_template
from FlaskTest import app

@app.route('/')
def index():
    return render_template("nextwayve.html")
#def index():=
#    return render_template("index.html")

@app.route('/bsit')
def bs():
    return render_template("bsit.html")

