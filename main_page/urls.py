from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *
from accounts import forms

urlpatterns = [
    path('', display, name='main'),
]
