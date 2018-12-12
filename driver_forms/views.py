from django.shortcuts import render
from django.views import View
from driver_forms.forms import CheckoutForm, ReportForm


class Report(View):
    def get(self, request):
        form = ReportForm()
        return render(request, "forms/report.html", {"report_form": form})


class Checkout(View):
    def get(self, request):
        form = CheckoutForm()
        return render(request, "forms/checkout.html", {"checkout_form": form})

    def post(self, request):
        form = CheckoutForm(request.POST, request.FILES)
        if form.is_valid():
            print()
            print(request.FILES)

        else:
            print(f"is_valid() failed; The form has encountered the following errors:\n{form.errors}")

        return render(request, "forms/checkout.html", {"checkout_form": form})
