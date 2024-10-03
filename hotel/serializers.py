from rest_framework import serializers
from .models import Hotel,HotelImages
import requests
from django.conf import settings

class HotelImagesSerializers(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField(many=False)
    class Meta:
        model = HotelImages
        fields = ['id','hotel','image','upload_date']
  
    
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
        imgbb_api_key = settings.IMGBB_API_KEY
        for image in uploaded_images:
            try:
                response = requests.post(
                    "https://api.imgbb.com/1/upload",
                    params={"key":imgbb_api_key},
                    files={"image":image.read()},
                )
                response_data = response.json()
                if response.status_code==200 and response_data.get("success"):
                    image_url = response_data["data"]["url"]
                    HotelImages.objects.create(hotel=hotel,image=image_url)
                else:
                    error_message = response_data.get("error",{}).get("message","Image upload failed.")
                    raise serializers.ValidationError(f"ImgBB Upload Error:{error_message}")
            except Exception as e:
                raise serializers.ValidationError(f"Image upload failed: {str(e)}")
        return hotel