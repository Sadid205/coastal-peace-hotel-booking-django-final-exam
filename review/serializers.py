from rest_framework import serializers
from .models import Review
from guest_or_admin.models import GuestOrAdmin
from hotel.models import Hotel

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(queryset=GuestOrAdmin.objects.all(),many=False)
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(),many=False)
    review_date = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = "__all__"