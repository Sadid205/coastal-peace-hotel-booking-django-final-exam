from django.urls import path,include
from .views import AccountViewSet,DepositViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('list',AccountViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('deposit/',DepositViewSet.as_view(),name="deposit"),
]

