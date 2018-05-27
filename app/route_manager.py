import importlib
import inspect
import logging
import os

from flask import Blueprint

from app.base_routes import BaseView, ErrorView, RedirectView, RouteView, TemplateView


class RouteManager:
    def __init__(self, app, db):

        # Set up app and db
        self.app = app
        self.db = db

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
