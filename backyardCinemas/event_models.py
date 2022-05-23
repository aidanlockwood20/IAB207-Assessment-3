from . import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details according to task sheet: Image, descrition, date, "other specific information"
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(400), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.DateTime)
    # Foreign Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Relationships with other tables
    comments = db.relationship('Comment', backref='Event')
    tickets = db.relationship('Ticket', backref='Event')

    def __repr__(self):
        format_string = '<Event object {}, Name: {}, Image: {}, Description: {}, Date: {}>'
        return format_string.format(self.id, self.name, self.image, self.description, self.date)


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details
    name = db.Column(db.String(80), nullable=False)
    # Using "Numeric(15,2)" for money data type acording to stackoverflow
    # "SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively" - Deciding to use a String(5) for price. Will discuss with group.
    price = db.Column(db.String(5), nullable=False)
    # Relationships with other tables
    orders = db.relationship('Order', backref='Ticket')
    # Foreign Relationships
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        format_string = '<Ticket object {}, Name: {}, Price: {}>'
        return format_string.format(self.id, self.name, self.price)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details
    text = db.Column(db.String(400), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # Foreign Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        format_string = '<Comment object {}, Text: {}, Created At: {}>'
        return format_string.format(self.id, self.text, self.created_at)


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details - Set ticket amount to 1 in case customer forget to set number
    ticket_amount = db.Column(db.Integer, nullable=False, default=1)
    # Foreign Relationships
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        format_string = '<Order object {}, Amount: {}>'
        return format_string.format(self.id, self.ticket_amount)
