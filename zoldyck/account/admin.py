from django.contrib import admin

from .models import Account
from request.models import request_s

# Register your models here.
admin.site.register(Account)
admin.site.register(request_s)