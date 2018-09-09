from app.base_routes import TemplateView


class RoleListView(TemplateView):
    path = "/admin/roles"
    name = "role/list"
    template = "admin/role_list.html"
