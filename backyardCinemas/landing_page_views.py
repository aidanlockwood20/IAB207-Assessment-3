from flask import Blueprint, render_template
from . import db
from .auth_models import User
from .event_models import Event, Ticket, Comment

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():

    users = User.query.all()
    events = Event.query.all()
    tickets = Ticket.query.all()
    comments = Comment.query.all()
    return render_template('index.html')
