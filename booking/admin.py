from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Booking
def bookingEmail(subject,request,obj,booking_status):
    email_subject = subject
    email_body = render_to_string("booking_email.html",{'user':request.user,'hotel':obj.hotel,'booking_status':booking_status})
    email = EmailMultiAlternatives(email_subject,'',to=[obj.guest.user.email])
    email.attach_alternative(email_body,"text/html")
    email.send()

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        if change:
            if obj.booking_status=="Confirmed":
                bookingEmail("Booking Confirmed!",request,obj,booking_status="Confirmed")
        super().save_model(request,obj,form,change)

admin.site.register(Booking,BookingAdmin)
