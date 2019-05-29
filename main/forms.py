# from datetime import timedelta

from django import forms
from .models import *
# from django.forms import ValidationError
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.utils import timezone
# from django.db.models import Q
# from django.utils.translation import gettext_lazy as _


# 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar','job','company']

    def __init__(self, *args, **kwargs):
    	self.request = kwargs.pop('request')
    	super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.request.user
        return super().save(commit=commit)
        
