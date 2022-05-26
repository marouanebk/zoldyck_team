from django.db import models
from account.models import Account

class request_s(models.Model):
	owner 		= models.OneToOneField(Account , on_delete=models.CASCADE)
	wilaya		= models.CharField(max_length=100)
	baladiya	= models.CharField(max_length=100)
# Create your models here.
