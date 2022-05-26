from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    return HttpResponse("heello world")
    # Create your views here.
