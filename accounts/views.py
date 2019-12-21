from django.shortcuts import render
from .forms import PatientRegistrationForm, UserLoginForm

# Create your views here.
def register_user(request):
    form = PatientRegistrationForm
    return render(request, "register.html", {"form": form})


def login(request):
    form = UserLoginForm
    return render(request, "login.html", {"form": form})
