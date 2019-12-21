from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField

class PatientRegistrationForm(UserCreationForm):

    fname = forms.CharField(label="First Name")
    lname = forms.CharField(label="Last Name")

    email = forms.EmailField(required=True)
    phone = PhoneNumberField(label = "Phone Number")
    personnummer = CharField(label = "Personnummer")

    password1 = forms.CharField(label = "Password")
    password2 = forms.CharField(label = "Repeat Password")
