from django.contrib import admin
from .models import Hotel,HotelImages,HotelsCategory
# Register your models here.

class MultipleImagesInline(admin.TabularInline):
    model = HotelImages
    extra = 1

class ChangeHotelAdmin(admin.ModelAdmin):
    inlines = [MultipleImagesInline]

admin.site.register(Hotel,ChangeHotelAdmin)
admin.site.register(HotelImages)
admin.site.register(HotelsCategory)