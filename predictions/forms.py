from django import forms
from predictions.choices import *

class FeaturesForm(forms.Form):
    amount_of_given_credit = forms.IntegerField()
    gender = forms.ChoiceField(choices=gender_choices)
    education = forms.ChoiceField(choices=education_choices)
    marital_status = forms.ChoiceField(choices=marital_choices)
    age = forms.IntegerField()
    payment_status_6_months_ago = forms.ChoiceField(choices=payment_choices)
    payment_status_5_months_ago = forms.ChoiceField(choices=payment_choices)
    payment_status_4_months_ago = forms.ChoiceField(choices=payment_choices)
    payment_status_3_months_ago = forms.ChoiceField(choices=payment_choices)
    payment_status_2_months_ago = forms.ChoiceField(choices=payment_choices)
    payment_status_1_month_ago = forms.ChoiceField(choices=payment_choices)
    amount_on_bill_statement_6_months_ago = forms.IntegerField()
    amount_on_bill_statement_5_months_ago = forms.IntegerField()
    amount_on_bill_statement_4_months_ago = forms.IntegerField()
    amount_on_bill_statement_3_months_ago = forms.IntegerField()
    amount_on_bill_statement_2_months_ago = forms.IntegerField()
    amount_on_bill_statement_1_month_ago = forms.IntegerField()
    previous_payment_6_months_ago = forms.IntegerField()
    previous_payment_5_months_ago = forms.IntegerField()
    previous_payment_4_months_ago = forms.IntegerField()
    previous_payment_3_months_ago = forms.IntegerField()
    previous_payment_2_months_ago = forms.IntegerField()
    previous_payment_1_month_ago = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(FeaturesForm, self).__init__(*args, **kwargs)
        self.fields['amount_of_given_credit'].widget.attrs.update({'class': 'amount'})
