from django.db import models

# Create your models here.
from .constraints import STAR_RATING 
class Hotel(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    details = models.TextField()
    booking_price = models.IntegerField()
    offer_price = models.IntegerField(null=True,blank=True)
    facilities = models.TextField()
    rules = models.TextField()
    rating = models.CharField(max_length=10,choices=STAR_RATING)
    location = models.CharField(max_length=500)
    number_of_rooms = models.IntegerField()
    room_types = models.CharField(max_length=500)
    included_category = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="images")
    image = models.URLField(max_length=2000)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel.name
    

class HotelsCategory(models.Model):
    category_name = models.CharField(max_length=300)
    hotel = models.ManyToManyField(Hotel,related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return self.category_name
    
class BestRoom(models.Model):
    room_name = models.CharField(max_length=300)
    size = models.CharField(max_length=400)
    capacity = models.CharField(max_length=300)
    price = models.IntegerField(default=None)
    images = models.JSONField(default=list)
    description = models.TextField()
    location = models.URLField(max_length=2000)
    amenities = models.JSONField(default=list)
    rating = models.CharField(max_length=10,choices=STAR_RATING,null=True,blank=True)
    review = models.ManyToManyField('review.Review',related_name='best_room',blank=True) 


    def __str__(self)->str:
        return self.room_name
    

class Service(models.Model):
    service_name = models.CharField(max_length=300)
    images = models.JSONField(default=list)
    price = models.IntegerField(default=None)
    description = models.TextField()
    review = None

    def __str__(self)->str:
        return self.service_name
    
    def get_review_model(self):
        from review.models import Review
        return Review
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.review = models.ManyToManyField(self.get_review_model(),related_name='service')



class FeedBack(models.Model):
    feedback_name = models.CharField(max_length=300)
    review = models.ManyToManyField('review.Review',related_name='feedback',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return self.feedback_name
    