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

    return render_template('index.html')


@main_bp.route('/search')
def search():
    if request.args['search']:
        search_results = request.args["search"]

        events = Event.query.filter(
            Event.description.like(search_results)).all()
        return render_template('search.html', results=search_results)
