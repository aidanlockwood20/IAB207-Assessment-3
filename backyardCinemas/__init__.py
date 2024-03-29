from sys import intern
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# Initialise DB Object
db = SQLAlchemy()


def create_app():

    # Initialise new Flask app object
    app = Flask(__name__)

    # Filter for date/time on comments
    @app.template_filter()
    def format_datetime(value):
        value = value.strftime
        return value("%d/%m/%Y, %H:%M")

    bootstrap = Bootstrap(app)

    # Configure app object
    app.debug = True
    app.secret_key = 'Somesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backyardCinemas.db'

    app.config['UPLOAD_EXTENSIONS'] = ['PNG', 'JPG', 'png', 'jpg']
    # Configuring the Login Manager
    login_manager = LoginManager()

    login_manager.login_view = 'auth.login_view'
    login_manager.init_app(app)

    # Adding in the user loader function
    from .auth_models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    db.init_app(app)

    # importing the main blueprint
    from .landing_page_views import main_bp
    app.register_blueprint(main_bp)

    # importing the authentication blueprint
    from .auth_views import auth_bp
    app.register_blueprint(auth_bp)

    # Importing error views
    from .error_views import page_not_found, interal_server_error, method_not_allowed
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, interal_server_error)

    # add event blueprint
    from .event_views import bp
    app.register_blueprint(bp)

    return app
