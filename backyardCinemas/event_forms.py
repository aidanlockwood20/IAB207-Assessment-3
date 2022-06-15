from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField, TimeField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed
from .event_models import Event, Comment
from .event_models import Event
from . import db

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#Create new event
class EventForm(FlaskForm):
  name = StringField('Event name/Movie Title', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  startDate = DateTimeField('Date', validators=[InputRequired()])
  duration = TimeField('Duration of movie', validators=[InputRequired()])
  location = StringField('Event Location', validators=[InputRequired()])
  image = FileField('Event Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  max_tickets = IntegerField('Number of tickets', validators=[InputRequired()])
  status = StringField('Event status', validators=[InputRequired()], render_kw={"placeholder": "Please list as either Upcoming, Inactive, Booked, or Cancelled."})
  submit = SubmitField("Create")
  
#User comment form
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')