from app.base_routes import RouteView
from app.models.security import User


class UserAdminView(RouteView):
    path = "/admin/users"
    name = "users"
    template = "admin/users.html"

    def get(self):
        """
        A list of the user models,
        with buttons for editing,
        adding or deleting them.
        """

        users = User.query.all()

        return self.render(self.template, users=users)
