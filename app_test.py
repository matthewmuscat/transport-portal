from flask_testing import TestCase
from portal import app


class SiteTest(TestCase):
    """
    Extend TestCase with flask app instantiation
    """

    def create_app(self):
        """
        Add flask app configuration settings
        """

        server_name = 'portal.local'

        app.config['TESTING'] = True
        app.config['LIVESERVER_TIMEOUT'] = 10
        app.config['SERVER_NAME'] = server_name
        app.allow_subdomain_redirects = True

        return app



