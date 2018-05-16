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


class RootEndpoint(SiteTest):
    """
    Test cases for the root endpoint and error handling
    """

    def test_index(self):
        """
        Check the root path responds with 200 OK
        """

        response = self.client.get('/', "http://"+app.config['SERVER_NAME'])
        self.assertEqual(response.status_code, 200)
