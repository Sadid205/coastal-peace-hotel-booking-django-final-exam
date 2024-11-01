from .serializers import BookingSerializer,HotelBookingSerializer,PendingBookingSerializer,BookingInfoSerializer
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
from rest_framework import filters
from django.db.models import Q
from guest_or_admin.models import GuestOrAdmin
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import api_view
# Create your views here.

def sendEmail(user,email,email_subject,html_template,hotel):
    email_subject = email_subject
    email_body = render_to_string(html_template,{'user':user,'hotel':hotel})
    email = EmailMultiAlternatives(email_subject,'',to=[email])
    email.attach_alternative(email_body,"text/html")
    email.send()

class BookingForSpecificUser(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        hotel_id = request.query_params.get("hotel_id")
        guest_id = request.query_params.get("guest_id")
        if hotel_id and guest_id:
            filtered_queryset = queryset.filter(hotel=hotel_id,guest=guest_id)
            return filtered_queryset
        if guest_id:
            filter_user_booking = queryset.filter(guest=guest_id)
            return filter_user_booking
        return queryset



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [BookingForSpecificUser]

def successBooking(request,new_hotel,guest,number_of_guests,room_type):
    new_booking =  Booking.objects.create(hotel=new_hotel,guest=guest)
    new_booking.number_of_guests = number_of_guests
    new_booking.room_type = room_type
    if new_hotel.offer_price is not None:
        request.user.account.balance-=new_hotel.offer_price
    else:
        request.user.account.balance-=new_hotel.booking_price
    request.user.account.save()
    new_booking.save()
    new_transaction = Transaction.objects.create(guest=guest,transaction_types="Booking",booking=new_booking)
    new_transaction.save()
    sendEmail(user=request.user,email=request.user.email,email_subject="Booking request success!",html_template="booking_success_email.html",hotel=new_hotel)
    admin_account_list = GuestOrAdmin.objects.filter(is_admin=True)
    if len(admin_account_list)>0:
        for admin_account in admin_account_list:
            sendEmail(user=admin_account.user,email=admin_account.user.email,email_subject="Booking request",html_template="booking_request.html",hotel=new_hotel)
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
                        return Response({"Response":"Your request is pending."})
                    case "Confirmed":
                        return Response({"Response":"Your request is confirmed.Please come to hotel and checked-in."})
                    case "Cancelled":
                        if request.user.account.balance >= new_hotel.booking_price:
                            successBooking(request=request,new_hotel=new_hotel,guest=request.user.guest,number_of_guests=number_of_guests,room_type=room_type)
                            return Response({"Response":f"You have successfully post a request to booking {new_hotel.name} hotel.Please wait for confirmation email."})
                        else:
                            return Response({"Response":f"Please add extra more {new_hotel.booking_price-request.user.account.balance}$"})
                    case "Checked-in":
                        return Response({"Response":"You are staying this hotel right now.You can not book this hotel again.Please checked-out."})
                    case "Checked-out":
                        if request.user.account.balance >= new_hotel.booking_price:
                            successBooking(request=request,new_hotel=new_hotel,guest=request.user.guest,number_of_guests=number_of_guests,room_type=room_type)
                            return Response({"Response":f"You have successfully post a request to booking {new_hotel.name} hotel.Please wait for confirmation email."})
                        else:
                            return Response({"Response":f"Please add extra more {new_hotel.booking_price-request.user.account.balance}$"})
            else:
                if request.user.account.balance >= new_hotel.booking_price:
                    successBooking(request=request,new_hotel=new_hotel,guest=request.user.guest,number_of_guests=number_of_guests,room_type=room_type)
                    return Response({"Response":f"You have successfully post a request to booking {new_hotel.name} hotel.Please wait for confirmation email."})
                else:
                    return Response({"Response":f"Please add extra more {new_hotel.booking_price-request.user.account.balance}$"})
        return Response(serializer.errors)
      
                    

            
class PendingBooking(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        pending_booking_list = Booking.objects.filter(booking_status="Pending")
        serializer = PendingBookingSerializer(pending_booking_list,many=True)
        return Response({"pending_booking_list":serializer.data})
    

class ConfirmBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def patch(self,request,*args,**kwargs):
        booking_id = kwargs.get("booking_id")
        booking_object = Booking.objects.get(id=booking_id)
        booking_object.booking_status = "Confirmed"
        booking_object.save()
        sendEmail(user=request.user,email=request.user.email,email_subject="Booking request approved.",html_template="booking_confirmed.html",hotel=booking_object.hotel)
        return Response({"Success":"Successfully confirmed booking."})
    
class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def patch(self,request,*args,**kwargs):
        booking_id = kwargs.get("booking_id")
        booking_object = Booking.objects.get(id=booking_id)
        booking_object.booking_status = "Cancelled"
        booking_object.save()
        sendEmail(user=request.user,email=request.user.email,email_subject="Booking request rejected.",html_template="booking_canceled.html",hotel=booking_object.hotel)
        return Response({"Success":"Successfully cancelled booking."})
    

class BookingInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        total_bookings = len(Booking.objects.filter(Q(booking_status="Pending")|Q(booking_status="Confirmed")|Q(booking_status="Checked-in")))
        total_user = len(GuestOrAdmin.objects.filter(is_admin=False))
        total_booking_request = len(Booking.objects.filter(booking_status="Pending"))
        total_hotel = len(Hotel.objects.all())
        booking_data = {
            "total_bookings":total_bookings,
            "total_user":total_user,
            "total_booking_request":total_booking_request,
            "total_hotel":total_hotel,
        }
        serializer = BookingInfoSerializer(booking_data)
        return Response({"booking_info":serializer.data})
    

@api_view(['GET'])
def GetDailyBookingCounts(request):
    now = timezone.now()
    daily_counts = []
    days_name = []

    for i in range(7):
        day_start = now - timedelta(days=i+1)
        day_end = now - timedelta(days=i)

        count = Booking.objects.filter(booking_date__gte=day_start,booking_date__lt=day_end).count()
        daily_counts.append(count)

        day_name = (now - timedelta(days=i)).strftime('%A')
        days_name.append(day_name)

    daily_counts.reverse()
    days_name.reverse()

    day_booking_data = list(zip(days_name,daily_counts))
    return Response(day_booking_data)