from flask import render_template, redirect, url_for, flash, request, abort, Blueprint, current_app
from .forms import LoginForm, RegistrationForm, CompanyRegistrationForm, CompanyLoginForm, CompanyEditForm, ReviewForm
from .models import Review, User, Company
from .extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import urlparse as url_parse
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import func
from datetime import datetime
import pytz
from .email import send_confirmation_email
from .email import send_confirmation_email

bp = Blueprint('main', __name__)
local_timezone = pytz.timezone('Europe/Berlin')

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
        send_confirmation_email(user)
        flash('Ein Bestätigungslink wurde an Ihre E-Mail-Adresse gesendet.', 'info')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(
            (User.email == form.username_or_email.data) |
            (User.username == form.username_or_email.data)
        ).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            if not user.confirmed:
                flash('Bitte bestätigen Sie zuerst Ihre E-Mail-Adresse.', 'warning')
                return redirect(url_for('main.login'))
            login_user(user, remember=form.remember_me.data)
            flash(f'Willkommen {user.username}', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        flash('Email oder Passwort falsch.', 'error')
    return render_template('login.html', form=form)



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sie wurden erfolgreich abgemeldet.', 'success')
    return redirect(url_for('main.index'))

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('search', '')
    companies = Company.query.filter(Company.name.like(f'%{query}%')).all()

    company_data = []
    for company in companies:
        total_reviews = Review.query.filter_by(company_id=company.id).count()
        total_rating = db.session.query(func.avg(Review.rating)).filter(Review.company_id == company.id).scalar()
        total_rating_stars = rating_to_stars(total_rating) if total_rating else "Noch keine Bewertung"

        company_data.append({
            'company': company,
            'total_reviews': total_reviews,
            'total_rating_stars': total_rating_stars
        })

    return render_template('search_results.html', company_data=company_data, query=query)

@bp.route('/companies')
def companies():
    companies = Company.query.all()

    company_data = []
    for company in companies:
        total_reviews = Review.query.filter_by(company_id=company.id).count()
        total_rating = db.session.query(func.avg(Review.rating)).filter(Review.company_id == company.id).scalar()
        total_rating_stars = rating_to_stars(total_rating) if total_rating else "Noch keine Bewertung"

        company_data.append({
            'company': company,
            'total_reviews': total_reviews,
            'total_rating_stars': total_rating_stars
        })

    return render_template('companies.html', company_data=company_data)

def rating_to_stars(rating):
    """ Konvertiert numerische Bewertungen in Sterne """
    if rating is not None:
        return '★' * int(rating) + '☆' * (5 - int(rating))
    return 'Noch keine Bewertung'

@bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@bp.route('/register_company', methods=['GET', 'POST'])
@login_required
def register_company():
    form = CompanyRegistrationForm()
    if form.validate_on_submit():
        company = Company(
            name=form.company_name.data,
            description=form.company_description.data,
            website=form.company_website.data,
            user_id=current_user.id  # User-ID hinzufügen
        )
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

@bp.route('/company/<int:company_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_company(company_id):
    company = Company.query.get_or_404(company_id)
    if company.user_id != current_user.id:
        abort(403)
    form = CompanyEditForm(obj=company)
    if form.validate_on_submit():
        company.name = form.company_name.data
        company.description = form.company_description.data
        company.website = form.company_website.data
        db.session.commit()
        flash('Company updated successfully.')
        return redirect(url_for('main.my_companies'))
    return render_template('edit_company.html', form=form, company=company)

@bp.route('/company/<int:company_id>')
def company_detail(company_id):
    company = Company.query.get_or_404(company_id)
    role_descriptions = {
        'dev': 'Entwickler',
        'manager': 'Manager',
        'game_designer': 'Game Designer',
        'programmer': 'Programmierer',
        'ui_ux_designer': 'UI/UX Designer',
        'artist_animator': 'Artist/Animator',
        'sound_designer': 'Sound Designer',
    }
    category_descriptions = {
        'worklife': 'Work-Life-Balance',
        'pay': 'Bezahlung',
        'teamwork': 'Teamarbeit',
        'work_environment': 'Arbeitsumgebung',
        'tech_ressources': 'Technologische Ressourcen',
        'project_dynamics': 'Projektdynamik',
        'creative_freedom': 'Kreative Freiheit'
    }

    # Durchschnittsbewertung und Anzahl der Bewertungen für jede Kategorie berechnen
    category_ratings = db.session.query(
        Review.category,
        func.avg(Review.rating).label('average'),
        func.count(Review.id).label('count')
    ).filter(Review.company_id == company_id).group_by(Review.category).all()

    # Gesamtdurchschnittsbewertung und Anzahl berechnen
    total_average_rating = db.session.query(func.avg(Review.rating)).filter(Review.company_id == company_id).scalar()
    total_review_count = db.session.query(func.count(Review.id)).filter(Review.company_id == company_id).scalar()

    # Durchschnittsbewertungen und Anzahl in ein Dictionary umwandeln
    avg_ratings_dict = {category: {'average': round(avg, 2), 'count': count} for category, avg, count in category_ratings}

    # Hinzufügen von Kategorien ohne Bewertungen
    for category in category_descriptions.keys():
        if category not in avg_ratings_dict:
            avg_ratings_dict[category] = {'average': 0.0, 'count': 0}

    # Durchschnittsbewertungen sortieren
    sorted_avg_ratings = sorted(
        avg_ratings_dict.items(),
        key=lambda x: x[1]['average'],
        reverse=True
    )

    # Gesamtdurchschnitt in Sterne umwandeln
    total_average_stars = rating_to_stars(total_average_rating) if total_average_rating else "Noch keine Bewertung"

    return render_template(
        'company_detail.html',
        company=company,
        role_descriptions=role_descriptions,
        category_descriptions=category_descriptions,
        sorted_avg_ratings=sorted_avg_ratings,
        total_average_stars=total_average_stars,
        total_review_count=total_review_count,
        rating_to_stars=rating_to_stars
    )

@bp.route('/submit_review/<int:company_id>', methods=['GET', 'POST'])
@login_required
def submit_review(company_id):
    company = Company.query.get_or_404(company_id)
    form = ReviewForm()
    if form.validate_on_submit():
        existing_review = Review.query.filter_by(user_id=current_user.id, company_id=company_id, category=form.category.data).first()
        if existing_review:
            flash('Sie haben dieses Unternehmen in dieser Kategorie bereits bewertet.', 'error')
            return redirect(url_for('main.company_detail', company_id=company_id))
        review = Review(
            comments=form.comments.data,
            rating=form.rating.data,
            role=form.role.data,
            category=form.category.data,
            user_id=current_user.id,
            company_id=company_id,
            timestamp=datetime.now(local_timezone)  # Set timestamp with local timezone
        )
        db.session.add(review)
        db.session.commit()
        flash('Vielen Dank für deine Bewertung!', 'success')
        return redirect(url_for('main.company_detail', company_id=company_id))
    return render_template('review_form.html', form=form, company=company)

@bp.route('/delete_review/<int:review_id>', methods=['POST'])
@login_required
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    company_id = review.company_id
    # Überprüfen, ob der aktuelle Benutzer der Autor der Bewertung ist oder ein Administrator ist
    if review.author != current_user:
        flash('You do not have permission to delete this review.')
        return redirect(url_for('main.company_detail', company_id=company_id))
    
    db.session.delete(review)
    db.session.commit()
    flash('Review deleted successfully.', 'success')
    return redirect(request.referrer or url_for('main.index'))

@bp.route('/my_reviews')
@login_required
def my_reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    role_descriptions = {
        'dev': 'Entwickler',
        'manager': 'Manager',
        'game_designer': 'Game Designer',
        'level_designer': 'Level Designer',
        'programmer': 'Programmierer',
        'ui_ux_designer': 'UI/UX Designer',
        'artist_animator': 'Artist/Animator',
        'sound_designer': 'Sound Designer',
    }
    category_descriptions = {
        'worklife': 'Work-Life-Balance',
        'pay': 'Bezahlung',
        'teamwork': 'Teamarbeit',
        'work_environment': 'Arbeitsumgebung',
        'tech_ressources': 'Technologische Ressourcen',
        'project_dynamics': 'Projektdynamik',
        'creative_freedom': 'Kreative Freiheit',
    }
    return render_template('my_reviews.html', reviews=reviews, role_descriptions=role_descriptions, category_descriptions=category_descriptions, rating_to_stars=rating_to_stars)

@bp.route('/my_companies')
@login_required
def my_companies():
    companies = Company.query.filter_by(user_id=current_user.id).all()
    return render_template('my_companies.html', companies=companies)

# Route to delete a company
@bp.route('/company/<int:company_id>/delete', methods=['POST'])
@login_required
def delete_company(company_id):
    company = Company.query.get_or_404(company_id)
    if company.user_id != current_user.id:
        abort(403)
    db.session.delete(company)
    db.session.commit()
    flash('Company deleted successfully.')
    return redirect(url_for('main.my_companies'))

@bp.route('/confirm_email/<token>')
def confirm_email(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('Das ist ein ungültiger oder abgelaufener Token', 'warning')
        return redirect(url_for('main.index'))
    user.confirmed = True
    db.session.commit()
    flash('Ihre E-Mail-Adresse wurde bestätigt.', 'success')
    return render_template('confirm_link.html')


