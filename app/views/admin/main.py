from app.base_routes import TemplateView


class MainAdminView(TemplateView):
    path = "/admin"
    name = "main"
    template = "admin/main.html"
