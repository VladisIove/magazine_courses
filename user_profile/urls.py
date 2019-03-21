from django.conf.urls import url
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views

from django_registration.forms import RegistrationFormUniqueEmail
from . import views

app_name = 'user_profile'

urlpatterns = [
	path('register','django_registration.views.register', {'form': RegistrationFormUniqueEmail,}, name='registration_register' ),
	path('', include('registration.urls')),
	# path('signup/', views.signup, name = 'signup'),
	# path('login/', auth_views.LoginView.as_view( template_name = 'login.html'), name = 'login'),
	# path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
	# url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]

