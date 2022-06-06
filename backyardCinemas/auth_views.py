# Flask module imports
from distutils.log import Log
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from . import db

# Form and Model imports
from .auth_forms import RegistrationForm, LoginForm
from .auth_models import User

# Authentication endpoint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# View to register new users


@auth_bp.route('/register', methods=['GET', 'POST'])
def registration_view():

    # Registration form to be used
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        print('Form submit')

        # Gather the data from the form
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data
        email_address = register_form.email_address.data
        password = register_form.password1.data

        # Check if user exists
        u1 = User.query.filter_by(email_address=email_address).first()
        if u1:
            flash('User name already exists, please login')
            return redirect(url_for('auth.login'))
        # Generate the password hash to be saved into the db
        password_hashed = generate_password_hash(password)

        # Create new instance of the user to be saved into the database
        user = User(first_name=first_name, last_name=last_name,
                    email_address=email_address, password_hash=password_hashed)

        # Add DB commit to put new user into the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login_view'))
    else:
        return render_template('auth/authenticate.html', form=register_form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_view():

    form = LoginForm()

    error = None
    
    if form.validate_on_submit():

        # Debug code to check whether the if conditional works 
        print('Form submit')

        email_address = form.email_address.data
        password = form.password.data

        user_query = User.query.filter_by(email_address=email_address).first()

        # if user is none, assume invalid email address
        if user_query is None:
            error = 'Invalid Email Address. Try Again'
        # If user is correct but password incorrect, return invalid password
        elif not check_password_hash(user_query.password_hash, password):
            error = 'Incorrect Password. Try Again'
        # No errors - log user in 
        if error is None:
            login_user(user_query)
            # Back-end feedback for user logging in (Useful pre-development of functional navbar)
            print('User successfully logged in!')
            return redirect(url_for('main.index'))
        print(error)
        flash(error)

    return render_template('auth/authenticate.html', form = form)


@auth_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout_view():
    # Front-end feedback for user logging out
    user_logout = 'Successfully logged out'
    # Flash message on main page. If url_for(main.index) does not flash the message,
    # then the next page that flashes a message will double-flash, with this as its first message.
    flash(user_logout)
    # Log user out, then return them to homepage.
    logout_user()
    return redirect(url_for('main.index'))
