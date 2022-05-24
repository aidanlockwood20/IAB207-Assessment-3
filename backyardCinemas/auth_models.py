from . import db
from flask_login import UserMixin

# User Model for the web application
#
# User Functions:
# Create User - Handled by /register route in auth_views.py
# User login - Handled by /login route in auth_views.py
#
# User Relationships:
# User creates comments. A user can create many comments, a comment can only be created by one user. Many to One.
# User creates events. A user can create many events, an event can only be created by one user. Many to One.
# User receives order. A user can receieve/generate many orders, an order can only be attributed/given to one user. Many to One.
#


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    # Necessary Details
    id = db.Column(db.Integer, primary_key=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email_address = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(
        db.String(255), nullable=False, default='password1')
    contact_number = db.Column(db.VarChar(20), nullable=False)
    address = db.Column(db.String(128), nullable=True)
    # Relationships with other tables
    comments = db.relationship('Comment', backref='User')
    events = db.relationship('Event', backref='User')
    orders = db.relationship('Order', backref='User')

    def __repr__(self):
        format_string = '<User object {}, Name: {} {}, Email Address: {}>'
        return format_string.format(self.id, self.first_name, self.last_name, self.email_address)
