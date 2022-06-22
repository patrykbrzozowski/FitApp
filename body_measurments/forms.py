from logging import PlaceHolder
from time import time
from django import forms
from datetime import date, datetime

from body_measurments.models import BodyCircuits, BodyMeasurements, Goals

class DateInput(forms.DateInput):
    input_type = 'date'

class BodyMeasurementsForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurements
        fields = ['weight', 'height','date']
        
    date = forms.DateField(widget=DateInput, initial=date.today(), label="Data")
    weight = forms.FloatField(label='Waga')
    height = forms.FloatField(label='Wzrost')

class BodyCircuitsForm(forms.ModelForm):
    class Meta:
        model = BodyCircuits
        fields = ['neck', 'hips', 'chest', 'biceps', 'thigh', 'waist', 'calf', 'belly', 'date']
        
    date = forms.DateField(widget=DateInput, initial=date.today(), label="Data")
    neck = forms.FloatField(label='Szyja')
    hips = forms.FloatField(label='Biodra')
    chest = forms.FloatField(label='Klatka piersiowa')
    biceps = forms.FloatField(label='Biceps')
    thigh = forms.FloatField(label='Udo')
    waist = forms.FloatField(label='Talia')
    calf = forms.FloatField(label='Łydka')
    belly = forms.FloatField(label='Brzuch')

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['weight_goal', 'week_rate']
    
    weight_goal = forms.FloatField(label='Masa ciała')
    week_rate = forms.FloatField(label='Tempo zminay masy ciała tygodniowo')