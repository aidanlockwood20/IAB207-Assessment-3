from flask_wtf import FlaskForm
from wtforms.fields import TimeField, TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

# Create new event


class EventForm(FlaskForm):
    name = StringField('Event name/Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description',
                                validators=[InputRequired()])
    startDate = DateTimeField('Date', validators=[InputRequired()])
    duration = SelectField('Duration of movie', choices=[(
        '', 'Choose a time'), ('30', '30 Minutes')], validators=[InputRequired()])
    location = StringField('Event Location', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    max_tickets = IntegerField(
        'Number of tickets', validators=[InputRequired()])
    status = SelectField('Event status', choices=[('', 'Choose a status'), ('Upcoming', 'Upcoming'), ('Inactive', 'Inactive'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled')], validators=[InputRequired()], render_kw={
                         "placeholder": "Choose a status"})
    submit = SubmitField("Create")

# User comment form


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')
