from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import request_s

class request_sform(forms.ModelForm):
    class Meta:
        model = request_s
        fields = ('owner','wilaya','baladiya')
