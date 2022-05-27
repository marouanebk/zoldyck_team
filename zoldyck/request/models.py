from django.db import models
from account.models import Account
from debah.models import deba7

class request_s(models.Model):
	owner 		= models.OneToOneField(Account , on_delete=models.CASCADE)
	wilaya		= models.CharField(max_length=100)
	baladiya	= models.CharField(max_length=100)
# Create your models here.
 
class date_request(models.Model):
	organisation = models.ForeignKey(Account , on_delete=models.CASCADE , related_name="organisation",limit_choices_to={'is_org': True})
	debah		 = models.ForeignKey(deba7 , on_delete=models.CASCADE , related_name="debah")
	simple_user  = models.ForeignKey(Account , on_delete=models.CASCADE , related_name="simple_user" ,limit_choices_to={'is_org': False})
	date 		 = models.DateTimeField(blank=True , null=True)
	# deba7
	# org
		#user
		 #date
		  # 

