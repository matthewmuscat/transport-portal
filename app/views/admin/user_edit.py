from app.base_routes import RouteView
from app.models.security import User


class UserEditView(RouteView):
    path = "/admin/users/edit/<int:user_id>"
    name = "user_edit"
    template = "admin/user_edit.html"

    def get(self, user_id):
        """
        A page for editing users.
        """

        user = User.query.get(user_id)

        return self.render(self.template, user=user)
