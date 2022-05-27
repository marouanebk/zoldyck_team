import re
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse

from .models import deba7
from .forms import AddDeba7Form , deba7edit
from request.models import date_request
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

def list_abt(request):
    user=request.user
    list = deba7.objects.filter(org=user.id)
    return render(request, 'org/yourabatt.html',{'list':list})


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

def edit(request, abt_id):
    instance = deba7()
    if abt_id:
        instance = get_object_or_404(deba7 , pk=abt_id)
    else :
        instance = RDV()
    
    form = deba7edit(request.POST or None, instance=instance)

    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('account:home'))
    return render(request, 'deba7s/edit.html', {'form': form})

def delete(request, abt_id):
    deba7.objects.filter(pk=abt_id).delete()

    return HttpResponseRedirect(reverse('account:home'))




def association_org(request):
    list_d = deba7.objects.filter(org=request.user)
    return render(request, "deba7s/org_list.html" , {'list_d':list_d})



def association(request,d_id):
    list_d = deba7.objects.all()
    dates   = date_request.objects.filter(debah=d_id)


    return render(request, "deba7s/association.html" , {'list_d':list_d, 'dates':dates})



