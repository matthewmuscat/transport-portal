from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, HTML, Layout, Submit
from django import forms
from django.urls import reverse


class CheckoutForm(forms.Form):

    # GENERAL INFO #
    name = forms.CharField(label="Driver name", max_length=100)
    license_car = forms.CharField(label="License plate, vehicle", max_length=10)
    license_hanger = forms.CharField(label="License plate, trailer", max_length=10, required=False)

    # VEHICLE CHECK #
    # Checks main light
    main_light_check = forms.ChoiceField(
        label="Is there visible damage on the main lights?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    main_light_input = forms.CharField(
        label="Describe any damage on the main lights",
        widget=forms.Textarea(attrs={"rows": "3"}),
    )
    main_light_upload = forms.ImageField(
        label="Upload an image which shows the damage"
    )

    # Check brake lights
    brake_light_check = forms.ChoiceField(
        label="Is there visible damage on the brake lights?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    brake_light_input = forms.CharField(
        label="Describe any damage on the brake lights",
        widget=forms.Textarea(attrs={"rows": "3"}),
    )
    brake_light_upload = forms.ImageField(
        label="Upload an image which shows the damage"
    )

    # Check indicator lights
    indicator_light_check = forms.ChoiceField(
        label="Is there visible damage on the indicator lights?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    indicator_light_input = forms.CharField(
        label="Describe any damage on the indicator lights",
        widget=forms.Textarea(attrs={"rows": "3"}),
    )
    indicator_light_upload = forms.ImageField(
        label="Upload an image which shows the damage"
    )

    # Check if there are any warning lights in the display
    warning_light_check = forms.ChoiceField(
        label="Are there any warning showing in the display?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    warning_light_input = forms.CharField(
        label="Describe the warnings that are shown in the display",
        widget=forms.Textarea(attrs={"rows": "3"}),
    )
    warning_light_upload = forms.ImageField(
        label="Upload an image of the display which shows the warnings"
    )

    # Check tires
    tire_check = forms.ChoiceField(
        label="Is there visible damage on the tires?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    tire_input = forms.CharField(
        label="Describe any damage on the tires",
        widget=forms.Textarea(attrs={"rows": "3"}),
    )
    tire_upload = forms.ImageField(
        label="Upload an image of the damage"
    )

    # Check for other visible damage
    visible_damage_check = forms.ChoiceField(
        label="Is there any other visible damage on the vehicle or the trailer?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    visible_damage_input = forms.CharField(
        label="Describe the damage",
        widget=forms.Textarea(attrs={"rows": "3"})
    )
    visible_damage_upload = forms.ImageField(
        label="Upload an image which shows the damage"
    )

    # EQUIPMENT CHECKS #
    # Number of tire chains
    chains_input = forms.CharField(
        label="How many tire chains are in the vehicle?",
        widget=forms.Textarea(attrs={"rows": "3"}),
        required=False
    )

    # Ferry card
    ferry_card_check = forms.ChoiceField(
        label="Is there a ferry card in the vehicle?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )
    ferry_card_input = forms.CharField(
        label="How much credit is left on the ferry card?",
        required=True
    )

    # Diesel card present
    diesel_card_check = forms.ChoiceField(
        label="Is the correct diesel card in the vehicle?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )

    # Vehicle registration
    vehicle_registration_check = forms.ChoiceField(
        label="Is the vehicle registration in the vehicle?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )

    # Transportation permit
    transport_permit_check = forms.ChoiceField(
        label="Is the transport permit (ECMT) in the vehicle?",
        choices=[("Y", "Yes"), ("N", "No")],
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        # The layout of the page
        header = "<h4 class=is-size-4><strong>{text}</strong></h4><br>"
        self.helper.layout = Layout(

            # Information about the vehicle and driver
            HTML(
                header.format(text="General Information")
            ),
            Field("name"),
            Field("license_car"),
            Field("license_hanger"),

            # VEHICLE CHECKS #
            Div(
                HTML(
                    "<br></br>" + header.format(text="Vehicle Checks")
                ),

                # Light checks
                InlineRadios("main_light_check"),
                Field("main_light_input", css_class="popup"),
                Field("main_light_upload", css_class="popup"),

                InlineRadios("brake_light_check"),
                Field("brake_light_input", css_class="popup"),
                Field("brake_light_upload", css_class="popup"),

                InlineRadios("indicator_light_check"),
                Field("indicator_light_input", css_class="popup"),
                Field("indicator_light_upload", css_class="popup"),

                InlineRadios("warning_light_check"),
                Field("warning_light_input", css_class="popup"),
                Field("warning_light_upload", css_class="popup"),

                # Damage checks
                InlineRadios("tire_check"),
                Field("tire_input", css_class="popup"),
                Field("tire_upload", css_class="popup"),

                InlineRadios("visible_damage_check"),
                Field("visible_damage_input", css_class="popup"),
                Field("visible_damage_upload", css_class="popup"),

                css_id="vehicle-checks"
            ),

            # EQUIPMENT CHECKS #
            Div(
                HTML(
                    "<br></br>" + header.format(text="Equipment Checks")
                ),
                InlineRadios("diesel_card_check"),
                InlineRadios("ferry_card_check"),
                Field("ferry_card_input", css_class="popup"),
                InlineRadios("vehicle_registration_check"),
                InlineRadios("transport_permit_check"),
                css_id="equipment-checks"
            )
        )

        self.helper.form_id = 'checkoutform'
        self.helper.form_class = 'control'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('checkout')

        submit = Submit('submit', 'Submit')
        submit.field_classes = "button is-link"
        self.helper.add_input(submit)


class ReportForm(forms.Form):
    name = forms.CharField(label="Driver", max_length=100)
    license_car = forms.CharField(label="License plate, vehicle", max_length=10)
    license_hanger = forms.CharField(label="License plate, trailer", max_length=10, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'checkoutform'
        self.helper.form_class = 'control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'forms_checkout'  # Should correspond with the url, ie: /forms/checkout

        submit = Submit('submit', 'Submit')
        submit.field_classes = "btn btn-info"
        self.helper.add_input(submit)
