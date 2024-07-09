from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.account_number


