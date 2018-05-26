from tests import SiteTest


class RootEndpoint(SiteTest):
    """
    Test cases for the root endpoint and error handling
    """

    def test_index(self):
        """
        Check the root path responds with 200 OK
        """

        response = self.client.get('/', "http://" + self.app.config['SERVER_NAME'])
        self.assertEqual(response.status_code, 200)
