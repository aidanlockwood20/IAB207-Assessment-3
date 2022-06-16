from flask import Blueprint, request, render_template, redirect, url_for, flash
from .event_models import Event

from . import db
from .event_models import Event, Comment

from .event_models import Event

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():

    events_obj = Event.query.all()
    return render_template('index.html', events=events_obj)


@main_bp.route('/search')
def search():
    if request.args['search']:
        regex_results = f'%{request.args["search"]}%'
        search_query = request.args["search"]

        events = Event.query.filter(
            Event.name.like(regex_results)).all()
    else:
        return redirect(url_for('main.index'))

    return render_template('search.html', query = search_query, results = events)
