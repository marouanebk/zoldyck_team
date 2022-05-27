from calendar import c
import re
from sys import orig_argv
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.utils import timezone

from debah.models import deba7
from .models import date_request, request_s

from .forms import request_sform
# Create your views here.
def request_v(request):
	form = request_sform
	if request.POST:
		form = request_sform(request.POST)
		if form.is_valid():
			form.save()
			return redirect("account:home")
	context = {'form':form}
	return render (request, 'request/request_s.html' , context)


def all_request(request):
	obj = request_s.objects.all()
	context = {'obj':obj}
	return render (request, "request/all_request.html" , context)

def confirm_request(request):	
	list = deba7.objects.filter(org=request.user)
	if request.method == 'POST':
		list = deba7.objects.filter(org=request.user)
		s = request.POST.get('d')
		s1 = request.POST.get('e')
		s2 = request.POST.get('f')
		s3 = request.POST.get('g')
		if s3 is not None:
			d = date_request.objects.create(organisation=request.user,debah=get_object_or_404(deba7,pk=int(s3)),simple_user=request.user,date=timezone.now())
			print(s3)
	return render (request, 'request/confirm_request.html',{'list':list})