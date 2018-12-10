from crispy_forms.bootstrap import InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, HTML, Layout, Submit
from django import forms


class CheckoutForm(forms.Form):

    # General info
    name = forms.CharField(label="Driver name", max_length=100)
    license_car = forms.CharField(label="License plate, vehicle", max_length=10)
    license_hanger = forms.CharField(label="License plate, trailer", max_length=10, required=False)

    # Checks main light
    main_light_check = forms.ChoiceField(
        label="Is there visible damage on the main lights?",
        choices=[("Y", "Yes"), ("Y", "No")],
        required=True
    )
    main_light_input = forms.CharField(
        label="Describe any damage on the main lights",
        widget=forms.Textarea(attrs={"rows": "3"}),
        required=False
    )

    # Check brake lights
    brake_light_check = forms.ChoiceField(
        label="Is there visible damage on the brake lights?",
        choices=[("Y", "Yes"), ("Y", "No")],
        required=True
    )
    brake_light_input = forms.CharField(
        label="Describe any damage on the brake lights",
        widget=forms.Textarea(attrs={"rows": "3"}),
        required=False
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

            # Checks that the driver has to perform
            HTML(
                "<br></br>" + header.format(text="Checks")
            ),
            InlineRadios("main_light_check"),
            Field("main_light_input", css_class="popup"),
            InlineRadios("brake_light_check"),
            Field("brake_light_input", css_class="popup"),
        )

        self.helper.form_id = 'checkoutform'
        self.helper.form_class = 'control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'forms_checkout'  # Should correspond with the url, ie: /forms/checkout

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
