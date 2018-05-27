from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app():

    # Build the actual app
    app = Flask(
        __name__,
        static_url_path="/static",
    )

    # TODO: Configure the app with a configuration object here

    mail.init_app(app)
    moment.init_app(app)
    # TODO: init_app the db in this file.

    # TODO: Register blueprints here, instead of the route manager.

    return app
