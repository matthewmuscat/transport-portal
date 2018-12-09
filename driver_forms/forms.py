from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(label="Your name, please!", max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'checkoutform'
        self.helper.form_class = 'control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'forms_checkout'  # Should correspond with the url, ie: /forms/checkout

        self.helper.add_input(Submit('submit', 'Submit'))


class ReportForm(forms.Form):
    name = forms.CharField(label="YOUR DINGDANGLE PLEASE", max_length=100)
