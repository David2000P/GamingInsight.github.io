from flask_mail import Message
from flask import url_for, current_app, render_template
from .extensions import mail

def send_confirmation_email(user):
    token = user.get_reset_token()
    confirm_url = url_for('main.confirm_email', token=token, _external=True)
    html = render_template('email/confirm_email.html', user=user, confirm_url=confirm_url)
    msg = Message('Confirm Your Email',
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email])
    msg.body = f'''To confirm your email, visit the following link:
{confirm_url}
If you did not make this request, simply ignore this email and no changes will be made.
'''
    msg.html = html
    mail.send(msg)
