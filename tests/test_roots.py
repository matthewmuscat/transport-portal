from tests import SiteTest


class RootEndpoint(SiteTest):
    """
    Test cases for the root endpoint and error handling
    """

    def test_index(self):
        """
        Check the root path responds with 302 OK
        """

        response = self.client.get('/', follow_redirects=True)
        self.assert200(response)

    def test_login_redirect(self):
        """
        Check that the root path redirects to /login if TESTING is not true.
        :return:
        """

        response = self.client.get('/')
        self.assertStatus(response, 302)
        self.assertIn("/login", response.headers.get("Location"))
