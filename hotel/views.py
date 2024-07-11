from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser,FormParser
from .models import Hotel,HotelImages
from .serializers import HotelImagesSerializers,HotelSerializers
from rest_framework import permissions 
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# Create your views here.

class HotelPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class HotelViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser,FormParser]
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = HotelPagination

class HotelImageViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = HotelImages.objects.all()
    serializer_class = HotelImagesSerializers
    permission_classes = [permissions.IsAuthenticated]