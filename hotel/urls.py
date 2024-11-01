from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet,HotelImageViewSet,HotelsCategoryViewSet,BestRoomViewSet,ServicesViewSet,FeedBackViewSet

router = DefaultRouter()
router.register('list',HotelViewSet)
router.register('images',HotelImageViewSet)
router.register('category',HotelsCategoryViewSet)
router.register('best_rooms',BestRoomViewSet)
router.register('services',ServicesViewSet)
router.register('feedback',FeedBackViewSet)
urlpatterns = [
    path('',include(router.urls))
]
