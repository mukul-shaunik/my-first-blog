from django import forms
from .models import RegForm

class PostForm(forms.ModelForm):
	class Meta:
		model = RegForm
		field = ('name', 'dob', 'email_id', 'father_name', 'mother_name', 'city', 'state', )
		exclude = ('p_address',)
