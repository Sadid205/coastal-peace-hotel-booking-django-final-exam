from django.db import models
from django.contrib.auth.models import User
from account.models import Account
# Create your models here.
class Guest(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="guest")
    account = models.OneToOneField(Account,on_delete=models.CASCADE,null=True,related_name='account')
    image = models.ImageField(upload_to="guest/images/")
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username}"
