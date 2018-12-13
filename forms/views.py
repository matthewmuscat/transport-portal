from django.shortcuts import render
from django.views import View
from forms.forms import CheckoutForm, ReportForm
from utils.email import send_mail_from_template


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
            send_mail_from_template(
                send_to="leon.haland@gmail.com",
                subject="Testdongle!",
                template_path="forms/email_checkout.html",
                context={"form_data": request.POST},
                attachments=request.FILES or None
            )

        else:
            print(f"is_valid() failed; The form has encountered the following errors:\n{form.errors}")

        return render(request, "forms/checkout.html", {"checkout_form": form})
