# Flask module imports
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from . import db

# Form and Model imports
from .auth_forms import RegistrationForm, LoginForm
from .auth_models import User

# Authentication endpoint
auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

# View to register new users
@auth_bp.route('/register', methods = ['GET', 'POST'])
def registration_view():

    # Registration form to be used
    form = RegistrationForm()

    if form.validate_on_submit():
        # Code to check if the if conditional is working 
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

        # log the user in and show flash message
        authenticate_user = User.query.filter_by(email_address = email_address)
        flash('Welcome to backyardCinemas! Please log in!')
        return redirect(url_for('auth.login_view'))

    return render_template('auth/authenticate.html', form = form, title = 'Register New User')

# The view to login the user
@auth_bp.route('/login', methods = ['GET', 'POST'])
def login_view():

    # Form used to login the user
    form = LoginForm()
    
    # Default error value 
    error = None

    if form.validate_on_submit():

        # Debug code to check whether the if conditional works 
        print('Form submit')

        # Get form data
        email_address = form.email_address.data
        password = form.password.data

        # Check db for user
        user_query = User.query.filter_by(email_address = email_address).first()

        # if user is none, assume invalid email address
        if user_query is None:
            error = 'Invalid Email Address. Try Again'
        # If user is correct but password incorrect, return invalid password
        elif not check_password_hash(user_query.password_hash, password):
            error = 'Incorrect Password. Try Again'
        # No errors - log user in 
        if error is None:
            login_user(user_query)
            
            # Display message to user and redirect to homepage
            flash('You have been logged in successfully!')
            return redirect(url_for('main.index'))

        # An error has occurred - display to user
        print(error)
        flash(error)

    return render_template('auth/authenticate.html', form = form, title = 'Login to backyardCinemas')

# Logout user 
@auth_bp.route('/logout', methods = ['GET', 'POST'])
def logout_view():

    logout_user()
    flash('You have been Successfully Logged Out')
    return redirect(url_for('auth.register_view'))