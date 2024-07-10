from rest_framework import serializers
from .models import Transaction
from guest.models import Guest
from booking.models import Booking

class TransactionSerializer(serializers.ModelSerializer):
    guest = serializers.PrimaryKeyRelatedField(queryset=Guest.objects.all(),many=False)
    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(),many=False)
    class Meta:
        model = Transaction
        fields = "__all__"