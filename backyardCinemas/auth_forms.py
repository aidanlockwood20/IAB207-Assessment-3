from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo

### WILL REFACTOR THIS CODE TO ONE FORM 

# Form used to register users
class RegistrationForm(FlaskForm):

    first_name = StringField('First Name', validators = [InputRequired()])
    last_name = StringField('Last Name', validators = [InputRequired()])
    email_address = StringField('Email Address', validators = [InputRequired(), Email()])
    password1 = PasswordField('Password', validators = [InputRequired()])
    password2 = PasswordField('Confirm Password', validators = [InputRequired(), EqualTo('password1', message = 'Passwords Must Match!')])
    submit = SubmitField('Sign Up!')

# Form used to login users
class LoginForm(FlaskForm):

    email_address = StringField('Email Address', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Login')