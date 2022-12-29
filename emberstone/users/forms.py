'''
User forms for emberstone
'''

# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# Form - Login
class LoginForm(FlaskForm):
    '''Login form'''
    email = EmailField('Email*',
                       validators=[DataRequired(),
                                   Email()],
                       render_kw={'placeholder': 'Email',
                                  'class': 'form-control'})
    password = PasswordField('Password*',
                             validators=[DataRequired(),
                                         Length(min=6)],
                             render_kw={'placeholder': 'Password',
                                        'class': 'form-control'})
    submit = SubmitField('Login',
                         render_kw={'class': 'btn btn-primary'})
