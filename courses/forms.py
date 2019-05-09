from django import forms


class HelpForm( forms.Form ):
	name = forms.CharField(max_length=120, help_text='Имя и Фамилия')
	email = forms.EmailField( max_length = 200)
	message = forms.CharField(widget = forms.Textarea)