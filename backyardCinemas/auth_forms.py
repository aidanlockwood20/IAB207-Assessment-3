from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, widgets
from wtforms.validators import InputRequired, Email, EqualTo

# Form used to register users
class RegistrationForm(FlaskForm):

    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators = [InputRequired()])
    email_address = StringField('Email Address', validators = [InputRequired(), Email()])
    contact_number = StringField('Contact Number', validators = [InputRequired()])
    password1 = PasswordField('Password', validators = [InputRequired()])
    password2 = PasswordField('Confirm Password', validators = [InputRequired(), EqualTo('password1', message = 'Passwords Must Match!')])
    submit = SubmitField('Sign Up!')

# Form used to login users
class LoginForm(FlaskForm):

    email_address = StringField('Email Address', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Login!')