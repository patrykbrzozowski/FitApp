from time import time
from django import forms
from datetime import date, datetime

from hydration.models import Water

class DateInput(forms.DateInput):
    input_type = 'date'

class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ['value', 'date']
        
    value = forms.ChoiceField(choices=Water.WTypes.choices, initial=2, label="Wartość")
    date = forms.DateField(widget=DateInput(attrs={'readonly': 'readonly'}), initial=date.today(), label="Data")