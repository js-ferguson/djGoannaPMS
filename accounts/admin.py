from django.contrib import admin
from .models import Users, RegUsers, Clinic

# Register your models here.
admin.site.register(Users)
admin.site.register(RegUsers)
admin.site.register(Clinic)
