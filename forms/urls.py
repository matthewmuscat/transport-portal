from django.urls import path

from . import views

urlpatterns = [
    path("discrepancies/", views.discrepancies, name='discrepancies'),
    path("checkout/", views.checkout, name='checkout'),
]
