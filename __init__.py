from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'bytemsters.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gdyjhenujb dncmnjvn dx'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views , url_prefix = '/')
    app.register_blueprint(auth , url_prefix = '/')
    app.register_blueprint(admin , url_prefix = '/')

    from .models import User, Product

    create_database(app)
    login_manager = LoginManager()
    #where do we need to go if we are not logged in?
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # if not path.exists("website" + DB_NAME):

    with app.app_context():
        db.create_all()
        print('database created successfully')
