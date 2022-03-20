from flask import Flask, render_template, url_for, redirect, request, send_from_directory, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/dashboard/<string:username>')
def dashboard(username: str):
    return render_template("dashboard.html", name=username)