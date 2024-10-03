from django.db import models
from django.contrib.auth.models import User
from account.models import Account
# Create your models here.
class GuestOrAdmin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="guest")
    account = models.OneToOneField(Account,on_delete=models.CASCADE,null=True,related_name='account')
    image = models.URLField(max_length=500)
    mobile_number = models.CharField(max_length=15)
    admin_request = models.BooleanField(default=False,null=True,blank=True)
    is_admin = models.BooleanField(default=False,null=True,blank=True)
    is_master_admin = models.BooleanField(default=False,null=True,blank=True)
    
    

    def __str__(self):
        return f"{self.user.username}"
