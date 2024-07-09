from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet,HotelImageViewSet

router = DefaultRouter()
router.register('list',HotelViewSet)
router.register('images',HotelImageViewSet)
urlpatterns = [
    path('',include(router.urls))
]
