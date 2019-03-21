from django.conf.urls import url
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django_registration.forms import RegistrationFormUniqueEmail
from . import views

app_name = 'user_profile'

urlpatterns = [
		path('register/', views.RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    path('', include('django_registration.backends.activation.urls')),
    path('', include('django.contrib.auth.urls')),
  ]

