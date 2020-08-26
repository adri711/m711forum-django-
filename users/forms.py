from django import forms
#from .models import member
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
	
	username = forms.CharField()
	email = forms.EmailField()
	
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	password_validation = forms.CharField(max_length=32, widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email','password', 'password_validation']

	def clean(self):

		cleaned_data = super(UserRegistrationForm, self).clean()
		password_input = cleaned_data.get('password')
		password_valid = cleaned_data.get('password_validation')

		if password_input != password_valid:
			raise forms.ValidationError("Passwords don't match.")