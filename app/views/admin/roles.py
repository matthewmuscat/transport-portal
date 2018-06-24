from app.base_routes import TemplateView


class RoleAdminView(TemplateView):
    path = "/admin/roles"
    name = "roles"
    template = "admin/roles.html"
