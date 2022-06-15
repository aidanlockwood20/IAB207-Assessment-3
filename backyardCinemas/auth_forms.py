from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, ValidationError
from re import search

# Register Form Validators


def contact_validator(form, field):
    print(field.data)
    print(search("[^0-9+ ]", field.data))
    if len(field.data) > 20:
        raise ValidationError('Contact Number Must Be Shorter Than 20 Digits')
    elif search("[^0-9+ ]", field.data) != None:
        raise ValidationError('Contact Number Must Contain Numbers')

    # Form used to register users


class RegistrationForm(FlaskForm):

    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email_address = StringField('Email Address', validators=[
                                InputRequired(), Email()])
    contact_number = StringField(
        'Contact Number', validators=[InputRequired(), contact_validator])

    address = StringField('Home Address', validators=[InputRequired()])
    password1 = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField('Confirm Password', validators=[
                              InputRequired(), EqualTo('password1', message='Passwords Must Match!')])
    submit = SubmitField('Sign Up!')

# Form used to login users


class LoginForm(FlaskForm):

    email_address = StringField('Email Address', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
