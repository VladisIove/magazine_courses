from django.conf.urls import url
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django_registration.backends.activation.views import RegistrationView
from . import views
from . import forms 

app_name = 'user_profile'

urlpatterns = [
	path('register/', RegistrationView.as_view(form_class=forms.MyCustomUserForm), name='registration_register'),
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
  ]

