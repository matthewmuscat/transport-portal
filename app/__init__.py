import importlib
import inspect
import logging
import os

from flask import Blueprint, Flask, request
from flask_mail import Mail
from flask_moment import Moment
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

from app.base_routes import BaseView, ErrorView, RedirectView, RouteView, TemplateView

mail = Mail()
moment = Moment()
db = SQLAlchemy()


class RouteManager:
    def __init__(self, config_name):
        from app.models.security import Role, User
        from config import config

        # Build the actual app
        app = Flask(
            __name__,
            static_url_path="/static",
        )
        app.config.from_object(config[config_name])

        # Configure extensions
        mail.init_app(app)
        moment.init_app(app)
        db.init_app(app)

        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        Security(app, user_datastore)

        # Set up the app and the db
        self.app = app
        self.db = db

        # Dynamically load the correct stylesheet based on domain name
        @self.app.context_processor
        def set_domain_name():

            if "domain_name" not in request.args:
                # Parse e.g. `kpmtransport` out of `portal.kpmtransport.no`
                domain_name = request.headers['Host'].split(".")[1]
            else:
                # In debug mode, allow user to specify which style to load via a `domain_name` URL param.
                if self.app.config["DEBUG"]:
                    domain_name = request.args.get("domain_name")
                else:
                    domain_name = "default"

            # Set the default if the selected one has no accompanying scss file.
            if f"{domain_name}.scss" not in os.listdir("app/static/scss/brandings"):
                domain_name = "default"

            return dict(domain_name=domain_name)

        # Set up the logging
        self.log = logging.getLogger(__name__)

        # Load all the views
        self.main_blueprint = Blueprint("main", __name__)
        self.log.debug(f"Loading Blueprint: {self.main_blueprint.name}")
        self.load_views(self.main_blueprint, "app/views")
        self.app.register_blueprint(self.main_blueprint)
        self.log.debug("")

    def run(self):
        self.app.run(port=8080)

    def load_views(self, blueprint, location="views"):
        for filename in os.listdir(location):
            if os.path.isdir(f"{location}/{filename}"):

                # Recurse if it's a directory; load ALL the views!
                self.load_views(blueprint, location=f"{location}/{filename}")
                continue

            if filename.endswith(".py") and not filename.startswith("__init__"):
                module = importlib.import_module(f"{location}/{filename}".replace("/", ".")[:-3])

                for cls_name, cls in inspect.getmembers(module):
                    load_as_blueprint = (
                        inspect.isclass(cls) and
                        cls is not BaseView and
                        cls is not ErrorView and
                        cls is not RouteView and
                        cls is not TemplateView and
                        cls is not RedirectView and
                        BaseView in cls.__mro__
                    )

                    if load_as_blueprint:
                        cls.setup(self, blueprint)
                        self.log.debug(f">> View loaded: {cls.name: <15} ({module.__name__}.{cls_name})")
