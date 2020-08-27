from django import forms
from .models import *


class PostCreationForm(forms.Form):
	title = forms.CharField(max_length=236)
	content = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = post
		fields = ['title', 'content']

class ReplyForm(forms.Form):
	reply_content = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = reply
		field = ['reply_content']

	def clean(self):

		cleaned_data = super(ReplyForm, self).clean()
		reply_text = cleaned_data.get('reply_content')
		try:
			if len(reply_text) < 25:
				raise forms.ValidationError("The reply length has to be over 24 character")
		except:
			pass
