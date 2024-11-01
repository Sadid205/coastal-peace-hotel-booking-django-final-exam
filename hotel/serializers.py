from rest_framework import serializers
from .models import Hotel,HotelImages,HotelsCategory,BestRoom,Service,FeedBack
from review.serializers import ReviewSerializer
import requests
from review.models import Review
from django.conf import settings
from guest_or_admin.models import GuestOrAdmin
from django.contrib.auth.models import User

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
        fields = ["id","name","images","uploaded_images","address","details","booking_price","offer_price","facilities","rules","rating","location","number_of_rooms","room_types","included_category"]


    def create(self,validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        hotel = Hotel.objects.create(**validated_data)
        self.handle_images(uploaded_images=uploaded_images,hotel=hotel)
        return hotel
    
    def update(self,instance,validated_data):
        uploaded_images = validated_data.pop("uploaded_images",None)
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        instance.save()
        if uploaded_images:
            self.delete_existing_images(instance)
            self.handle_images(uploaded_images=uploaded_images,hotel=instance)
        return instance



    def handle_images(self,uploaded_images,hotel):
        imgbb_api_key = settings.IMGBB_API_KEY
        for image in uploaded_images:
            try:
                response = requests.post(
                    "https://api.imgbb.com/1/upload",
                    params={"key":imgbb_api_key},
                    files={"image":image.read()},
                )
                response_data = response.json()
                if response.status_code == 200 and response_data.get("success"):
                    image_url = response_data["data"]["url"]
                    HotelImages.objects.create(hotel=hotel,image=image_url)
                else:
                    error_message = response_data.get("error",{}).get("message","Image upload failed.")
                    raise serializers.ValidationError(f"ImgBB Upload Error: {error_message}")
            except Exception as e:
                raise serializers.ValidationError(f"Image upload failed : {str(e)}")
            
    def delete_existing_images(self,hotel):
        images = hotel.images.all()
        for image in images:
            image.delete()


class HotelsCategorySerializer(serializers.ModelSerializer):
    hotel = HotelSerializers(many=True,read_only=True)
    hotel_list = serializers.ListField(child=serializers.IntegerField(),write_only=True)
    class Meta:
        model = HotelsCategory
        fields = "__all__"
    
    def create(self,validated_data):
        hotel_id_list = validated_data.pop('hotel_list',None)
        hotels_category = super().create(validated_data)

        if hotel_id_list is not None:
            new_hotel_list = []
            for hotel_id in hotel_id_list:
                try:
                    hotel = Hotel.objects.get(id=hotel_id)
                except Hotel.DoesNotExist:
                    continue
                if hotel:
                    if hotel.category.exists():
                        continue
                hotel.included_category = True
                hotel.save()
                new_hotel_list.append(hotel)
            hotels_category.hotel.set(new_hotel_list)
        return hotels_category
    
    def update(self,instance,validated_data):
        hotel_id_list = validated_data.pop('hotel_list',None)
        
        if hotel_id_list is not None:
            new_hotel_list = []
            for hotel_id in hotel_id_list:
                try:
                    hotel = Hotel.objects.get(id=hotel_id)
                except Hotel.DoesNotExist:
                    continue
                if hotel:
                    if hotel.category.exclude(id=instance.id).exists():
                        continue
                hotel.included_category = True
                hotel.save()
                new_hotel_list.append(hotel)
            validated_data['hotel'] = new_hotel_list
            instance = super().update(instance,validated_data)
            instance.hotel.set(new_hotel_list)
        return instance
    
class BestRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestRoom
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']

class GuestOrAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = GuestOrAdmin
        fields = ['id', 'image', 'mobile_number', 'admin_request', 'is_admin', 'is_master_admin', 'user', 'account']

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = GuestOrAdminSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'reviews', 'rating', 'review_date', 'included_feedback', 'hotel', 'reviewer',]


class FeedBackSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    review_list = serializers.ListField(child=serializers.IntegerField(),write_only=True)
    class Meta:
        model = FeedBack
        fields = "__all__"

    def get_review(self,obj):
        if obj.review.exists():
            reviews_data = ReviewSerializer(instance=obj.review.all(),many=True)
            return reviews_data.data
        return []

    def create(self,validated_data):
        review_id_list = validated_data.pop('review_list',None)
        feedback = super().create(validated_data)

        if review_id_list is not None:
            new_review_list = []
            for review_id in review_id_list:
                try:
                    review = Review.objects.get(id=review_id)
                except Review.DoesNotExist:
                    continue
                if review:
                    if review.feedback.exists():
                        continue
                review.included_feedback = True
                review.save()
                new_review_list.append(review)
            feedback.review.set(new_review_list)
        return feedback
    
    def update(self,instance,validated_data):
        review_id_list = validated_data.pop('review_list')

        if review_id_list is not None:
            new_review_list = []
            for review_id in review_id_list:
                try:
                    review = Review.objects.get(id=review_id)
                except Review.DoesNotExist:
                    continue
                if review.feedback.exclude(id=instance.id).exists():
                    continue
                review.included_feedback = True
                review.save()
                new_review_list.append(review)
            validated_data['review'] = new_review_list
            instance = super().update(instance,validated_data)
            instance.review.set(new_review_list)
        return instance            