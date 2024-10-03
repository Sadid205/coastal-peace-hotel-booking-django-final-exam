from rest_framework import serializers
from .models import Booking
from guest_or_admin.models import GuestOrAdmin
from hotel.models import Hotel
from django.db.models import Q

class BookingSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField(many=False)
    guest = serializers.StringRelatedField(many=False)
    class Meta:
        model = Booking
        fields = "__all__"

class HotelBookingSerializer(serializers.Serializer):
    number_of_guests = serializers.IntegerField(required=True)
    room_type = serializers.CharField(required=True)
    

class PendingBookingSerializer(serializers.ModelSerializer):
    hotel_name = serializers.SerializerMethodField()
    guest_name = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = '__all__'
    def get_hotel_name(self,obj):
        return  obj.hotel.name
    def get_guest_name(self,obj):
        return obj.guest.user.username

class BookingInfoSerializer(serializers.Serializer):
    total_bookings = serializers.IntegerField()
    total_user = serializers.IntegerField()
    total_booking_request = serializers.IntegerField()
    total_hotel = serializers.IntegerField()
