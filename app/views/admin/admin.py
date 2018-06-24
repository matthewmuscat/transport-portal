from app.base_routes import TemplateView


class IndexView(TemplateView):
    path = "/admin"
    name = "admin"
    template = "admin/admin.html"
