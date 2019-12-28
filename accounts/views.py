from django.shortcuts import render, reverse, redirect
from django.contrib import messages, auth
from .forms import PatientRegistrationForm, CustomerRegistrationForm, ClinicRegistrationForm, UserLoginForm


def register_user(request):
    """
    A view for regular users to register
    """
    if request.method == 'POST':
        user_form = PatientRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "You are not able to log in at this time")
    else:
        user_form = PatientRegistrationForm()

    context = {'user_form': user_form}
    return render(request, "register.html", context)


def register_customer(request):
    """
    A view for customers to register
    """
    if request.method == 'POST':
        customer_form = UserLoginForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()

            user = auth.authenticate(request.POST.get('email'),
                password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered a clinic")
                return redirect(reverse('index'))

            else:
                messages.error(request, "You are not able to log in at this time")
    else:
        customer_form = CustomerRegistrationForm()

    context = {'customer_form': customer_form}
    return render(request, "register_customer.html", context)


def register_clinic(request):
    """
    A view to handle registering clinics
    """
    if request.method == 'POST':
        clinic_form = ClinicRegistrationForm(request.POST)
        if clinic_form.is_valid():
            clinic_form.save()
    else:
        clinic_form = ClinicRegistrationForm()
    
    context = {'clinic_form': clinic_form}
    return render(request, "register_clinic.html", context)


def login(request):
    form = UserLoginForm
    return render(request, "login.html", {"form": form})


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
