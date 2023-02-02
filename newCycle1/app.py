from flask import Flask, render_template, request, redirect, url_for
import json

data = ""

def validPassword(password):
    specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]
    flag = False
    
    for i in range(len(password)):
        if password[i] in specialChars:
            flag =  True
            break
    
    if len(password) > 8 and flag:
        return True
    else:
        return False

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/index", methods=["GET"])
def index2():
    try:
        return render_template("index.html", data=data)
    except:
        pass
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
    
    with open("newCycle1/static/accounts.json", "r") as f:
        accountsDict = json.load(f)
    
    error = None
    if request.method == "POST":
        try:
            username = request.form['username']
            if accountsDict[username]["Password"] == request.form['password']:
                global data
                data = '{"' + str(username) + '": ' + str(accountsDict[username]) + '}'
                return redirect("/index")
            else:
                error = 'Invalid Password. Please try again.'
        except:
            error = 'Invalid Username. Please try again.'
    return render_template('login.html', error=error)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    with open("newCycle1/static/accounts.json", "r") as f:
        accountsDict = json.load(f)
    
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username not in accountsDict and validPassword(password):
            accountsDict[username] = {"Password": password, "AccountType" : "newPlayer", "LocationX": 12, "LocationY": 12}
            global data
            data = "{'" + str(username) + "': " + str(accountsDict[username]) + "}"
            with open("newCycle1/static/accounts.json", "w") as f:
                json.dump(accountsDict, f, indent=4)
            return redirect("/index")
        
        elif username in accountsDict:
            error = 'Username already exists. Please try again.'
        else:
            error = 'Password is invalid. Please try again.'
    return render_template('signup.html', error=error)

app.run(host='0.0.0.0', port=81, debug=True)

