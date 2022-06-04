from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#Create new event
class EventForm(FlaskForm):
  name = StringField('Event name/Movie Title', validators=[InputRequired()])
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  date = DateTimeField('Date', validators=[InputRequired()])
  image = FileField('Event Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  submit = SubmitField("Create")
  
#User comment form
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')
