from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from portal import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("forms/", include("driver_forms.urls")),
    path("", include("asset_manager.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
