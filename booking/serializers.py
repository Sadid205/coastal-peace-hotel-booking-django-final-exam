from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField(many=False)
    guest = serializers.StringRelatedField(many=False)
    class Meta:
        model = Booking
        fields = "__all__"

class HotelBookingSerializer(serializers.Serializer):
    number_of_guests = serializers.IntegerField(required=True)
    room_type = serializers.CharField(required=True)
    