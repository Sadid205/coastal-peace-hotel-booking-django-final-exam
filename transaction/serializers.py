from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    guest = serializers.StringRelatedField(many=True)
    booking = serializers.StringRelatedField(many=True)
    class Meta:
        model = Transaction
        fields = "__all__"