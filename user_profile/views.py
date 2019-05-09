from django_registration.views import RegistrationView
from django_registration.forms import RegistrationFormUniqueEmail
from django_registration.forms import RegistrationFormTermsOfService

from .forms import MyCustomUserForm
# Create your views here.


class MyRegistrationView(RegistrationView):
  form_class =  MyCustomUserForm
