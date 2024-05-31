from app import create_app
from app.models import User
from app.extensions import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)