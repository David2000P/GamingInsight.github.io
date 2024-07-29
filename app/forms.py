from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(1000))
    website = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Beziehung zum Benutzer hinzufügen
    user = db.relationship('User', backref='companies')
    reviews = db.relationship('Review', backref='company', lazy='dynamic')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    culture = db.Column(db.Integer)  # Bewertung für Arbeitskultur
    work_life_balance = db.Column(db.Integer)  # Bewertung für Work-Life-Balance
    career_opportunities = db.Column(db.Integer)  # Bewertung für Karrierechancen
    technology = db.Column(db.Integer)  # Bewertung für Technologie
    compensation = db.Column(db.Integer)  # Bewertung für Vergütung
    community = db.Column(db.Integer)  # Bewertung für Gemeinschaft
    comments = db.Column(db.String(1000))  # Freitextkommentare
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


