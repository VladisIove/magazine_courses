"""from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class SignupForm( UserCreationForm ):
	email = forms.EmailField( max_length = 200, help_text = 'Обязательно')

	def clean_email(self):

		email = self.cleaned_data.get('email')

		try:
			match = User.objects.get(email = email)
		except User.DoesNotExist:
			return email

		raise forms.ValidationError('Эта почта уже используется')
		
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
"""

from django_registration.forms import RegistrationForm

from .models import User

class MyCustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
