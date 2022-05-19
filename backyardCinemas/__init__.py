from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# Initialise DB Object
db = SQLAlchemy()


def create_app():

    # Initialise new Flask app object
    app = Flask(__name__)

    bootstrap = Bootstrap(app)

    # Configure app object
    app.debug = True
    app.secret_key = 'Somesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backyardCinemas.db'

    # Configuring the Login Manager
    login_manager = LoginManager()

    login_manager.login_view = 'auth_bp.login_view'
    login_manager.init_app(app)

    db.init_app(app)

    # importing the main blueprint
    from .landing_page_views import main_bp
    app.register_blueprint(main_bp)
    
    # importing the authentication blueprint
    from .auth_views import auth_bp
    app.register_blueprint(auth_bp)

    from .error_views import page_not_found
    app.register_error_handler(404, page_not_found)

    return app
