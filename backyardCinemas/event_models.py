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
    # Necessary Details according to task sheet: Image, descrition, date, "other specific information"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(400), nullable=False)
    max_tickets = db.Column(db.Integer, nullable=False)
    # From the task sheet: "In addition,
    # an event must have one of the following states: Upcoming, Inactive, Booked,
    # or Cancelled."
    # Longest word is 9 long, may as well store value as string(10). Default to Upcoming.
    status = db.Column(db.String(10), nullable=False, default="Upcoming")
    # Just shy of 512 for description
    description = db.Column(db.String(500))
    startDate = db.Column(db.DateTime)
    duration = db.Column(db.DateTime)
    location = db.Column(db.String(128), nullable=False)
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
# Removed "create_ticket" idea, makes no sense. Tickets are created upon purchase, the amount of tickets that exists
# is defined by the event's max ticket count on event creation.
# Purchase Tickets - Handled by /buy_tickets route in event_views.py
#
# Ticket Relationships:
# Ticket is held by events. A ticket can only relate to one event, an event can have many tickets. One to Many.
# Ticket is sold in order. A ticket can only be in one order, an order can have many tickets. One to Many.


class Ticket(db.Model):
    __tablename__ = 'tickets'
    # Necessary Details
    id = db.Column(db.Integer, primary_key=True)
    # Using "Numeric(15,2)" for money data type acording to stackoverflow
    # "SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively" - Deciding to use a String(5) for price. Will discuss with group.
    price = db.Column(db.String(5), nullable=False)
    # Foreign Relationships
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=True)
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
    # Necessary Details
    id = db.Column(db.Integer, primary_key=True)
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
# Generate Order - Handled by /buy_tickets route in events_view.py
#
# Order Relationships:
# Order contains tickets. An order can have many tickets. A ticket can only be in one order. Many to One.
# Order is served to user. An order can be served to only one user. A user can be served many orders. One to Many.


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    # Necessary Details - Set ticket amount to 1 in case customer forget to set number
    # Removed "Ticket Amount" field. Makes no sense - it's redundant information and can cause merge issues.
    # Ticket amount will be a call to how many tickets are assigned to this order within /create_order
    # (User buys ticket > Order is created > Ticket is created, then assigned to Order.)
    # Relationships with other tables
    tickets = db.relationship('Ticket', backref='Order')
    # Foreign Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        format_string = '<Order object {}, Amount: {}>'
        return format_string.format(self.id, self.ticket_amount)
