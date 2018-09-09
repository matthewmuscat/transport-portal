from flask_testing import TestCase

from app import RouteManager


class SiteTest(TestCase):
    """
    Extend TestCase with flask app instantiation
    """

    def create_app(self):
        """
        Add flask app configuration settings
        """

        manager = RouteManager("testing")

        return manager.app
