from . import db
from flask_login import UserMixin

# User Model for the web application
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    email_address = db.Column(db.String(128), unique=True, nullable=True)
    password_hash = db.Column(
        db.String(255), nullable=False, default='password1')

    def __repr__(self):
        format_string = '<User object {}, Name: {} {}, Email Address: {}>'
        return format_string.format(self.id, self.first_name, self.last_name, self.email_address)
