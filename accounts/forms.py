from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    first_name = forms.Field(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Imię'
    }), label='')
    last_name = forms.Field(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Nazwisko'
    }), label='')
    email = forms.Field(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Email'
    }), label='')
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Hasło'
    }), label='')
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user', 'placeholder': 'Potwierdź hasło'
    }), label='')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance

        