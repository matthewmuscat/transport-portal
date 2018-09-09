from app.base_routes import RouteView
from app.models.security import User


class UserDetailView(RouteView):
    path = "/admin/users/<int:user_id>"
    name = "user/detail"
    template = "admin/user/detail.html"

    def get(self, user_id):
        """
        A page for editing users.
        """

        user = User.query.get(user_id)

        return self.render(self.template, user=user)
