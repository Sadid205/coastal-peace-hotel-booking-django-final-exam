from django.db import models
# Create your models here.

class Banner(models.Model):
    banner_name = models.CharField(max_length=300,blank=True,null=True)
    image = models.JSONField(default=list)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.banner_name