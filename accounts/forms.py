from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth import get_user_model
from goannaPMS import settings

class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PatientRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    phone = PhoneNumberField(label = "Phone Number")
    personnummer = forms.CharField(label='Personnummer')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'personnummer', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError(u'Email address must be unique')
        return email


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your parrword")
        if password1 != password2:
            raise ValidationError("Passwords must match")
        return password2


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    fname = forms.CharField(label="First Name")
    lname = forms.CharField(label="Last Name")

    email = forms.EmailField(required=True)
    phone = PhoneNumberField(label = "Phone Number")
    personnummer = forms.CharField(label = "Personnummer")


class ClinicRegistrationForm(forms.Form):
    clinic_name = forms.CharField(label='Clinic Name')
    street_address1 = forms.CharField(label='Street address 1')
    street_address2 = forms.CharField(label='Street address 2')
    county = forms.CharField(label='County')
    city = forms.CharField(label='City')
    phone = PhoneNumberField(label='Phone')

