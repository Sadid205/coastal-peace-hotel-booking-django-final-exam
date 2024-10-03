from django.db import models
from hotel.models import Hotel
from guest_or_admin.models import GuestOrAdmin
from .constraints import BOOKING_STATUS
import uuid
# Create your models here.

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    guest = models.ForeignKey(GuestOrAdmin,on_delete=models.CASCADE)
    booking_status = models.CharField(max_length=20,choices=BOOKING_STATUS,default="Pending")
    booking_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    check_in_date = models.DateTimeField(null=True,blank=True)
    check_out_date = models.DateTimeField(null=True,blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_guests = models.IntegerField(default=0,null=True)
    room_type = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"Time : {self.booking_date},Hotel Name : {self.hotel.name}"





