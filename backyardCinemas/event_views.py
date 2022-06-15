
from flask import Blueprint, render_template, request, redirect, url_for
from .event_models import Event, Comment
from .event_forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

bp = Blueprint('event', __name__, url_prefix='/events')


@bp.route('/<id>')
def show(id):
    event = Event.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()
    return render_template('events/show_event.html', event=event, form=cform)

@bp.route('/<event>/comment', methods=['GET', 'POST'])
@login_required
def comment(event):
    form = CommentForm()
    # get the event object associated to the page and the comment
    event_obj = Event.query.filter_by(id=event).first()
    if form.validate_on_submit():
        # read the comment from the form
        comment = Comment(text=form.text.data,
                          Event=event_obj,
                          User=current_user)
        # here the back-referencing works - comment.event is set
        # and the link is created
        db.session.add(comment)
        db.session.commit()

        # flashing a message which needs to be handled by the html
        #flash('Your comment has been added', 'success')
        print('Your comment has been added', 'success')
    # using redirect sends a GET request to event.show
    return redirect(url_for('event.show', id=event))


@bp.route('/create_event', methods=['GET', 'POST'])
@login_required
def create():
    print('Method type: ', request.method)
    form = EventForm()
    if form.validate_on_submit():
        # call the function that checks and returns image
        db_file_path = check_upload_file(form)
        event = Event(name=form.name.data, description=form.description.data,
                      startDate=form.startDate.data, duration=form.duration.data, location=form.location.data, image=db_file_path, max_tickets=form.max_tickets.data, status=form.status.data)
        # add the object to the db session
        db.session.add(event)
        # commit to the database
        db.session.commit()
        print('Successfully created new event', 'success')
        # Always end with redirect when form is valid
        return redirect(url_for('event.create'))
    return render_template('events/create_event.html', form=form)


@bp.route('/purchase_history', methods=['GET', 'POST'])
def purchase_history():
    return render_template('events/purchase_history.html')


def check_upload_file(form):
    # get file data from form
    fp = form.image.data
    filename = fp.filename
    # get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    # upload file location – directory of this file/static/image
    upload_path = os.path.join(
        BASE_PATH, 'static/image', secure_filename(filename))
    # store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/image/' + secure_filename(filename)
    # save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path
