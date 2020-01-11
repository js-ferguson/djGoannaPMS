from django.contrib import admin
from .models import Clinic
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PatientRegistrationForm

class CustomUserAdmin(UserAdmin):
    add_form = PatientRegistrationForm
 #   model = CustomUser
    list_display = ['email', 'username',]
    fieldsets = ((None, {'fields': ('phone', 'personnummer',)}),)

# Register your models here.
#admin.site.register(Users)
#admin.site.register(RegUsers)
#admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Clinic)
