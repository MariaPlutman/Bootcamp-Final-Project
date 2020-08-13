from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User, Request, Project, Client 

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth_blueprint import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main_blueprint import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app