from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField

class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PatientRegistrationForm(UserCreationForm):
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

