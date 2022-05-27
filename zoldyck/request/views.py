from django.shortcuts import render
from django.shortcuts import redirect
from .models import request_s

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
	return render (request, 'request/confirm_request.html')