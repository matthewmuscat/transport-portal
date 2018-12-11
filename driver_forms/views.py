from django.shortcuts import redirect, render
from django.views import View
from driver_forms.forms import CheckoutForm, ReportForm


class Report(View):
    def get(self, request):
        report_form = ReportForm()
        return render(request, "forms/report.html", {"report_form": report_form})


class Checkout(View):
    def get(self, request):
        checkout_form = CheckoutForm()
        return render(request, "forms/checkout.html", {"checkout_form": checkout_form})

    def post(self, request):
        return redirect("http://beardfist.com")
