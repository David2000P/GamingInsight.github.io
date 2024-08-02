from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, URL, ValidationError
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    password2 = PasswordField('Passwort wiederholen', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Bitte verwenden Sie einen anderen Benutzernamen.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Bitte verwenden Sie eine andere E-Mail-Adresse.')

class LoginForm(FlaskForm):
    username_or_email = StringField('Benutzername oder E-Mail', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Eingeloggt bleiben')
    submit = SubmitField('Einloggen')


class CompanyRegistrationForm(FlaskForm):
    company_name = StringField('Name des Unternehmens', validators=[DataRequired()])
    company_description = TextAreaField('Beschreibung', validators=[DataRequired()])
    company_website = StringField('Webseite', validators=[DataRequired()])
    submit = SubmitField('Jetzt registrieren')

    def validate_company_website(self, field):
        if not field.data.startswith(('http://', 'https://')):
            field.data = 'http://' + field.data
        try:
            URL()(None, field)
        except ValidationError:
            raise ValidationError('Ungültige URL')

class CompanyLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CompanyEditForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    company_description = TextAreaField('Company Description', validators=[DataRequired()])
    company_website = StringField('Company Website', validators=[DataRequired(), URL()])
    submit = SubmitField('Update')

class ReviewForm(FlaskForm):
    role = SelectField('Rolle', choices=[
        ('dev', 'Entwickler'), ('manager', 'Manager'), 
        ('game_designer', 'Game Designer'), ('level_designer', 'Level Designer'),
        ('programmer', 'Programmierer'), ('ui_ux_designer', 'UI/UX Designer'),
        ('artist_animator', 'Artist/Animator'), ('sound_designer', 'Sound Designer'),
    ], validators=[DataRequired()])
    category = SelectField('Kategorie', choices=[
        ('worklife', 'Work-Life-Balance'), ('pay', 'Bezahlung'),
        ('teamwork', 'Teamarbeit'), ('project_dynamics', 'Projektdynamik'),
        ('work_environment', 'Arbeitsumgebung'), ('tech_ressources', 'Technologische Ressourcen'),
        ('creative_freedom', 'Kreative Freiheit')
    ], validators=[DataRequired()])
    rating = SelectField('Bewertung', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    comments = TextAreaField('Kommentare', validators=[DataRequired()])
    submit = SubmitField('Bewertung absenden')
