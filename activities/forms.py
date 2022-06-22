from logging import PlaceHolder
from time import time
from django import forms
from datetime import date, datetime

from activities.models import Activity

class DateInput(forms.DateInput):
    input_type = 'date'

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['type', 'duration_time','date']
        
    type = forms.ChoiceField(choices=Activity.ATypes.choices, initial=2, label="Rodzaj aktywnośći")
    duration_time = forms.FloatField(label='Długość trwania', widget=forms.NumberInput(attrs={'placeholder': 'Podaj wartość w minutach'}))
    date = forms.DateField(widget=DateInput, initial=date.today(), label="Data")