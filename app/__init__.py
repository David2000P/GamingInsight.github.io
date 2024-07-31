from flask import Flask
from .extensions import db, migrate, login_manager
from .models import User

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    app.config['SECRET_KEY'] = 'hier_dein_sehr_starker_geheimer_schlüssel'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insightjob.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Umleiten auf Login-Seite, wenn nicht eingeloggt

    from .routes import bp
    app.register_blueprint(bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app 
