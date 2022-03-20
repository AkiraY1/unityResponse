from flask import Flask
import pymongo
from . import models

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yoloman'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app