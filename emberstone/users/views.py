'''
User views for emberstone
'''

# Imports
from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from emberstone.users.forms import LoginForm
from emberstone.models import User


# Blueprint variable
users_bp = Blueprint('users', __name__)


# Routes
# Login Page
@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    '''Route: Login Page'''
    # Check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))

    # Login form
    form = LoginForm()

    # Validate form
    if form.validate_on_submit and request.method == 'POST':
        # Query database for user
        user = User.query.filter_by(email=form.email.data).first()

        # Check if user exists and password is correct
        if user and check_password_hash(user.password, form.password.data):
            # Log user in
            login_user(user, remember=True)

            # Redirect user to homepage
            return redirect(url_for('core.index'))
        else:
            # Display error message
            flash('Login Unsuccessful. Please check email and password',
                  'danger')

    return render_template('login.html',
                           title='Emberstone - Login',
                           form=form)


# Logout Page
@users_bp.route('/logout')
@login_required
def logout():
    '''Route: Logout Page'''
    # Log user out
    logout_user()

    # Redirect user to login page
    return redirect(url_for('users.login'))
