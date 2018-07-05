from app.base_routes import RouteView


class UserNewView(RouteView):
    path = "/admin/users/create"
    name = "create_user"
    template = "admin/user_new.html"

    def get(self):
        """
        A page to create a new user
        """

        return self.render(self.template)
