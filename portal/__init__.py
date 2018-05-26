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

    mail.init_app(app)
    moment.init_app(app)

    # TODO: Register blueprints here, instead of the route manager.

    return app

