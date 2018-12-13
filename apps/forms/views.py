import datetime

from apps.forms.forms import CheckoutForm, ReportForm
from django.shortcuts import render
from django.views import View
from utils.email import send_mail_from_template


class Report(View):
    def get(self, request):
        form = ReportForm()
        return render(request, "forms/report.html", {"report_form": form})


class Checkout(View):
    def _process(self, data, form):
        """
        Takes the form data from a POST request,
        and formats it into something that's easy to read.
        """

        general_info_fields = [
            "name",
            "license_car",
            "license_hanger"
        ]
        vehicle_check_fields = [
            "main_light_check",
            "main_light_input",
            "brake_light_check",
            "brake_light_input",
            "indicator_light_check",
            "indicator_light_input",
            "warning_light_check",
            "warning_light_input",
            "tire_check",
            "tire_input",
            "visible_damage_check",
            "visible_damage_input"
        ]
        equipment_check_fields = [
            "chains_input",
            "ferry_card_check",
            "ferry_card_input",
            "diesel_card_check",
            "vehicle_registration_check",
            "transport_permit_check"
        ]

        general_info = {}
        vehicle_check = {}
        equipment_check = {}

        for field_name, response in data.items():

            print(f"processing {field_name}")

            # Get rid of empty fields
            all_fields = equipment_check_fields + vehicle_check_fields + general_info_fields
            if not response or field_name not in all_fields:
                continue

            # Get the label
            label = form[field_name].label

            # Replace radio responses with symbols
            if response == "Y":
                response = "✔"
            elif response == "N":
                response = "✖"

            if field_name in general_info_fields:
                print("Adding to general info!")
                general_info[label] = response
            elif field_name in vehicle_check_fields:
                vehicle_check[label] = response
            elif field_name in equipment_check_fields:
                equipment_check[label] = response

        response_groups = {
            "general_info": general_info,
            "vehicle_check": vehicle_check,
            "equipment_check": equipment_check
        }
        print(response_groups['general_info'])
        return response_groups

    def get(self, request):
        form = CheckoutForm()
        return render(request, "forms/checkout.html", {"checkout_form": form})

    def post(self, request):
        form = CheckoutForm(request.POST, request.FILES)
        if form.is_valid():
            today = datetime.date.today().strftime("%d. %B %Y")
            subject = f"Checkout report, {today}: {request.POST['name']} - {request.POST['license_car']}"
            send_mail_from_template(
                send_to="leon.haland@gmail.com",
                subject=subject,
                template_path="forms/email_checkout.html",
                context=self._process(request.POST, form),
                attachments=request.FILES or None
            )

        else:
            print(f"is_valid() failed; The form has encountered the following errors:\n{form.errors}")

        return render(request, "forms/checkout.html", {"checkout_form": form})
