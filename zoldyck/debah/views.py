import re
from django.shortcuts import render
from .models import deba7
from .forms import AddDeba7Form
from request.models import date_request
# Create your views here.
def deba7_list(request):
    list = deba7.objects.all()
    return render(request, 'deba7s/deba7_list.html',{'list':list})
def add_deba7(request):
    print('ok')
    if request.method == 'POST':
        form = AddDeba7Form(request.POST)
        print('ok1')
        if form.is_valid():
            print('ok2')
            form.save()
    form = AddDeba7Form()
    return render(request, 'deba7s/add_deba7.html', {'form': form})



def association_org(request):
    list_d = deba7.objects.filter(org=request.user)
    return render(request, "deba7s/org_list.html" , {'list_d':list_d})



def association(request,d_id):
    list_d = deba7.objects.all()
    dates   = date_request.objects.filter(debah=d_id)


    return render(request, "deba7s/association.html" , {'list_d':list_d, 'dates':dates})



