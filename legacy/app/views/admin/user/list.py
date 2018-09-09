from app.base_routes import RouteView
from app.models.security import User


class UserListView(RouteView):
    path = "/admin/users"
    name = "user/list"
    template = "admin/user/list.html"

    def get(self):
        """
        A list of the user models,
        with buttons for editing,
        adding or deleting them.
        """

        users = User.query.all()

        return self.render(self.template, users=users)
