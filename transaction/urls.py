from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet
from django.urls import path,include
router = DefaultRouter()
router.register('list',TransactionViewSet)
urlpatterns = [
    path('',include(router.urls))
]
