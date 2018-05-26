import importlib
import inspect
import logging
import os

from flask import Blueprint
from flask_security import SQLAlchemyUserDatastore, Security

from portal import create_app, db
from portal.base_routes import BaseView, ErrorView, RedirectView, RouteView, TemplateView
from portal.config import configs
from portal.constants import PREFERRED_URL_SCHEME
from portal.models import Role, User


class RouteManager:
    def __init__(self):

        # Set up the app and the database
        self.app = create_app()

        # configure the app - We should handle this in create_app, and use the config objects like in flasky
        self.config = configs["prod"]  # Discover this based on domain name
        self.app.config['DEBUG'] = True
        self.app.config['SECRET_KEY'] = 'super-secret'
        self.app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
        self.app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT")
        self.app.config["PREFERRED_URL_SCHEME"] = PREFERRED_URL_SCHEME
        
        # Set up SQLAlchemy binds
        postgres_uri = f"postgres://{self.config.PSQL_USER}:{self.config.PSQL_PASS}@{self.config.PSQL_HOST}"
        self.app.config["SQLALCHEMY_DATABASE_URI"] = f"{postgres_uri}/portal"
        self.app.config["SQLALCHEMY_BINDS"] = {
            "kpm_transport": f"{postgres_uri}/kpm_portal",
            "mr_transport": f"{postgres_uri}/mr_portal"
        }

        # Set up the database stuff
        self.db = db
        self.db.init_app(self.app)

        # Set up Flask-Security
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        Security(self.app, user_datastore)

        # Set up the logging
        self.log = logging.getLogger(__name__)

        # Load all the views
        self.main_blueprint = Blueprint("main", __name__)
        self.log.debug(f"Loading Blueprint: {self.main_blueprint.name}")
        self.load_views(self.main_blueprint, "portal/views")
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
