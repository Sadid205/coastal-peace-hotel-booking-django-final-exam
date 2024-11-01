from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BannerView
router = DefaultRouter()
router.register('list',BannerView)
urlpatterns = [
    path('',include(router.urls))
]