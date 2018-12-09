from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("forms/", include("driver_forms.urls")),
    path("", include("asset_manager.urls")),
]
