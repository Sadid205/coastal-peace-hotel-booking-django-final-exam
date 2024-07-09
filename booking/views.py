from .serializers import BookingSerializer,HotelBookingSerializer
from .models import Booking
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from hotel.models import Hotel
from .models import Booking
from transaction.models import Transaction
from rest_framework.response import Response

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

def successBooking(request,new_hotel,guest,number_of_guests,room_type):
    new_booking =  Booking.objects.create(hotel=new_hotel,guest=guest)
    booking_id = str(10000000+request.user.id)
    new_booking.number_of_guests = number_of_guests
    new_booking.room_type = room_type
    new_booking.booking_id = booking_id
    request.user.account.balance-=new_hotel.booking_price
    request.user.account.save()
    new_booking.save()
    transaction_id = str(10000000000000+request.user.id)
    new_transaction = Transaction.objects.create(guest=guest,transaction_id=transaction_id,transaction_types="Booking",booking=new_booking)
    new_transaction.save()
    email_subject = "Booking request success!"
    email_body = render_to_string("booking_success_email.html",{'user':request.user,'hotel':new_hotel})
    email = EmailMultiAlternatives(email_subject,'',to=[request.user.email])
    email.attach_alternative(email_body,"text/html")
    email.send()
    return new_booking

class HotelBookingViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        serializer = HotelBookingSerializer()
        fields = serializer.get_fields()
        field_object = {field_key:str(field_value) for field_key,field_value in fields.items()}
        return Response(field_object)
    
    def post(self,request,*args,**kwargs):
        hotel_id = kwargs.get("hotel_id")
        serializer = HotelBookingSerializer(data=request.data)
       
        if serializer.is_valid():
            number_of_guests = serializer.validated_data.get("number_of_guests")
            room_type = serializer.validated_data.get("room_type")
            try:
                new_hotel = Hotel.objects.get(id=hotel_id)
            except Hotel.DoesNotExist:
                new_hotel = None
                return Response({"Error":"This hotel is not available at this moment."})
            if Booking.objects.filter(hotel=new_hotel,guest=request.user.guest):
                booking = Booking.objects.filter(hotel=new_hotel,guest=request.user.guest).order_by('-booking_date').first()
                status = booking.booking_status
                match status:
                    case "Pending":
                        return Response({"Pending":"Your request is pending."})
                    case "Confirmed":
                        return Response({"Confirmed":"Your request is confirmed.Please come to hotel and checked-in."})
                    case "Cancelled":
                        if request.user.account.balance >= new_hotel.booking_price:
                            successBooking(request=request,new_hotel=new_hotel,guest=request.user.guest,number_of_guests=number_of_guests,room_type=room_type)
                            return Response({"Success":f"You have successfully post a request to booking {new_hotel.name} hotel.Please wait for confirmation email."})
                        else:
                            return Response({"Insufficient balance":f"Please add extra more {new_hotel.booking_price-request.user.account.balance}$"})
                    case "Checked-in":
                        return Response({"Checked-in":"You are staying this hotel right now.You can not book this hotel again.Please checked-out."})
                    case "Checked-out":
                        if request.user.account.balance >= new_hotel.booking_price:
                            successBooking(request=request,new_hotel=new_hotel,guest=request.user.guest,number_of_guests=number_of_guests,room_type=room_type)
                            return Response({"Success":f"You have successfully post a request to booking {new_hotel.name} hotel.Please wait for confirmation email."})
                        else:
                            return Response({"Insufficient balance":f"Please add extra more {new_hotel.booking_price-request.user.account.balance}$"})
            else:
                if request.user.account.balance >= new_hotel.booking_price:
                    successBooking(request=request,new_hotel=new_hotel,guest=request.user.guest,number_of_guests=number_of_guests,room_type=room_type)
                    return Response({"Success":f"You have successfully post a request to booking {new_hotel.name} hotel.Please wait for confirmation email."})
                else:
                    return Response({"Insufficient balance":f"Please add extra more {new_hotel.booking_price-request.user.account.balance}$"})
        return Response(serializer.errors)
      
                    

            
