from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class CheckoutForm(forms.Form):
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
        submit.field_classes = "button is-link"
        self.helper.add_input(submit)
