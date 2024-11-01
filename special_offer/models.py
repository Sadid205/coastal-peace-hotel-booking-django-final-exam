from django.db import models
from hotel.models import Hotel

# Create your models here.

class SpecialOffer(models.Model):
    offer_name = models.CharField(max_length=300)
    hotel = models.ManyToManyField(Hotel,related_name='offer')
    created_date = models.DateTimeField(auto_now_add=True)
    offer_duration = models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    discount = models.IntegerField(default=None)

    def __str__(self):
        return self.offer_name
    

    