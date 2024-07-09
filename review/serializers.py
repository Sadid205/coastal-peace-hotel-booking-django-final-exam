from rest_framework import serializers
from .models import Review
from guest.models import Guest
from hotel.models import Hotel

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(queryset=Guest.objects.all(),many=False)
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(),many=False)
    class Meta:
        model = Review
        fields = "__all__"