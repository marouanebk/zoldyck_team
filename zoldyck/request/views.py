from calendar import c
from sys import orig_argv
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from debah.models import deba7
from .models import request_s

from .forms import request_sform,request_date
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

def confirm_request(request,o):
	ins = get_object_or_404(request_s,pk=o)
	deba7s = deba7.objects.filter(org=o)
	form = request_date()
	if request.method == 'POST':
		ins.id = form['organisation']
		deba7s = form['debah']
		form.save()
	return render (request, 'request/confirm_request.html',{'form':form})