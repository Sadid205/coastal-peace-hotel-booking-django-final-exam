from rest_framework import serializers
from .models import Hotel,HotelImages
class HotelImagesSerializers(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField(many=False)
    class Meta:
        model = HotelImages
        fields = ['id','hotel','image']
  
    
class HotelSerializers(serializers.ModelSerializer):
    images = HotelImagesSerializers(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False,use_url=False),
        write_only=True
    )
    class Meta:
        model = Hotel
        fields = ["id","name","images","uploaded_images","address","details","booking_price","facilities","rules","rating","location","number_of_rooms","room_types",]


    def create(self,validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        hotel = Hotel.objects.create(**validated_data)
        for image in uploaded_images:
            HotelImages.objects.create(hotel=hotel,image=image)
        return hotel