from flask import Flask, render_template

# from db import get_db, close_db

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
