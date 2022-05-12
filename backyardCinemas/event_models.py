from . import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    # Details necessary according to task sheet: Image, descrition, date, "other specific information"
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(400), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.DateTime)
    # Relationships with other tables
    comments = db.relationship('Comment', backref='Event')


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    # Details necessary
    name = db.Column(db.String(80), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    # DN
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # Foreign Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
