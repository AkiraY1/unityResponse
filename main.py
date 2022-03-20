from flask import Flask, render_template, url_for, redirect, request, send_from_directory, Blueprint
from flask_login import login_user, logout_user, current_user, login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")