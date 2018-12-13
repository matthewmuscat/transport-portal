from django.urls import path

from . import views

urlpatterns = [
    path("report/", views.Report.as_view(), name='report'),
    path("checkout/", views.Checkout.as_view(), name='checkout'),
]
