from django.shortcuts import render
from rest_framework import viewsets,filters
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Hotel,HotelImages,HotelsCategory,BestRoom,Service,FeedBack
from .serializers import HotelImagesSerializers,HotelSerializers,HotelsCategorySerializer,BestRoomSerializer,ServicesSerializer,FeedBackSerializer
from rest_framework import permissions 
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# from rest_framework.authentication import TokenAuthentication
# Create your views here.

class HotelPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class HotelViewSet(viewsets.ModelViewSet):
  
    parser_classes = [MultiPartParser,FormParser]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = HotelPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['name','address','location','facilities','details','booking_price','number_of_rooms','room_types','rules']

class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImages.objects.all()
    serializer_class = HotelImagesSerializers
    permission_classes = [permissions.IsAuthenticated]


class HotelsCategoryViewSet(viewsets.ModelViewSet):
    queryset = HotelsCategory.objects.all()
    serializer_class = HotelsCategorySerializer

    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        hotel_list = instance.hotel.all()

        for hotel in hotel_list:
            hotel.included_category = False
            hotel.save()
        super().destroy(request,*args,**kwargs)

        return Response({"success":{"Successfully deleted":instance.category_name}})


class BestRoomViewSet(viewsets.ModelViewSet):
    queryset = BestRoom.objects.all()
    serializer_class = BestRoomSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer

class FeedBackViewSet(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        review_list = instance.review.all()

        for review in review_list:
            review.included_feedback = False
            review.save()
        super().destroy(request,*args,**kwargs)

        return Response({"success":{"Successfully deleted":{instance.feedback_name}}})