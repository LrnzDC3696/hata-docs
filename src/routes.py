from src import app
from flask import render_template


@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/intro/")
def intro():
    return render_template('intro.html')

@app.route("/topic/")
def topic():
    return render_template('topic.html')

@app.route("/ref/")
def ref():
    return render_template('ref.html')

@app.route("/meta/")
def meta():
    return render_template('meta.html')
