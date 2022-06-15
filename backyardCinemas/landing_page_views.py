from flask import Blueprint, request, render_template
from flask_login import current_user

from . import db
from .auth_models import User
from .event_models import Event, Ticket, Comment

from .event_models import Event

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    print(current_user.is_authenticated)
    
    users = User.query.all()
    events = Event.query.all()
    tickets = Ticket.query.all()
    comments = Comment.query.all()
    return render_template('index.html')

@main_bp.route('/search')
def search():
    if request.args['search']:
        regex_query = f'%{request.args["search"]}%'
        search_results = request.args["search"]
        events = Event.query.filter(Event.name.like(regex_query)).all()
        print(events)
        return render_template('search.html', query = search_results, results = events)