from app.base_routes import TemplateView


class IndexView(TemplateView):
    path = "/"
    name = "index"
    template = "main/index.html"
