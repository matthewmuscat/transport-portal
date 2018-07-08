from app.base_routes import RouteView


class UserNewView(RouteView):
    path = "/admin/users/new"
    name = "user/new"
    template = "admin/user_new.html"

    def get(self):
        """
        A page to create a new user
        """

        return self.render(self.template)
