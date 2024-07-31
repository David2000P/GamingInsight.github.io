from flask import render_template, redirect, url_for, flash, request, Blueprint
from .forms import LoginForm, RegistrationForm, CompanyRegistrationForm, CompanyLoginForm, CompanyEditForm
from .models import Review, User, Company
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

bp = Blueprint('main', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
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

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)

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


@bp.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('search', '')
    companies = Company.query.filter(Company.name.like(f'%{query}%')).all()
    return render_template('search_results.html', companies=companies, query=query)

@bp.route('/companies')
def companies():
    companies = Company.query.all()
    return render_template('companies.html', companies=companies)

@bp.route('/users')
def users():
    users = User.query.all()  # Query all users
    return render_template('users.html', users=users)

@bp.route('/company/<int:company_id>')
@login_required
def company_detail(company_id):
    company = Company.query.get_or_404(company_id)
    return render_template('company_detail.html', company=company)

@bp.route('/register_company', methods=['GET', 'POST'])
@login_required
def register_company():
    form = CompanyRegistrationForm()
    if form.validate_on_submit():
        company = Company(
            name=form.company_name.data,
            description=form.company_description.data,
            website=form.company_website.data,
            email=form.email.data
        )
        company.set_password(form.password.data)
        db.session.add(company)
        db.session.commit()
        flash('Company registration successful.')
        return redirect(url_for('main.companies'))
    return render_template('register_company.html', form=form)

@bp.route('/company_login', methods=['GET', 'POST'])
def company_login():
    form = CompanyLoginForm()
    if form.validate_on_submit():
        company = Company.query.filter_by(email=form.email.data).first()
        if company and company.check_password(form.password.data):
            login_user(company, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.company_detail', company_id=company.id)
            return redirect(next_page)
        else:
            flash('Invalid email or password')
    return render_template('company_login.html', form=form)

@bp.route('/edit_company/<int:company_id>', methods=['GET', 'POST'])
@login_required
def edit_company(company_id):
    company = Company.query.get_or_404(company_id)
    if company.user_id != current_user.id:
        flash('You do not have permission to edit this company.')
        return redirect(url_for('main.index'))

    form = CompanyEditForm(obj=company)
    if form.validate_on_submit():
        company.name = form.company_name.data
        company.description = form.company_description.data
        company.website = form.company_website.data
        db.session.commit()
        flash('Company updated successfully.')
        return redirect(url_for('main.company_detail', company_id=company.id))
    return render_template('edit_company.html', form=form, company=company)

@bp.route('/review/<int:company_id>', methods=['POST'])
@login_required
def submit_review(company_id):
    # Daten aus dem Formular extrahieren
    culture = request.form['culture']
    work_life_balance = request.form['work_life_balance']
    career_opportunities = request.form['career_opportunities']
    technology = request.form['technology']
    compensation = request.form['compensation']
    community = request.form['community']
    comments = request.form['comments']

    # Review-Objekt erstellen und in der Datenbank speichern
    review = Review(
        culture=culture,
        work_life_balance=work_life_balance,
        career_opportunities=career_opportunities,
        technology=technology,
        compensation=compensation,
        community=community,
        comments=comments,
        user_id=current_user.id,
        company_id=company_id
    )
    db.session.add(review)
    db.session.commit()
    flash('Deine Bewertung wurde erfolgreich gespeichert.')
    return redirect(url_for('main.company_detail', company_id=company_id)) 
