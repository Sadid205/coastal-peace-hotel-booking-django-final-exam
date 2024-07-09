from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions 
# Create your views here.

class ReviewerCanEditOtherWiseReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.guest == obj.reviewer:
            return True
        else:
            return False


class ReviewListForSpecificHotel(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        hotel_id = request.query_params.get("hotel_id")
        if hotel_id:
            return queryset.filter(hotel = hotel_id)
        return queryset

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [ReviewListForSpecificHotel]
    permission_classes = [permissions.IsAuthenticated,ReviewerCanEditOtherWiseReadOnly]