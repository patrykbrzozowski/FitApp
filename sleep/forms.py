from time import time
from django import forms
from datetime import date, datetime

from sleep.models import Sleep

class DateInput(forms.DateInput):
    input_type = 'date'

class SleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = ['duration_time', 'date']
        
    date = forms.DateField(widget=DateInput, initial=date.today(), label="Data")
    duration_time = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Podaj wartość w godzinach'}), label='Czas trwania')


    def is_valid(self):
        is_valid = super().is_valid()
        date_list = [sleep_date['date'] for sleep_date in Sleep.objects.values('date')]
        print(date_list)
        
        date = self.cleaned_data.get('data')
        if date in date_list:
            self.add_error('date', 'Juz jest podana ta data')
            is_valid = False
        return is_valid