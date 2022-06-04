from . import db
from datetime import datetime

#
# Event Functions:
# Create Event - Handled by /create_event route in event_views.py
# Update Event - Handled by /update_event route in event_views.py
# Delete Event - Handled by /delete_event route in event_views.py
#
# Event Relationships:
# Event is created by a user. An event can only be created by one user, a user can create many events. One to Many.
# Event is appended with a comment. An event can have multiple comments, a comment can only relate to one event. Many to One.
# Event has tickets. An event can have many tickets, a ticket can only relate to one event. Many to One.


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

#
# Ticket Functions:
# Generate Tickets - Handled by /create_tickets route in event_views.py
# Purchase Tickets - Handled by /buy_tickets route in event_views.py
#
# Ticket Relationships:
# Ticket is held by events. A ticket can only relate to one event, an event can have many tickets. One to Many.
# Ticket is sold in order. A ticket can only be in one order, an order can have many tickets. One to Many.


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details
    name = db.Column(db.String(80), nullable=False)
    # Using "Numeric(15,2)" for money data type acording to stackoverflow
    # "SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively" - Deciding to use a String(5) for price. Will discuss with group.
    price = db.Column(db.String(5), nullable=False)
    # Relationships with other tables
    # orders = db.relationship('Order', backref='Ticket')
    # Foreign Relationships
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        format_string = '<Ticket object {}, Name: {}, Price: {}>'
        return format_string.format(self.id, self.name, self.price)

#
# Comment Functions:
# Create Comment - Handled by /create_comment route in event_views.py
# Delete Comment - Handled by /delete_comment route in event_views.py
#
# Comment Relationships:
# Comment is created by a user. A comment can only have one user, a user can create many comments. One to Many.
# Comment is created on an event. A comment can only be on one event, an event can have many comments. One to Many.


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

#
# Order Functions:

#
# Order Relationships:


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details - Set ticket amount to 1 in case customer forget to set number
    ticket_amount = db.Column(db.Integer, nullable=False, default=1)
    # Relationships with other tables
    tickets = db.relationship('Ticket', backref='Order')
    # Foreign Relationships
    # ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        format_string = '<Order object {}, Amount: {}>'
        return format_string.format(self.id, self.ticket_amount)
