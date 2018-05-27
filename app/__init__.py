from flask import Flask
from flask_mail import Mail
from flask_moment import Moment
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
moment = Moment()
db = SQLAlchemy()
security = Security()


def create_app(config_name):
    from app.models.security import Role, User
    from config import config

    # Build the actual app
    app = Flask(
        __name__,
        static_url_path="/static",
    )
    app.config.from_object(config[config_name])

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    Security(app, user_datastore)

    return app
