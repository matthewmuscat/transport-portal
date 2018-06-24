from app.base_routes import TemplateView


class UserAdminView(TemplateView):
    path = "/admin/users"
    name = "users"
    template = "admin/users.html"
