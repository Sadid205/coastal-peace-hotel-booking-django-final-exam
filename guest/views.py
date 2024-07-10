from django.shortcuts import render
from .models import Guest
from .serializers import GuestSerializer,RegistrationSerializer,UserLoginSerializer,EditProfileSerializer,ChangePasswordSerializer
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
# Create your views here.

class GuestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class RegistrationApiView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = RegistrationSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirmation_link = f"https://coastal-peace-hotel-booking.onrender.com/guest/active/{uid}/{token}"
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
        return redirect("login")
    else:
        return redirect("register")
    
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
    def post(self,request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"Success":"Logout Success"})
    
class EditProfileViewSet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EditProfileSerializer
    def get(self,request):
        user = request.user
        serializer = self.serializer_class(instance=user)
        return Response(serializer.data)

    def post(self,request):
        user = request.user
        serializer = self.serializer_class(instance=user,data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class PasswordChangeViewSet(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    

