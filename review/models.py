from django.db import models
from hotel.models import Hotel
from guest.models import Guest
from .constraints import USER_RATING
# Create your models here.
class Review(models.Model):
    reviewer = models.ForeignKey(Guest,on_delete=models.CASCADE,null=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True)
    reviews = models.TextField()
    rating = models.CharField(max_length=20,choices=USER_RATING)
    review_date = models.DateTimeField(auto_now_add=True)
