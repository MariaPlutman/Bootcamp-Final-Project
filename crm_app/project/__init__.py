from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import flask_migrate
import flask_mail
import os

db = SQLAlchemy()
migrate = flask_migrate.Migrate()
login_mgr = LoginManager()
mail_mgr  = flask_mail.Mail()


def create_app():
    from .config import config

    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config[env])

    db.init_app(app)
    login_mgr.login_view = 'auth.login'
    login_mgr.init_app(app)
    migrate.init_app(app, db)
    mail_mgr.init_app(app)

    from .models import User, Request

    @login_mgr.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth_blueprint import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main_blueprint import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
