# Flask module imports
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from . import db
# Form and Model imports
from forms.auth_forms import RegistrationForm, LoginForm
from auth_models import User

# Authentication endpoint
auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

# View to register new users
@auth_bp.route('/register', methods = ['GET', 'POST'])
def registration_view():

    # Registration form to be used
    form = RegistrationForm()

    if form.validate_on_submit():
        print('Form submit')

        # Gather the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        email_address = form.email_address.data
        password = form.password1.data

        # Generate the password hash to be saved into the db
        password_hashed = generate_password_hash(password)

        # Create new instance of the user to be saved into the database
        user = User(first_name = first_name, last_name = last_name, email_address = email_address, password_hash = password_hashed)

        # Add DB commit to put new user into the database
        db.session.add(user)
        db.session.commit()

        # log the user in 
        authenticate_user = User.query.filter_by(email_address = email_address)
        login_user(authenticate_user)

    return render_template('auth/authenticate.html', form = form)

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login_view():

    form = LoginForm()

    if form.validate_on_submit():

        print('Form submit')

        email_address = form.email_address.data
        password = form.password.data

        user_query = User.query.filter_by(email_address = email_address).first()

        if user_query is None:
            error = 'Invalid Email Address. Try Again'
        elif not check_password_hash(user_query.password_hash, password):
            error = 'Incorrect Password. Try Again'
        if error is None:
            login_user(user_query)
        print(error)
        flash(error)

    return render_template('auth/authenticate.html', form = form)

@auth_bp.route('/logout', methods = ['GET', 'POST'])
def logout_view():

    logout_user()
    return redirect(url_for('auth.register_view'))