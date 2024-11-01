from rest_framework import serializers
from .models import Transaction
from guest_or_admin.models import GuestOrAdmin
from booking.models import Booking

class TransactionSerializer(serializers.ModelSerializer):
    guest = serializers.PrimaryKeyRelatedField(queryset=GuestOrAdmin.objects.all(),many=False)
    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(),many=False)
    class Meta:
        model = Transaction
        fields = "__all__"
    
