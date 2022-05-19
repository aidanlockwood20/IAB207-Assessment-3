from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialise DB Object
db = SQLAlchemy()


def create_app():

    # Initialise new Flask app object
    app = Flask(__name__)

    # Configure app object
    app.debug = True
    app.secret_key = 'Somesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backyardCinemas.db'

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
