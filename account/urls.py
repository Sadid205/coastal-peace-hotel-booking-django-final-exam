from django.urls import path,include
from .views import AccountViewSet,DepositViewSet,PaymentSuccessOrFailViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('list',AccountViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('deposit/',DepositViewSet.as_view(),name="deposit"),
    path('deposit/payment/<int:tran_id>/<int:user_id>/<int:amount>/',PaymentSuccessOrFailViewSet.as_view(),name='payment')
]

