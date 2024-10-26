from flask_login import UserMixin
from wtforms import StringField, PasswordField, validators, SubmitField
from flask_wtf import FlaskForm

"""
User blue prints.
"""
class User(UserMixin):
    """User blueprint storing class."""

    def __init__(self, user_id, user_name, user_mail, user_pass):
        self.id = user_id
        self.name = user_name
        self.email = user_mail
        self.password = user_pass

"""
Flask authentication.
"""

class RegistrationForm(FlaskForm):
    """Blueprint for signup form."""
    name = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    register = SubmitField(label='Register')


class LoginForm(FlaskForm):
    """Blueprint for login form."""
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])