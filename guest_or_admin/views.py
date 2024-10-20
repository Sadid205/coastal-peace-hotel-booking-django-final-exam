from django.shortcuts import render
from .models import GuestOrAdmin
from .serializers import GuestSerializer,RegistrationSerializer,UserLoginSerializer,EditProfileSerializer,ChangePasswordSerializer,GuestOrAdminSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from .serializers import UserSerializer
from rest_framework import filters
from django.db.models import Q
# from rest_framework.authentication import TokenAuthentication

# Create your views here.

class GuestForSpecificUserAccount(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        user_id = request.query_params.get("user_id")
        if user_id:
            return queryset.filter(user=user_id)
        return queryset
    
class UserForSpecificGuestAccount(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        guest_id = request.query_params.get("guest_id")
        if guest_id:
            return queryset.filter(guest=guest_id)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [UserForSpecificGuestAccount]

class GuestViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = GuestOrAdmin.objects.all()
    serializer_class = GuestSerializer
    filter_backends = [GuestForSpecificUserAccount]

class RegistrationApiView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = RegistrationSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirmation_link = f"https://cph-hotel-booking.vercel.app/guest/active/{uid}/{token}"
            email_subject = "Email Confirmation Link"
            email_body = render_to_string('email_confirmation.html',{'confirmation_link':confirmation_link,"user":user})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Please check your mail for confirmation")
        return Response(serializer.errors)
    
def activate(request,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect("https://cph-booking.netlify.app/")
    else:
        return redirect("https://cph-booking.netlify.app/register")
    
class UserLoginApiView(APIView):
    serializer_class = UserLoginSerializer
    def get(self,request):
        serializer = self.serializer_class()
        fields = serializer.get_fields()
        field_object = {field_key:str(field_value) for field_key,field_value in fields.items()}
        return Response(field_object)

    def post(self,request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'Token':token.key,'user_id':user.id})
            else:
                return Response({'Error':"Invalid Credential!"})
        return Response(serializer.errors)

class UserLogoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"Success":"Logout Success"})
    
class EditProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = EditProfileSerializer
    def get_object(self):
        return self.request.user
    # def get(self,request):
    #     user = request.user
    #     serializer = self.serializer_class(instance=user)
    #     return Response(serializer.data)

    # def post(self,request):
    #     user = request.user
    #     serializer = self.serializer_class(instance=user,data=request.data,context={'request':request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    
class PasswordChangeViewSet(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    

class AdminRequestViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        guest_or_admin_object = GuestOrAdmin.objects.filter(admin_request=True)
        serializers = GuestOrAdminSerializer(guest_or_admin_object,many=True)
        return Response({"admin_request":serializers.data})

class AdminListViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        admin_object = GuestOrAdmin.objects.filter(is_admin=True)
        serializers = GuestOrAdminSerializer(admin_object,many=True)
        return Response({"admin_list":serializers.data})

class UserListViewSet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user_object = GuestOrAdmin.objects.filter(Q(is_admin=False),Q(is_master_admin=False))
        serializers = GuestOrAdminSerializer(user_object,many=True)
        return Response({"user_list":serializers.data})
        