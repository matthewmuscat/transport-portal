import importlib
import inspect
import logging
import os

from flask import Blueprint, Flask, _request_ctx_stack
from flask_security import PonyUserDatastore, Security

from portal.base_routes import BaseView, ErrorView, RedirectView, RouteView, TemplateView
from portal.config import configs
from portal.constants import PREFERRED_URL_SCHEME
from portal.models import Role, User, security_db, get_database

TEMPLATES_PATH = "templates"
STATIC_PATH = "static"


class RouteManager:
    def __init__(self):

        # Set up the app and the database
        self.app = Flask(
            __name__,
            static_folder=STATIC_PATH,
            template_folder=TEMPLATES_PATH,
            static_url_path="/static",
        )

        # configure the app
        self.app.config['DEBUG'] = True
        self.app.config['SECRET_KEY'] = 'super-secret'
        self.app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
        self.app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT")
        self.app.config["PREFERRED_URL_SCHEME"] = PREFERRED_URL_SCHEME

        # Set up the database stuff
        self.db = db
        self.config = configs["prod"]  # Discover this based on domain name
        provider = "postgres"
        user = os.environ.get("PSQL_USER")
        host = os.environ.get("PSQL_HOST")
        password = os.environ.get("PSQL_PASS")
        database = os.environ.get("PSQL_DB")
        self.db.bind(
            provider='postgres',
            user=self.config.PSQL_USER,
            password=self.config.PSQL_PASS,
            host=self.config.PSQL_HOST,
            database=self.config.PSQL_DB,
        )
        self.db.generate_mapping()

        # Set up Flask-Security
        self.user_datastore = PonyUserDatastore(db, User, Role)
        self.security = Security(self.app, self.user_datastore)

        # Set up the logging
        self.log = logging.getLogger(__name__)

        # Load all the views
        self.main_blueprint = Blueprint("main", __name__)
        self.log.debug(f"Loading Blueprint: {self.main_blueprint.name}")
        self.load_views(self.main_blueprint, "portal/views")
        self.app.register_blueprint(self.main_blueprint)
        self.log.debug("")

        self.app.before_request(self.https_fixing_hook)  # Try to fix HTTPS issues

    def https_fixing_hook(self):
        """
        Attempt to fix HTTPS issues by modifying the request context stack
        """

        if _request_ctx_stack is not None:
            req_ctx = _request_ctx_stack.top
            req_ctx.url_adapter.url_scheme = PREFERRED_URL_SCHEME

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
