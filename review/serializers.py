from rest_framework import serializers
from .models import Review
from guest_or_admin.models import GuestOrAdmin
from hotel.models import Hotel
from django.contrib.auth.models import User

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestOrAdmin
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(queryset=GuestOrAdmin.objects.all(),many=False)
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(),many=False)
    review_date = serializers.StringRelatedField(many=False)
    guest_reviewer = serializers.SerializerMethodField()
    user_data = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ('review_date','guest_reviewer')

    def get_guest_reviewer(self,obj):
        if obj.reviewer:
            reviewer_data = ReviewerSerializer(instance=obj.reviewer).data
            return reviewer_data
        return None
    
    def get_user_data(self,obj):
        if obj.reviewer:
            return UserSerializer(instance=obj.reviewer.user).data
        return None
        