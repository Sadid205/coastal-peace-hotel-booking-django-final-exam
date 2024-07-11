from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer,DepositSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from rest_framework import permissions
from transaction.models import Transaction
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



class DepositViewSet(APIView):
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = DepositSerializer
    def get(self,request):
        serializer = self.serializer_class()
        fields = serializer.get_fields()
        field_object = {key_name:str(key_value) for key_name,key_value in fields.items()}
        return Response(field_object)
    def post(self,request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        if serializer.is_valid():
           user,amount =  serializer.save()
           transaction_id = str(10000000000000+request.user.id)
           new_transaction = Transaction.objects.create(guest=request.user.guest,transaction_id=transaction_id,transaction_types="Deposit")
           new_transaction.save()
           email_subject = "Deposit successfully"
           email_body = render_to_string("deposit_success_email.html",{"user":user,"amount":amount})
           email = EmailMultiAlternatives(email_subject,'',to=[user.email])
           email.attach_alternative(email_body,"text/html")
           email.send()
           return Response({"Success":"Please check your email."})

