from flask import Blueprint, render_template, request, flash
import pymongo

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    #authentication from database and redirect
    username = request.form.get('username')
    password = request.form.get('password')
    #print(username)
    #print(password)

    return render_template("login.html")

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    #Authentication, database insertion and redirection
    client = pymongo.MongoClient("mongodb+srv://unity:unity@users.lalm7.mongodb.net/users?retryWrites=true&w=majority")
    db = client.test

    username = request.form.get('username')
    password = request.form.get('password')

    if username and password:
        if db.users.find_one({"user":username}):
            return render_template("signup.html", error="Username already exists.")
        else:
            db.users.insert_one({'user': username, 'pw': password})
            return render_template("dashboard.html")
    else:
        return render_template("signup.html", error="Please fill all fields.")

    return render_template("signup.html")