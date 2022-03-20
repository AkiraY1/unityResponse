from flask import Blueprint, render_template, request, flash, redirect, url_for
import pymongo
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    client = pymongo.MongoClient("mongodb+srv://unity:unity@users.lalm7.mongodb.net/users?retryWrites=true&w=majority")
    db = client.test

    if username and password:
        if db.users.find_one({"user":username, "pw": password}):
            return redirect(url_for('main.dashboard', username=username))
        else:
            return render_template("login.html", error="Incorrect username or password")
    else:
        return render_template("login.html", error="Please fill all fields.")

    return render_template("login.html")

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    client = pymongo.MongoClient("mongodb+srv://unity:unity@users.lalm7.mongodb.net/users?retryWrites=true&w=majority")
    db = client.test

    if username and password:
        if db.users.find_one({"user":username}):
            return render_template("signup.html", error="Username already exists.")
        else:
            db.users.insert_one({'user': username, 'pw': password})
            return redirect(url_for('auth.login'))
    else:
        return render_template("signup.html", error="Please fill all fields.")

    return render_template("signup.html")