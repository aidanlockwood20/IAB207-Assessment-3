from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialising the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # App Configurations
    app.debug = True
    app.secret_key = 'Somesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backyardCinemas.db'

    # Initialising the database
    db.init_app(app)

    return app