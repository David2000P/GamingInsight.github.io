from flask import Flask
from db import init_app

app = Flask(__name__)
app.config['DATABASE'] = 'instance/database.sqlite'

init_app(app)
