from flask import render_template, redirect, url_for, flash, request, Blueprint
from .forms import LoginForm, RegistrationForm, CompanyRegistrationForm
from .models import Review, User, Company
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

bp = Blueprint('main', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/register_company', methods=['GET', 'POST'])
@login_required
def register_company():
    form = CompanyRegistrationForm()
    if form.validate_on_submit():
        print("Form validated")  # Debug output
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        print(f"User {user.username} registered")  # Debug output
        company = Company(
            name=form.company_name.data,
            description=form.company_description.data,
            website=form.company_website.data,
            user_id=user.id
        )
        db.session.add(company)
        db.session.commit()
        print(f"Company {company.name} registered")  # Debug output
        login_user(user)
        flash('Company registration successful.')
        return redirect(url_for('main.index'))
    return render_template('register_company.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        flash('Invalid email or password')
    return render_template('login.html', title='Login', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sie wurden erfolgreich abgemeldet.')
    return redirect(url_for('main.index'))

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/top_reviews')
@login_required
def top_reviews():
    reviews = Review.query.order_by(Review.rating.desc()).limit(10)
    return render_template('top_reviews.html', reviews=reviews)

@bp.route('/categories')
@login_required
def categories():
    categories = ["Entwickler", "Publisher", "Hardware", "Zubehör"]
    return render_template('categories.html', categories=categories)

@bp.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('search')
    if query:
        companies = Company.query.filter(Company.name.like('%' + query + '%')).all()
        return render_template('search_results.html', companies=companies, query=query)
    else:
        flash("Bitte geben Sie einen Suchbegriff ein.")
        return redirect(url_for('main.index'))

@bp.route('/companies')
@login_required
def companies():
    companies = Company.query.all()
    return render_template('companies.html', companies=companies)

@bp.route('/users')
def users():
    users = User.query.all()  # Abfragen aller Benutzer
    return render_template('users.html', users=users)
