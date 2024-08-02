from flask import Flask
from .extensions import db, migrate, login_manager, mail
from .models import User
from .config import Config  # Korrigierter Importpfad

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message = 'Bitte melden Sie sich an, um eine Bewertung abzugeben.'
    login_manager.login_message_category = 'error'

    from .routes import bp
    app.register_blueprint(bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
