from flask import Flask, render_template, request, redirect, url_for
import os, json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/index", methods=["GET"])
def index2():
    return render_template("index.html")

@app.route("/howToPlay", methods=["GET"])
def howToPlay():
    return render_template("howToPlay.html")

@app.route("/classDesc", methods=["GET"])
def classDesc():
    return render_template("classDesc.html")

@app.route("/leaderboards", methods=["GET"])
def leaderboards():
    return render_template("leaderboards.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    
    accountsDict = {"Usename": "Password"}
    document_path = "accounts.json"
    with open(document_path, "r") as f:
        for line in f:
            (key, val) = line.split()
            accountsDict[key] = val
    
    
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect("/index")
    return render_template('login.html', error=error)

app.run(host='0.0.0.0', port=81, debug=True)

