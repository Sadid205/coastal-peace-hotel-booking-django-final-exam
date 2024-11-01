from django.shortcuts import render
from rest_framework import viewsets
from .models import SpecialOffer
from .serializers import SpecialOfferSerializer
from rest_framework.response import Response
from rest_framework import permissions 

# Create your views here.
class SpecialOfferView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer

    def destroy(self,request,*args,**kwargs):
        instance = self.get_object()
        hotel_list = instance.hotel.all()
        
        for hotel in hotel_list:
            hotel.offer_price = None
            hotel.save()
        
        super().destroy(request,*args,**kwargs)

        return Response({"success":{"Successfully deleted":instance.offer_name}})


    