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
from rest_framework import filters
from sslcommerz_lib import SSLCOMMERZ 
import time
import random
from django.contrib.auth.models import User
import requests

import environ
env = environ.Env()
environ.Env.read_env()

store_password = env("STORE_PASSWORD")
store_id=env('STORE_ID')

# from rest_framework.authentication import TokenAuthentication
# Create your views here.

class GetAccountForSpecificUser(filters.BaseFilterBackend):
    def filter_queryset(self,request,queryset,view):
        user_id = request.query_params.get("user_id")
        if user_id:
            return queryset.filter(user=user_id)
        return queryset

class AccountViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [GetAccountForSpecificUser]



class DepositViewSet(APIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = DepositSerializer

    def unique_transaction_id(self):
        return f"{int(time.time()*1000)}{random.randint(1000,9999)}"
    
    def get(self,request):
        serializer = self.serializer_class()
        fields = serializer.get_fields()
        field_object = {key_name:str(key_value) for key_name,key_value in fields.items()}
        return Response(field_object)
    def post(self,request):
        serializer = self.serializer_class(data=request.data,context={'request':request})

        
        # print(store_id,store_password)
        if serializer.is_valid():
            user,amount =  serializer.save()
            settings = { 'store_id':store_id, 'store_pass':store_password, 'issandbox': True }
            sslcz = SSLCOMMERZ(settings)
            post_body = {}
            post_body['total_amount'] = amount
            post_body['currency'] = "BDT"
            post_body['tran_id'] = self.unique_transaction_id()
            post_body['success_url'] = f"http://127.0.0.1:8000/accounts/deposit/payment/{post_body['tran_id']}/{user.id}/{amount}/"
            post_body['fail_url'] = f"http://127.0.0.1:8000/accounts/deposit/payment/{post_body['tran_id']}/{user.id}/{amount}/"
            post_body['cancel_url'] = f"http://127.0.0.1:8000/accounts/deposit/payment/{post_body['tran_id']}/{user.id}/{amount}/"
            post_body['emi_option'] = 0
            post_body['cus_name'] = f"{user.first_name} {user.last_name}"
            post_body['cus_email'] = f"{user.email}"
            post_body['cus_phone'] = f"{user.guest.mobile_number}"
            post_body['cus_add1'] = "customer address"
            post_body['cus_city'] = "Dhaka"
            post_body['cus_country'] = "Bangladesh"
            post_body['shipping_method'] = "NO"
            post_body['multi_card_name'] = ""
            post_body['num_of_item'] = 1
            post_body['product_name'] = "Test"
            post_body['product_category'] = "Test Category"
            post_body['product_profile'] = "general"


            response = sslcz.createSession(post_body) # API response
            # print(response)
            print(response['GatewayPageURL'])
            return Response({"redirect_url":response['GatewayPageURL']})
    


class PaymentSuccessOrFailViewSet(APIView):
    
    def post(self,request,tran_id,user_id,amount):

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None

        val_id = request.data.get("val_id")
        
        if val_id:
            varification_url = f"https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php?val_id={val_id}&store_id={store_id}&store_passwd={store_password}&v=1&format=json"
            varification_response = requests.get(varification_url)
            varification_data = varification_response.json()
            print(varification_response)
            if varification_data.get("status")=="VALID":
                if user is not None:
                    user.account.balance+=amount
                    user.account.save()
                    new_transaction = Transaction.objects.create(guest=user.guest,transaction_id=tran_id,transaction_types="Deposit",transaction_amount=amount)
                    new_transaction.save()
                    email_subject = "Deposit successfully"
                    email_body = render_to_string("deposit_success_email.html",{"user":user,"amount":amount})
                    email = EmailMultiAlternatives(email_subject,'',to=[user.email])
                    email.attach_alternative(email_body,"text/html")
                    email.send()
                    redirect_url = f"http://localhost:5173/deposit?status=Deposit successfull.Please check your email.&is_success=true"
                    return redirect(redirect_url)
                else:
                    redirect_url = f"http://localhost:5173/deposit?status=User doesn't exists.&is_success=false"
                    return redirect(redirect_url)
            else:
                redirect_url = f"http://localhost:5173/deposit?status=Payment varification failed!&is_success=false"
                return redirect(redirect_url)
        else:
            redirect_url = f"http://localhost:5173/deposit?status=Something went wrong!&is_success=false"
            return redirect(redirect_url)
