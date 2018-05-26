from app.base_routes import TemplateView


class IndexView(TemplateView):
    path = "/"
    name = "index"
    template = "under_construction.html"
