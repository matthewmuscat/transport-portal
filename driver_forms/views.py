from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
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

            # Build an email
            html_template = get_template("forms/email.html")
            context = Context({"balls": "node", "fire": "proof"})
            html_email = html_template.render(context)  # noqa

        else:
            print(f"is_valid() failed; The form has encountered the following errors:\n{form.errors}")

        return render(request, "forms/checkout.html", {"checkout_form": form})
