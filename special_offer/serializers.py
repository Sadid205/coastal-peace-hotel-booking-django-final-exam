from rest_framework import serializers
from .models import SpecialOffer
from rest_framework.response import Response
from hotel.serializers import HotelSerializers
from hotel.models import Hotel
class SpecialOfferSerializer(serializers.ModelSerializer):
    hotel = HotelSerializers(many=True,read_only=True)
    hotel_list = serializers.ListField(child=serializers.IntegerField(),write_only=True)
    class Meta:
        model = SpecialOffer
        fields = '__all__'

    def create(self,validated_data):
        hotel_id_list = validated_data.pop('hotel_list',None)
        special_offer = super().create(validated_data)

        if hotel_id_list is not None:
            new_hotel_list = []
            print(hotel_id_list)
            for hotel_id in hotel_id_list:
                try:
                    hotel = Hotel.objects.get(id=hotel_id)
                except Hotel.DoesNotExist:
                    continue
                if hotel:
                    if hotel.offer_price is None:
                        hotel.offer_price = hotel.booking_price-(hotel.booking_price*(special_offer.discount/100))
                        new_hotel_list.append(hotel)
                        hotel.save()
            special_offer.hotel.set(new_hotel_list)
        return special_offer
    
    def update(self,instance,validated_data):
        hotel_id_list = validated_data.pop('hotel_list',None)
        new_discount = validated_data.get('discount',None)
        if new_discount is not None:
            instance.discount = new_discount
            instance.save()
        # instance = super().update(instance,validated_data)

        if hotel_id_list is not None:
            new_hotel_list = []
            print(hotel_id_list)
            for hotel_id in hotel_id_list:
                try:
                    hotel = Hotel.objects.get(id=hotel_id)
                except Hotel.DoesNotExist:
                    continue
                if hotel:
                    print(hotel.offer.exclude(id=instance.id).exists())
                    if hotel.offer.exclude(id=instance.id).exists():
                        continue
                    hotel.offer_price = hotel.booking_price-(hotel.booking_price*(instance.discount/100))
                    hotel.save()
                    new_hotel_list.append(hotel)
            validated_data['hotel'] = new_hotel_list
            instance = super().update(instance,validated_data)
            instance.hotel.set(new_hotel_list)
        return instance



