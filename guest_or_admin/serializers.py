from rest_framework import serializers
from .models import GuestOrAdmin
from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
import requests

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class GuestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    account = serializers.StringRelatedField(many=False)
    class Meta:
        model = GuestOrAdmin
        fields = "__all__"
    

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    image = serializers.ImageField(required=False)
    mobile_number = serializers.CharField(required=True)
    admin_request = serializers.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username','image','first_name','last_name','email','password','confirm_password','mobile_number','admin_request']

    def save(self):
        username = self.validated_data['username']
        image = self.validated_data['image']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        mobile_number = self.validated_data['mobile_number']
        admin_request = self.validated_data["admin_request"]
        imgbb_api_key = settings.IMGBB_API_KEY

        if password != confirm_password:
            raise serializers.ValidationError({"Error" : "Password doesn't matched."})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Error" : "Email already exists."})
        user_account = User(username=username,email=email,first_name=first_name,last_name=last_name)
        user_account.set_password(password)
        user_account.is_active = False
        user_account.save()
        account_number=str(10000000000000+user_account.id)
        new_account = Account(user=user_account,account_number=account_number)
        new_account.save()
        try:
            response = requests.post(
                "https://api.imgbb.com/1/upload",
                params={"key":imgbb_api_key},
                files={"image":image.read()},
            )
            response_data = response.json()
            if response.status_code==200 and response_data.get("success"):
                image_url = response_data["data"]["url"]
                guest_account = GuestOrAdmin(user=user_account,account=new_account,image=image_url,mobile_number=mobile_number,admin_request=admin_request)
                guest_account.save()
            else:
                error_message = response_data.get("error",{}).get("message","Image upload failed.")
                raise serializers.ValidationError(f"ImgBB Upload Error:{error_message}")
        except Exception as e:
            raise serializers.ValidationError(f"Image upload failed: {str(e)}")
        return user_account
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class EditProfileSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required=True)
    # mobile_number = serializers.CharField(required=True)
   #'image','mobile_number'
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def update(self,instance,validated_data):
        instance.username = validated_data.get("username",instance.email)
        instance.first_name = validated_data.get("first_name",instance.first_name)
        instance.last_name = validated_data.get("last_name",instance.last_name)
        instance.email = validated_data.get("email",instance.email)
        instance.save()
        
        # guest_account = instance.guest
        # guest_account.image = validated_data.get("image",guest_account.image)
        # guest_account.mobile_number = validated_data.get("mobile_number",guest_account.mobile_number)
        # guest_account.save()
        return instance
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True,write_only=True)
    new_password = serializers.CharField(required=True,write_only=True,validators=[validate_password])
    retype_new_password = serializers.CharField(required=True,write_only=True)

    class Meta:
        model = User
        fields = ['old_password','new_password','retype_new_password']

    def validate(self,attrs):
        user = self.context['request'].user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"validation_error":"Password doesn't match!"})
        if attrs['new_password'] != attrs['retype_new_password']:
            raise serializers.ValidationError({"validation_error":"Password doesn't match!"})
        return attrs
    
    
    def update(self,instance,validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
    
class GuestOrAdminSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    account_number = serializers.SerializerMethodField()
    class Meta:
        model = GuestOrAdmin
        fields = "__all__"
    def get_email(self,obj):
        return obj.user.email
    def get_user_name(self,obj):
        return obj.user.username
    def get_account_number(self,obj):
        return obj.account.account_number

# class AdminListSerializer(serializers.ModelSerializer):
#     user_email = serializers.SerializerMethodField()
#     user_name = serializers.SerializerMethodField()
#     account_number = serializers.SerializerMethodField()
#     class Meta:
#         model = GuestOrAdmin
#         fields ="__all__"
#     def get_user_email(self,obj):
#         return obj.user.email
#     def get_user_name(self,obj):
#         return obj.user.username
#     def get_account_number(self,obj):
#         return obj.account.account_number
    

