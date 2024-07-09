from django.db import models
from booking.models import Booking
from guest.models import Guest
from .constraints import TRANSACTION_STATUS,TRANSACTION_TYPES
# Create your models here.
class Transaction(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE,null=True)
    transaction_id = models.CharField(max_length=30,null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=20,choices=TRANSACTION_STATUS,default="Success")
    transaction_types = models.CharField(max_length=20,choices=TRANSACTION_TYPES,default="Deposit")
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"Transaction types : {self.transaction_types},Transaction date : {self.transaction_date}"
