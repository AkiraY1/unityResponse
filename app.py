from flask import Flask, render_template, url_for, redirect, request, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")