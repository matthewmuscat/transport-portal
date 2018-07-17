import importlib
import inspect
import logging
import os

from flask import Blueprint, Flask, request
from flask_mail import Mail
from flask_moment import Moment
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
moment = Moment()
db = SQLAlchemy()


class RouteManager:
    def __init__(self, config_name):
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

        # Set up the app and the db
        self.app = app
        self.app.db = db

        # Security init (this depends on a working database)
        from app.models.security import Role, User
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        self.app.security = Security(app, user_datastore)

        # Dynamically load the correct stylesheet based on domain name
        @self.app.context_processor
        def set_domain_name():

            if self.app.config["DEBUG"] and "domain_name" in request.args:
                domain_name = request.args.get("domain_name")

            else:
                # Parse e.g. `kpmtransport` out of `portal.kpmtransport.no`
                domain_name = request.headers['Host'].split(".")[1]

            # Set the default if the selected one has no accompanying scss file.
            if domain_name not in os.listdir("app/static/scss/brandings"):
                domain_name = "default"

            return dict(domain_name=domain_name)

        # Set up the logging
        self.log = logging.getLogger(__name__)

        # Load the main blueprint
        self.main_blueprint = Blueprint("main", __name__)
        self.log.debug(f"Loading Blueprint: {self.main_blueprint.name}")
        self.load_views(self.main_blueprint, "app/views/main")

        # Load the admin blueprint
        self.admin_blueprint = Blueprint("admin", __name__)
        self.log.debug(f"Loading Blueprint: {self.main_blueprint.name}")
        self.load_views(self.admin_blueprint, "app/views/admin")

        # Load the error handling blueprint
        # self.error_blueprint = Blueprint("error", __name__)
        # self.log.debug(f"Loading Blueprint: {self.main_blueprint.name}")
        # self.load_views(self.error_blueprint, "app/views/error_handlers")

        # Register all the blueprints
        self.app.register_blueprint(self.main_blueprint)
        self.app.register_blueprint(self.admin_blueprint)
        # self.app.register_blueprint(self.error_blueprint)
        self.log.debug("")

    def run(self):
        self.app.run(port=8080)

    def load_views(self, blueprint, location="views"):
        from app.base_routes import BaseView, ErrorView, RedirectView, RouteView, TemplateView

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
