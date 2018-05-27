from flask_testing import TestCase

from app import create_app


class SiteTest(TestCase):
    """
    Extend TestCase with flask app instantiation
    """

    def create_app(self):
        """
        Add flask app configuration settings
        """

        return create_app("testing")
