from django.shortcuts import render
from rest_framework import viewsets,filters
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Hotel,HotelImages
from .serializers import HotelImagesSerializers,HotelSerializers
from rest_framework import permissions 
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

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