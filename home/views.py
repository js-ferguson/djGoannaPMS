from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Users, RegUsers, Clinic

def index(request):
    users = Users.objects.all()
    clinics = Clinic.objects.all()
    reg_users = RegUsers.objects.all()

    return render(request, "index.html", {"users": users, "regusers": reg_users, "clinics": clinics})


