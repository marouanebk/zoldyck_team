from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import request_s,date_request

class request_sform(forms.ModelForm):
    class Meta:
        model = request_s
        fields = ('owner','wilaya','baladiya')
class request_date(forms.ModelForm):
    class Meta:
        model = date_request
        fields = ('organisation','debah','simple_user','date')
