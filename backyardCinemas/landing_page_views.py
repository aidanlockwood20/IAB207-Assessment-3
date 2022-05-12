from flask import Blueprint, render_template

from . import db
from .auth_models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():

    users = User.query.all()
    return render_template('index.html')
