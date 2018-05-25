import os

from flask_testing import TestCase

from app import manager
from gunicorn_config import _when_ready as when_ready

# Some unit tests fail if this is set
if "FLASK_DEBUG" in os.environ:
    del os.environ["FLASK_DEBUG"]


class SiteTest(TestCase):
    """
    Extend TestCase with flask app instantiation
    """

    app = manager.app

    def create_app(self):
        """
        Add flask app configuration settings
        """

        self.app.config["WTF_CSRF_CHECK_DEFAULT"] = False
        server_name = 'pytest.local'

        self.app.config['TESTING'] = True
        self.app.config['LIVESERVER_TIMEOUT'] = 10
        self.app.config['SERVER_NAME'] = server_name

        return self.app
