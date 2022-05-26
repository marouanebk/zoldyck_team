from django.db import models
from account.models import Account
# Create your models here.
class deba7(models.Model):
    org = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='org',limit_choices_to={'is_org':True})
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    limit = models.IntegerField()
    taken = models.IntegerField(default=0)
    limit_reacher = models.BooleanField(default=False)