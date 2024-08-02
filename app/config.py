import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'your_password_salt'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///insightjob.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'  # Überprüfe, ob der Mailserver korrekt ist
    MAIL_PORT = 587  # Überprüfe den Port
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False  # Stelle sicher, dass dies korrekt ist
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  # Deine E-Mail-Adresse
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # Dein E-Mail-Passwort

os.environ['EMAIL_USER'] = 'sercanp76@gmail.com'
os.environ['EMAIL_PASS'] = 'urrv qcao vkfz qjdk'