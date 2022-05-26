from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm




def home(request):
    return HttpResponse("heello world")
    # Create your views here.


def singup(request):
    context = {'form':RegistrationForm}
    return render(request, 'account/signup.html', context)
