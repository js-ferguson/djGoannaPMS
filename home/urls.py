from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('register', views.register, name='register-user')
]