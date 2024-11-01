from django.db import models
# from hotel.models import Hotel
from django.apps import apps
from guest_or_admin.models import GuestOrAdmin
from .constraints import USER_RATING
# Create your models here.
class Review(models.Model):
    reviewer = models.ForeignKey(GuestOrAdmin,on_delete=models.CASCADE,null=True)
    hotel = models.ForeignKey('hotel.Hotel',on_delete=models.CASCADE,null=True) 
    reviews = models.TextField()
    rating = models.CharField(max_length=20,choices=USER_RATING)
    review_date = models.DateTimeField(auto_now_add=True)
    included_feedback = models.BooleanField(default=False)
    

    # def get_hotel_model(self):
    #     from hotel.models import Hotel
    #     return Hotel
    
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.hotel = models.ForeignKey(self.get_hotel_model(),on_delete=models.CASCADE,null=True)