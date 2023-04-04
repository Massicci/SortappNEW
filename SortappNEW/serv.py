from flask import Flask
from flask import render_template
from flask import request
from app.engine import *

server = Flask(__name__)

# Defines blank user (unauthorized)
user = User()
# Defines istance of CLasse (blank class)
# to use in difference requests
selectedclass = Classe()

# Calls render_template method only if the user is logged in
# This is a key functions in order to simplify the code and avoid repetition.
def usertemplate(link, **kwargs):

    if user.authorized:
        return render_template(link, **kwargs)
    else:
        return render_template('/loginfail.html')

# Login (request method: GET)
# Links to index after login
@server.route('/login')
def login():
    if request.method == "GET":
        return render_template("login.html")

@server.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        # Assigns login data and checks authorization
        user.login(request.form['usr'],
                   request.form['psswrd']
                  )
        return usertemplate('/index.html')
    # Request.method == "GET"
    else:
        return usertemplate('/index.html')

@server.route('/classroom', methods=["GET", "POST"])
def show_classroom():

    if request.method == "POST":
        selectedclass.getdata(request.form["classe"])
        return usertemplate('/classroom.html',
                            classe=selectedclass
                           )
    # Request.method == "GET"
    else:
        return usertemplate('/index.html')

@server.route('/sortstudent', methods=["GET", "POST"])
def sortstudent():

    if request.method == "POST":
        return usertemplate('/teststudent.html',
                            classe=selectedclass,
                            stud=selectedclass.randomsort()
               )
    # Request.method == "GET"
    else:
        return usertemplate('/index.html')

@server.route('/decidestudent/', methods=["GET", "POST"])
def decidestudent():

    if request.method == "POST":
        return usertemplate('/teststudent.html',
                            classe=selectedclass,
                            stud=request.form["student"]
               )
    # Request.method == "GET"
    else:
        return usertemplate('/index.html')

@server.route('/assignmark', methods=["GET", "POST"])
def assignmark():

    if request.method == "POST":
        selectedclass.assignmark(request.form["student"],
                                 request.form["mark"]
                      )
        return usertemplate('/index.html')
    # Request.method == "GET"
    else:
        return usertemplate('/index.html')

if __name__ == "__main__":
    server.run()
