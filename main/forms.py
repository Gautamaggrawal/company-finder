from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['job','company']

    def __init__(self, *args, **kwargs):
    	self.request = kwargs.pop('request')
    	super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.request.user
        return super().save(commit=commit)
        
class Companyform(forms.ModelForm):
	class Meta:
		model=Company
		exclude=('logo',)
