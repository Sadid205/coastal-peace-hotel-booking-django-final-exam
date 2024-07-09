from django.db import models
# Create your models here.
from .constraints import STAR_RATING 
class Hotel(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    details = models.TextField()
    booking_price = models.IntegerField()
    facilities = models.TextField()
    rules = models.TextField()
    rating = models.CharField(max_length=10,choices=STAR_RATING)
    location = models.CharField(max_length=500)
    number_of_rooms = models.IntegerField()
    room_types = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to="hotel/images/")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel.name