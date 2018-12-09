from django.urls import path

from . import views

urlpatterns = [
    path("report/", views.report, name='report'),
    path("checkout/", views.checkout, name='checkout'),
]
