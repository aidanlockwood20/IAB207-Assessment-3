from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, IntegerField, DateField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange
from flask_wtf.file import FileRequired, FileField, FileAllowed
from .event_models import Event, Comment
from .event_models import Event
from . import db

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

# Create new event


class EventForm(FlaskForm):
    name = StringField('Event name/Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description',
                                validators=[InputRequired()])
    startDate = DateField('Date', validators=[InputRequired()])
    duration = IntegerField('Duration of movie (mins)',
                            validators=[InputRequired(), NumberRange(min=1)])
    location = StringField('Event Location', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    max_tickets = IntegerField(
        'Number of tickets', validators=[InputRequired(), NumberRange(min=1, message='Must select more than zero tickets')])
    cost = IntegerField('Cost per ticket', validators=[InputRequired(), NumberRange(min=1)], render_kw={
                        "placeholder": "Please enter an amount in dollars ($)"})
    status = SelectField('Event status', choices=[('', 'Choose a Status'), ('Upcoming', 'Upcoming'), (
        'Inactive', 'Inactive'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled')], validators=[InputRequired()])
    submit = SubmitField("Create")

# User comment form


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')
